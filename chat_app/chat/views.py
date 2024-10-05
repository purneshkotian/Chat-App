# chat/views.py

from django.shortcuts import render

def room(request, room_name):
    return render(request, 'chat/chat_room.html', {
        'room_name': room_name
    })
