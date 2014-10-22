from django.conf.urls import url

from .views import logout, password_reset, password_change

# Subclassed view functions
subclass_urlpatterns = [
    url(r'^logout/$', logout, name='logout'),
    url(r'^password_reset/$', password_reset, name='password_reset'),
    url(r'^password_change/$', password_change, name='password_change'),
]

from authtools.views import password_reset_complete, password_reset_confirm, password_reset_confirm_uidb36

# Rewritten URL pattern syntax
rewrite_urlpatterns = [
    url(r'^password_reset/complete/$', password_reset_complete, name='password_reset_complete'),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm, name='password_reset_confirm'),
    url(r'^password_reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        password_reset_confirm_uidb36, name='password_reset_confirm_uidb36'),
]
