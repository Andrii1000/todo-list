from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView, UpdateView, CreateView

from tasks.forms import TagForm, TaskForm
from tasks.models import Task, Tag


class IndexListView(ListView):
    model = Task
    template_name = "tasks/index.html"
    context_object_name = "tasks"

    def get_queryset(self):
        return Task.objects.order_by("is_done", "created_at")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("tasks:index")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("tasks:index")


class TagListView(ListView):
    model = Tag
    context_object_name = "tags"


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("tasks:tag-list")


def complete_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = True
    task.save()
    return redirect('tasks:index')


def undo_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_done = False
    task.save()
    return redirect('tasks:index')


