from django.urls import path, include
from django.conf.urls import url
from .views import ( PasswordChangeView,PasswordResetView,PasswordResetConfirmView)

urlpatterns = [
                url(r'^reset/$', PasswordResetView.as_view(),name='password_reset'),
                url(r'^reset/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
                url(r'^change/$', PasswordChangeView.as_view(),name='password_change'),
               ]