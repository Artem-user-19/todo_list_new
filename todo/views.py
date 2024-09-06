from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from .models import Task, Tag
from .forms import TaskForm, TagForm


class TaskListView(ListView):
    model = Task
    template_name = 'templates/home.html'
    context_object_name = 'tasks'
    ordering = ['is_done', '-created_at']


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'templates/task_form.html'
    success_url = reverse_lazy('home')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ['content', 'deadline', 'is_done', 'tags']
    template_name = 'templates/task_form.html'
    success_url = reverse_lazy('home')


class ToggleTaskStatusView(View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        task.is_done = not task.is_done
        task.save()
        return redirect(reverse_lazy('home'))

    def get(self, request, pk):
        return self.post(request, pk)


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'templates/task_confirm_delete.html'
    success_url = reverse_lazy('home')


class TagListView(ListView):
    model = Tag
    template_name = 'templates/tag_list.html'
    context_object_name = 'tags'


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    template_name = 'templates/tag_form.html'
    success_url = reverse_lazy('tag_list')


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    template_name = 'templates/tag_form.html'
    success_url = reverse_lazy('tag_list')


class TagDeleteView(DeleteView):
    model = Tag
    template_name = 'templates/tag_confirm_delete.html'
    success_url = reverse_lazy('tag_list')


