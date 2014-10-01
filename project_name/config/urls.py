from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin

from django.views.generic.base import RedirectView, TemplateView

urlpatterns = patterns('',
    # Core URLs
    url(r'^', include('core.urls', namespace='core')),

    # Extension URLs that subclass views from third-party libraries
    url(r'^', include('extensions.urls.subclass')),

    # Root-level redirects for common browser requests
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'img/compressed/favicon.ico'), name='favicon.ico'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain'), name='robots.txt'),

    # Admin URLs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Authtools URLs
    # https://github.com/fusionbox/django-authtools/blob/master/authtools/urls.py
    url(r'^', include('authtools.urls')),

    # Extension URLs that rewrite the URL from third-party libraries
    # Belongs at the bottom of the URLconf
    url(r'^', include('extensions.urls.rewrite')),
)

admin.site.site_header = '%s Headquarters' % settings.PROJECT_NAME
admin.site.index_title = 'Base of Operations'

if settings.DEBUG:
    urlpatterns += patterns('',
        # Testing 404 and 500 error pages
        url(r'^404/$', TemplateView.as_view(template_name='404.html'), name='404'),
        url(r'^500/$', TemplateView.as_view(template_name='500.html'), name='500'),
    )

    import debug_toolbar
    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)))

    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
