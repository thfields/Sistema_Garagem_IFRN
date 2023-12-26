from django.contrib import admin
from django.urls import path
from todos.views import TodoListView, TodoCreateView, TodoHomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TodoHomeView.as_view(), name='home'),
    path('painel/', TodoListView.as_view(), name='todo_list'),
    path('adicionar/', TodoCreateView.as_view(), name='todo_create'),
]
