from django.urls import path

from tasks.views import (
    IndexListView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    undo_task,
    complete_task
)

urlpatterns = [
    path("", IndexListView.as_view(), name="index"),
    path("task/create", TaskCreateView.as_view(), name="task_create"),
    path("task/<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("task/<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
    path("undo_task/<int:pk>/", undo_task, name="undo_task"),
    path("complete_task/<int:pk>/", complete_task, name="complete_task"),
]

app_name = "tasks"
