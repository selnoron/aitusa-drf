from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import (
    MainView,
    TaskView,
    OneTaskView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
)



urlpatterns = [
    path('', MainView.as_view()),
    path('tasks/all/', TaskView.as_view()),
    path('tasks/get/<int:pk>/', OneTaskView.as_view()),
    path('tasks/create/', TaskCreateView.as_view()),
    path('tasks/update/<int:pk>/', TaskUpdateView.as_view()),
    path('tasks/delete/<int:pk>/', TaskDeleteView.as_view())
]

urlpatterns += static(
    settings.STATIC_URL,
    document_root=settings.STATIC_ROOT
)
urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)