"""
URL configuration for taskmanager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from base.views import *
from django.contrib.auth.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='base/logout.html', ), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('tasks/', TaskList.as_view(), name='task_list'),
    path('tasks/detail/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('tasks/create/', TaskCreate.as_view(), name='task_create'),
    path('tasks/edit/<int:pk>/', TaskUpdate.as_view(), name='task_edit'),
    path('tasks/delete/<int:pk>/', TaskDelete.as_view(), name='task_delete'),


    path('password_change', PasswordChangeView.as_view(template_name = 'base/password_change_form.html'), name='password_change'),
    path('password_change/done', PasswordChangeDoneView.as_view(template_name = 'base/password_change_done.html'), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(template_name = 'base/password_reset_form.html'), name='password_reset'),
    path('password_reset/done', PasswordResetDoneView.as_view(template_name = 'base/password_reset_done.html'), name='password_reset_done'),
    path('password_reset/confirm/<uidb64>/<token>', PasswordResetConfirmView.as_view(template_name = 'base/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password_reset/complete', PasswordResetCompleteView.as_view(template_name = 'base/password_reset_complete.html'), name='password_reset_complete'),
]
