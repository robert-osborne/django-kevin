from .authtools import urls as authtools_urls
from .django_rq import urls as django_rq_urls

urlpatterns = []
urlpatterns += authtools_urls.subclass_urlpatterns
urlpatterns += django_rq_urls.make_time_aware_urlpatterns
urlpatterns += django_rq_urls.add_title_to_template_urlpatterns
