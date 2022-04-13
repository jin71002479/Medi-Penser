
from django.conf import settings
from django.urls import path
from cam.views import camera_1,video,index
from django.conf.urls.static import static

app_name='cam'

urlpatterns = [
    path('video_1/', video, name="video"),
    path('show/',camera_1,name='show'),
    path('index/',index,name='index')
]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
