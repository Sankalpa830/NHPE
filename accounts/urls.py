from django.urls import path
from accounts.views import SignUp, Login, Logout, Purchased_View, Profile_View, EditProfile_View

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', Logout, name='logout'),
    path('purchase',  Purchased_View.as_view(), name='purchase'),
    path('profile', Profile_View.as_view(), name = 'profile'),
    path('editprofile',EditProfile_View.as_view(), name = 'edit')
]
