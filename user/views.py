from django.shortcuts import render, HttpResponseRedirect
from .models import User
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy
from product.models import Basket
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, UpdateView


class UserRegistrationView(CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')


class UserProfileView(UpdateView):
    model = User
    template_name = 'user/profile.html'
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.request.user.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForm()
    context = {
        'form': form
    }
    return render(request, 'user/login.html', context=context)


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Поздравляю')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'user/register.html', context=context)


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)
    context = {'form': form,
               'baskets': Basket.objects.filter(user=request.user),
               }
    return render(request, 'user/profile.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
