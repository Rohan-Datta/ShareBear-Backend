from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from UserAPI import views as user_views
#from ItemAPI import views as item_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', user_views.UserList.as_view()),
    re_path('users/(?P<pk>[0-9]+)/', user_views.UserDetail.as_view()),
 #   path('items/', item_views.ItemList.as_view()),
  #  re_path('items/(?P<pk>[0-9]+)/', item_views.ItemDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
