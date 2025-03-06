from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
import threading
from .tasks import *
from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
@login_required
def messageboard_view(request):
    message_board=get_object_or_404(MessageBoard, id=8)
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
                return redirect('messageboard')
        else:
            messages.warning(request, "You must be subscribed to message")

    context={'messageboard':message_board, 'form':form}
    return render(request, 'a_messageboard/index.html', context)

def messageboard_subscribe(request):
    message_board=get_object_or_404(MessageBoard, id=8)
    if request.user not in message_board.subscribers.all():
        message_board.subscribers.add(request.user)
        messages.success(request, "Successfully subscribed")
    else:
         message_board.subscribers.remove(request.user)
         messages.success(request, "Successfully subscribed")

    return redirect('messageboard')


def send_email(message):
    """Function to send email with celery"""
    messageboard=message.messageboard   
    subscribers=messageboard.subscribers.all()
     
    for sub in subscribers:
        
        email_subject=f'New Message from {message.author.profile.name}'
        email_body=f'Seems like \n you received a new message from {message.author.profile.name}'
        send_email_task.delay(email_subject,email_body,sub.email)

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
