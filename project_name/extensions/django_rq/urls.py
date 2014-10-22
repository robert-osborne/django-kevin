from django.conf.urls import url

from .views import jobs, job_detail

# Subclass view functions to make time aware in templates
make_time_aware_urlpatterns = [
    url(r'^admin/rq/queues/(?P<queue_index>[\d]+)/$', jobs, name='rq_jobs'),
    url(r'^admin/rq/queues/(?P<queue_index>[\d]+)/(?P<job_id>[-\w]+)/$', job_detail, name='rq_job_detail'),
]

from .views import queues, clear_queue, delete_job, requeue_job_view, actions

# Added title context variable to templates
add_title_to_template_urlpatterns = [
    url(r'^admin/rq/$', queues, name='rq_home'),
    url(r'^admin/rq/queues/(?P<queue_index>[\d]+)/empty/$', clear_queue, name='rq_clear'),
    url(r'^admin/rq/queues/(?P<queue_index>[\d]+)/(?P<job_id>[-\w]+)/delete/$', delete_job, name='rq_delete_job'),
    url(r'^admin/rq/queues/(?P<queue_index>[\d]+)/(?P<job_id>[-\w]+)/requeue/$', requeue_job_view, name='rq_requeue_job'),
    url(r'^admin/rq/queues/actions/(?P<queue_index>[\d]+)/$', actions, name='rq_actions'),
]
