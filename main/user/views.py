import urllib
import json
from .forms import  UserForm, SignUpForm
from .models import User
from user.custom_permission import AdminRequiredJsonMixin

from django.views import View
from django.contrib.auth.views import LoginView
from django.http import JsonResponse
from django.views.generic.edit import FormView, CreateView


class CustomLoginView(LoginView):
    template_name = "user/login.html"
    redirect_authenticated_user = True


class UserView(AdminRequiredJsonMixin, View):
    def post(self, request, id, *args, **kwargs):
        try:
            user_instance = User.objects.get(id=id)
            form = UserForm(request.POST, instance=user_instance)
            if form.is_valid():
                form.save()
                return JsonResponse({"message": ["success"]})
            return JsonResponse(form.errors, status=400)
        except Exception as e:
            return JsonResponse({"error": [e.__str__()]}, status=400)


class SignUpView(FormView, CreateView):
    form_class = SignUpForm
    template_name = "user/signup.html"
    success_url = "/home"
