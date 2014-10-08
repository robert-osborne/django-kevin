# Subclassing Authtools views
# https://github.com/fusionbox/django-authtools/blob/master/authtools/views.py

from __future__ import absolute_import

from authtools.views import LogoutView, PasswordResetView, PasswordChangeView


class ExtLogoutView(LogoutView):
    template_name = 'registration/logout.html'

logout = ExtLogoutView.as_view()


class ExtPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'

password_reset = ExtPasswordResetView.as_view()


class ExtPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change.html'

    def get_success_url(self):
        from django.contrib.auth import update_session_auth_hash
        # https://docs.djangoproject.com/en/1.7/topics/auth/default/#session-invalidation-on-password-change

        update_session_auth_hash(self.request, self.request.user)
        return super(ExtPasswordChangeView, self).get_success_url()

password_change = ExtPasswordChangeView.as_view()
