
from django.conf import settings
from django.urls import path
from main.views import index,about,chatanswer
from django.conf.urls.static import static

app_name='main'

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('chatanswer/', chatanswer, name="chatanswer")
]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
