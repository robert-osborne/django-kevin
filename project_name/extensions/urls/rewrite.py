from django.conf.urls import patterns, url

# Authtool Extensions
authtools_url_patterns = patterns('authtools.views',
    url(r'^password_reset/complete/$', 'password_reset_complete', name='password_reset_complete'),
    url(r'^password_reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'password_reset_confirm', name='password_reset_confirm'),
    url(r'^password_reset/(?P<uidb36>[0-9A-Za-z]{1,13})-(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        'password_reset_confirm_uidb36', name='password_reset_confirm_uidb36'),
)

urlpatterns = authtools_url_patterns
