from django.urls import path
from .views import

urlpatterns = [
    path('list/', TodoList.as_view()),
]