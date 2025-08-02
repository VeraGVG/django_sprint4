from django.contrib.auth.forms import UserCreationForm

from django.views.generic import CreateView

from django.views.generic import DetailView

from django.contrib.auth.models import User

from django.views.generic import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import UserUpdateForm

from django.urls import reverse_lazy

from blog.models import Post


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('login')


class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['posts'] = Post.objects.filter(author=user)
        return context


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    template_name = 'users/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user
