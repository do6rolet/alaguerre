from django.conf import settings  # allow to get some settings (for media files)
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views
from apps.core.views import frontpage, signup
from apps.inside.views import inside, search
from apps.inside.api import *
from apps.userprofile.views import *
from apps.conversation.views import *
from apps.conversation.api import api_add_message

urlpatterns = [
  path('', frontpage, name='frontpage'),
  path('signup/', signup, name='signup'),
  path('logout/', views.LogoutView.as_view(), name='logout'),
  path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),

  path('inside/', inside, name='inside'),
  path('search/', search, name='search'),
  path('edit_profile/', edit_profile, name='edit_profile'),
  path('conversations/', conversations, name='conversations'),
  path('conversations/<int:user_id>/', conversation, name='conversation'),
  path('u/<str:username>/', userprofile, name='userprofile'),
  path('u/<str:username>/follow', follow_reporter, name='follow_reporter'),
  path('u/<str:username>/unfollow', unfollow_reporter, name='unfollow_reporter'),
  path('u/<str:username>/followers', followers, name='followers'),
  path('u/<str:username>/follows', follows, name='follows'),

  # API

  path('api/add_report/', api_add_report, name='api_add_report'),
  path('api/add_like/', api_add_like, name='api_add_like'),
  path('api/add_message/', api_add_message, name='api_add_message'),
] + static(settings.MEDIA_URL,
         document_root=settings.MEDIA_ROOT)  # help to find media files in development
