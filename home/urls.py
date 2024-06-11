from django.contrib.auth import views as auth_views 
from django.urls import path
from home.views import *

urlpatterns = [
    path('login/',login_page,name="login_page"),
    path('signup/',signup_page,name="signup_page"),
    path('',signup_page,name="signup_page"),
    path('landpage/',landpage,name="landpage"),
    path('logout/',logout_page,name="logout_page"),
    # Add more URLs as needed
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete')
]
