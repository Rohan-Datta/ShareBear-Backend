from django.urls import path

urlpatterns = [
    #entries/
    path('entries/', views.EntryList.as_view()),
    #entries/1/
    re_path('entries/(?P<pk>[0-9]+)/', views.EntryDetail.as_view()),
    
]