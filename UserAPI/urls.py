from django.urls import path
from UserAPI.views import *

urlpatterns = [

    path('users/', ListUsersView.as_view(), name='users-all')
    path('profiles/', ListProfilesView.as_view(), name='profiles-all')
]
