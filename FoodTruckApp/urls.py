from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

from django.urls import reverse

app_name = 'FoodTruckApp'
urlpatterns = [
    url(r'^register', views.register, name='register'),
    url(r'^password_change/$', auth_views.PasswordChangeView.as_view(template_name = 'register/password_change_form.html'), name='password_change'),
    url(r'^password_change/done/$', auth_views.PasswordChangeDoneView.as_view(template_name = 'register/password_change_done.html'), name='password_change_done'),
    url(r'^password_reset/$', auth_views.PasswordResetView.as_view(template_name = 'register/password_reset_form.html'), name='password_reset'),
    url(r'^password_reset/done/$', auth_views.PasswordResetDoneView.as_view(template_name = 'register/password_reset_done.html'), name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', auth_views.PasswordResetConfirmView.as_view(template_name = 'register/password_reset_confirm.html'), name='password_reset_confirm'),
    url(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(template_name = 'register/password_reset_complete.html'), name='password_reset_complete'),
    url(r'^index$', views.index, name='index'),
    url(r'^menu$', views.menu, name='menu'),
    url(r'^userProfile$', views.userProfile, name='userProfile'),
    url(r'^ownerProfile$', views.ownerProfile, name='ownerProfile'),

]
