
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from a_messageboard.views import *

urlpatterns = [
    path('', messageboard_view, name="messageboard"),
    path('subscribe', messageboard_subscribe,name='subscribe' ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
