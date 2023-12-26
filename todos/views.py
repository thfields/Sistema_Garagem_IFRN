from django.views.generic import ListView, CreateView, TemplateView

from django.urls import reverse_lazy
from .models import Todo
# Create your views here.

class TodoHomeView(TemplateView):
  template_name = 'todos/home.html'

class TodoListView(ListView):
  model = Todo
  
class TodoCreateView(CreateView):
  model = Todo
  fields = ['placa','tipo']
  success_url = reverse_lazy("todo_list")