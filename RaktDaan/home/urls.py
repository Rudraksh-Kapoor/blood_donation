from django.urls import path
from home.views import *
urlpatterns = [
    path('',index,name='index'),
    path('register',register,name='register'),
    path('donors_list/<int:myid>/',donors_list,name='donors_list'),
    path('login',Login,name='login'),
    path("logout/",Logout, name="logout"),
    path('donors_details/<int:myid>/',donors_details,name='donors_details'),
    path('request_blood',request_blood,name='request_blood'),
    path("see_all_request",see_all_request, name="see_all_request"),
    path('profile', profile, name='profile'),
    path('edit_profile',edit_profile, name='edit_profile'),
    path('change_status',change_status, name='change_status'),
    path('aboutus',aboutus,name='aboutus'),

]