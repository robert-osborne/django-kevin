from django.conf.urls import patterns, url

# Authtool Extensions
authtools_url_patterns = patterns(
    'extensions.views.authtools',
    url(r'^logout/$', 'logout', name='logout'),
    url(r'^password_reset/$', 'password_reset', name='password_reset'),
    url(r'^password_change/$', 'password_change', name='password_change'),
)

urlpatterns = authtools_url_patterns
