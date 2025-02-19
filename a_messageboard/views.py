from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
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

