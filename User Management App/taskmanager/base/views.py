from typing import Any
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Task
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy

# Create your views here.
class CustomLoginView(LoginView):
    model = User
    fields = '__all__'
    template_name = 'base/login.html'
    redirect_authenticated_user = True

    def get_success_url(self) -> str:
        return reverse_lazy('task_list')


# class CustomLogoutView(LoginRequiredMixin, LogoutView):
#     template_name = 'base/logout.html'
#     def get_success_url(self):
#         return reverse_lazy('login')
    

class RegisterPage(FormView):
    form_class = UserCreationForm
    template_name = 'base/register.html'
    success_url = reverse_lazy('task_list')
    redirect_authenticated_user = True

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'base/task_list.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False)

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__icontains= search_input)
        context['search_input'] = search_input

        return context


class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'base/task_detail.html'
    context_object_name = 'task'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'desc', 'complete']
    template_name = 'base/task_create.html'
    success_url = reverse_lazy('task_list')

    def form_valid(self, form: BaseModelForm):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    template_name = 'base/task_update.html'
    success_url = reverse_lazy('task_list')


class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'base/task_delete.html'
    success_url = reverse_lazy('task_list')