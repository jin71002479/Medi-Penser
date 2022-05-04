
from django.conf import settings
from django.urls import path
from cam.views import camera_1,md,cap,Register,operation
from django.conf.urls.static import static


app_name='cam'

urlpatterns = [
    path('show/',camera_1,name='show'),
    path('cap/',cap,name='cap'),
    path('input/',Register,name='Register'),
    path('mod/',md,name='mod'),
    path('operation/',operation,name='operation'),
]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)
