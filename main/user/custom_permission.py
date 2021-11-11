from django.contrib.auth.mixins import AccessMixin
from django.http import JsonResponse


class AdminRequiredJsonMixin(AccessMixin):
    """Verify that the current user is Admin"""
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return JsonResponse({'error':['user has no permission']})
        return super().dispatch(request, *args, **kwargs)