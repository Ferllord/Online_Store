from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect
from .models import User, EmailVerification
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from product.models import Basket
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from common.views import TitleMixin


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Поздравляю'


class UserProfileView(UpdateView):
    model = User
    template_name = 'user/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))


class UserLoginView(LoginView):
    template_name = 'user/login.html'
    form_class = UserLoginForm


class EmailVerificationView(TitleMixin, TemplateView):
    template_name = 'user/email.html'
    title = 'Email Verification'

    def get(self, request, *args, **kwargs):
        template = super(EmailVerificationView, self).get(request, *args, **kwargs)
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email = EmailVerification.objects.filter(user=user, code=code)
        if email.exists() and not email.first().is_expired():
            user.is_verified_email = True
            user.save()
            return template
        else:
            return HttpResponseRedirect(reverse('index'))

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             user = auth.authenticate(username=username, password=password)
#             if user:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'user/login.html', context=context)
#
#
# def register(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Поздравляю')
#             return HttpResponseRedirect(reverse('users:login'))
#     else:
#         form = UserRegistrationForm()
#     context = {
#         'form': form
#     }
#     return render(request, 'user/register.html', context=context)
#
#
# @login_required
# def profile(request):
#     if request.method == 'POST':
#         form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('users:profile'))
#     else:
#         form = UserProfileForm(instance=request.user)
#     context = {'form': form,
#                'baskets': Basket.objects.filter(user=request.user),
#                }
#     return render(request, 'user/profile.html', context=context)
#
#
# def logout(request):
#     auth.logout(request)
#     return HttpResponseRedirect(reverse('index'))
