
from django.conf import settings
from django.urls import path
from cam.views import camera_1,video
from django.conf.urls.static import static

app_name='cam'

urlpatterns = [
    path('video_1/', video, name="video"),
    path('show/',camera_1,name='show'),
]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
