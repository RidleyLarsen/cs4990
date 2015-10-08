from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class LoginRequiredMixin(object):
    '''
        This mixin will assure clients are logged in and redirect them
        to the login page if they are not or if their session is
        expired.
    '''
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(
            request,
            *args,
            **kwargs
        )
