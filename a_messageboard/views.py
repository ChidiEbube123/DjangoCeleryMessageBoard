from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
import threading
from .tasks import *
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.views.decorators.cache import cache_page
from django.core.cache import cache

@login_required
def aal_subs(request):
    cache_key='message_boards'
    message_boards = cache.get(cache_key) 
    if not message_boards:
        message_boards = MessageBoard.objects.all()  # Expensive DB query
        cache_key=f'message_boards{message_boards.count}'
        cache.set(cache_key, message_boards, timeout=60*15) 
    return render(request, 'a_messageboard/messageboards.html', {'message_boards':message_boards})

@cache_page(60 * 60)  # Cache for 15 minutes
def create_messageboard(request):
    if request.method == 'POST':
        form = MessageBoardCreateForm(request.POST, request.FILES)
        if form.is_valid():
            messageboard = form.save()
            return redirect('messageboard', messageboard.id)
    else:
        form = MessageBoardCreateForm()
    return render(request, 'a_messageboard/create_messageboard.html', {'form': form})
@login_required
def messageboard_view(request, id):
    cache_key="chats"
    message_board=cache.get(cache_key)
    if not message_board:
        message_board=get_object_or_404(MessageBoard,id=id)
        cache_key=f"chats{message_board.id}"
        cache.set(cache_key, message_board, timeout=60*10)
    form=MessageCreateForm()
    if request.method=="POST":
        if request.user in message_board.subscribers.all():
            form = MessageCreateForm(request.POST)
            if form.is_valid():
                message=form.save(commit=False)
                message.author=request.user
                message.messageboard=message_board
                message.save()
                send_email(message)
                return redirect('messageboard', id=id)
        else:
            messages.warning(request, "You must be subscribed to message")

    context={'messageboard':message_board, 'form':form}
    return render(request, 'a_messageboard/index.html', context)
# add id here
def messageboard_subscribe(request, id):
    message_board=get_object_or_404(MessageBoard, id=id)
    if request.user not in message_board.subscribers.all():
        message_board.subscribers.add(request.user)
        messages.success(request, "Successfully subscribed")
    else:
         message_board.subscribers.remove(request.user)
         messages.success(request, "Successfully subscribed")

    return redirect('messageboard', id=id)

def send_email_thread(email_subject, email_body,sub):
    email=EmailMessage(email_subject, email_body, to=[sub.email])
    email.send()
def send_email(message):
    """Function to send email with celery"""
    messageboard=message.messageboard   
    subscribers=messageboard.subscribers.all()
     
    for sub in subscribers:
        
        email_subject=f'New Message from {message.author.profile.name}'
        email_body=f'Seems like \n you received a new message from {message.author.profile.name}'
        #send_email_task.delay(email_subject,email_body,sub.email)
        email_thread=threading.Thread(target=send_email_thread, args=(email_subject,email_body,sub))
        email_thread.start()
                
   

'''    
            email_thread=threading.Thread(target=send_email_thread, args=(email_subject,email_body,sub))
            email_thread.start()
                
            except:
                pass   
def send_email_thread(email_subject, email_body,sub):
    email=EmailMessage(email_subject, email_body, to=[sub.email])
    email.send()
 '''

'''
 celery -A a_core worker -P solo for low wor kload
  celery -A a_core worker -P threads multiple tasks sim in sep threads
   celery -A a_core worker -P gevent high number of tasks


sudo service redis-server start

celery -A a_core worker -P threads
celery -A a_core.celery_app flower 
celery -A a_core.celery_app flower --basic_auth=username:password
celery -A a_core beat -l info
celery beat - periodic stuff schedhue
celery -A a_core beat -l info --scheduler django_c
elery_beat.schedulers:Data
baseScheduler
'''


