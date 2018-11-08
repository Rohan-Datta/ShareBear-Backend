from django.urls import path
from UserAPI.views import ListUsersView

urlpatterns = [

    path('users/', ListUsersView.as_view(), name='users-all')

]
