from django.conf import settings
from django.urls import path
from contact.views import contact
from django.conf.urls.static import static

app_name='contact'

urlpatterns = [
    path('contact/', contact, name="list"),
]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)