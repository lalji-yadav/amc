from django.urls import path, include
from . import views as viewsone
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('', viewsone.loginPage,name='login'),
    path('login/', viewsone.loginPage, name='login'),
    path('register/', viewsone.register, name='register'),
    path('auth/', viewsone.authBase),

    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

    path('password_reset/',auth_views.PasswordResetView.as_view(
         template_name='ResetPassword/password_reset_form.html')
         ,name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(
         template_name='ResetPassword/password_reset_done.html'),
         name='password_reset_done'),

    path('reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
          template_name='ResetPassword/password_reset_confirm.html'),
         name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='ResetPassword/password_reset_complete.html'),
         name='password_reset_complete'),
]
