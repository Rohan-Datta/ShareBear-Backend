from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from UserAPI import views as user_views
from EntryAPI import views as entry_views

urlpatterns = [
    #admin/	
    path('admin/', admin.site.urls),
    
    #users/
    path('users/', user_views.UserList.as_view()),
    
    #user/1/
    re_path('users/(?P<pk>[0-9]+)/', user_views.UserDetail.as_view()),
    
    #entries/
    path('entries/', entry_views.EntryList.as_view()),
    
    #entries/1/
    re_path('entries/(?P<pk>[0-9]+)/', entry_views.EntryDetail.as_view()),
    
    #profiles/
    path('profiles/', user_views.ProfileList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
