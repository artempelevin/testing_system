from django.urls import path

from users.views import SignUp, SignIn, SignOut

urlpatterns = [
    path('signin', SignIn.as_view(), name='signin'),
    path('signout', SignOut.as_view(), name='signout'),
    path('signup', SignUp.as_view(), name='signup')
]
