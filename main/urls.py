
from django.conf import settings
from django.urls import path
from main.views import index,about,contact
from django.conf.urls.static import static

app_name='main'

urlpatterns = [
    path('',index,name='index'),
    path('about/',about,name='about'),
    path('contact/',contact,name='contact'),
]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
