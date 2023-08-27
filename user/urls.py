from django.urls import path, include
from user.views import UserInfoView, KakaoLogin, NaverLogin, GoogleLogin

from dj_rest_auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordResetConfirmView,
    PasswordResetView, UserDetailsView,
)

from dj_rest_auth.app_settings import api_settings






urlpatterns = [
    path('login/', LoginView.as_view(), name='rest_login'),
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('info/', UserInfoView.as_view()),
    path('password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('password/reset/', PasswordResetView.as_view(), name='rest_password_reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path('registration/', include('dj_rest_auth.registration.urls')),
    path('social/kakao/', KakaoLogin.as_view(), name='kakao_login'),
    path('social/naver/', NaverLogin.as_view(), name='naver_login'),
    path('social/google/', GoogleLogin.as_view(), name='google_login'),
    ]

if api_settings.USE_JWT:
    from rest_framework_simplejwt.views import TokenVerifyView

    from dj_rest_auth.jwt_auth import get_refresh_view

    urlpatterns += [
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    ]
