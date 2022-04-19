from urllib.parse import urlparse
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'member'

urlpatterns = [
  path('login/', views.login_view, name="login"),
  path('logout/', views.logout_view, name="logout"),
  path('signup/', views.signup, name='signup'),
]
