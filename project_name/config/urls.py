from django.conf.urls import patterns, url, include
from django.conf import settings
from django.contrib import admin

from django.views.generic.base import RedirectView, TemplateView

urlpatterns = patterns('',
    # Core URLs
    url(r'^', include('core.urls', namespace='core')),

    # Root-level redirects for common browser requests
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico')),
    url(r'^robots\.txt$', TemplateView.as_view(template_name='robots.txt', content_type='text/plain')),

    # Admin URLs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # Authtools URLs
    # https://github.com/fusionbox/django-authtools/blob/master/authtools/urls.py
    url(r'^', include('authtools.urls', namespace='authtools')),

    # Django Rest Framework URLs
    # http://www.django-rest-framework.org/api-guide/routers
    url(r'^api/', include('api.v1.urls', namespace='api_v1')),
    url(r'^api/v1/', include('api.v1.urls', namespace='api_v1')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

admin.site.site_header = '%s Headquarters' % settings.PROJECT_NAME
admin.site.index_title = 'Base of Operations'

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^404/$', TemplateView.as_view(template_name="404.html")),
        (r'^500/$', TemplateView.as_view(template_name="500.html")),
    )

    import debug_toolbar
    urlpatterns += patterns('', url(r'^__debug__/', include(debug_toolbar.urls)))

    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
