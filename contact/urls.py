from django.conf import settings
from django.urls import path
from contact.views import contact, search, detail
from contact.views import update, delete, answer_create, answer_delete
from contact.views import upload3, upload4, download
from django.conf.urls.static import static

app_name='contact'

urlpatterns = [
    path('contact/', contact, name="list"),
    path('search/', search, name='search'),
    path('<int:question_id>/', detail, name='detail'),
    path(
        'answer/create/<int:question_id>/', answer_create,
        name='answer_create'),
    path('<int:question_id>/update/', update, name="update"),
    path('<int:question_id>/delete/', delete, name="delete"),
    path('upload3/', upload3, name='upload3'),
    path('upload4/', upload4, name='upload4'),
    path('download/<int:question_id>/', download, name='download'),
    path('<int:answer_id>/answer_delete/', answer_delete, name="answer_delete"),
]+ static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT)