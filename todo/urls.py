from django.urls import path
from .views import (
    TaskListView, TaskCreateView, TaskUpdateView, toggle_task_status,
    TagListView, TagCreateView, TagUpdateView, TagDeleteView, TaskDeleteView
)

urlpatterns = [
    # Task URLs
    path('', TaskListView.as_view(), name='home'),
    path('task/add/', TaskCreateView.as_view(), name='add_task'),
    path('task/edit/<int:pk>/', TaskUpdateView.as_view(), name='edit_task'),
    path('task/toggle/<int:pk>/', toggle_task_status, name='toggle_task'),

    # Tag URLs
    path('tags/', TagListView.as_view(), name='tag_list'),
    path('tag/add/', TagCreateView.as_view(), name='add_tag'),
    path('tag/edit/<int:pk>/', TagUpdateView.as_view(), name='edit_tag'),
    path('tag/delete/<int:pk>/', TagDeleteView.as_view(), name='delete_tag'),
    path('task/delete/<int:pk>/', TaskDeleteView.as_view(), name='delete_task'),
]