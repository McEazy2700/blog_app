from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='sign-up'),
    path('login/', views.SignInView.as_view(), name='sign-in'),
]
