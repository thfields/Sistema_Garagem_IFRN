from django.views.generic import ListView, CreateView, TemplateView, View
from datetime import datetime, time
from django.urls import reverse_lazy
from .models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from math import ceil

relacao = []
#este campo deve ser comentado e descomentado caso queira sertar o banco
# config = Constante(
#      carro = 3,
#      moto = 1,
#      )
# config.save()
# config = Constante(
#      carro = 3,
#      moto = 1,
#      )
# config.save()

class TudoRelacaoView(TemplateView):
    template_name = 'todos/relacao.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['itens_relacao'] = relacao
        return context

class TodoHomeView(TemplateView):
    template_name = 'todos/home.html'

class TodoListView(ListView):
    model = Todo
  
class TodoCreateView(CreateView):
    model = Todo
    fields = ['placa', 'tipo', 'andar']
    success_url = reverse_lazy("todo_list")
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        andar = form.cleaned_data['andar']
        tipo = form.cleaned_data['tipo']
        
        if andar == 'Andar 1':
            andar1 = get_object_or_404(Constante, pk=1)
            if andar1.carro > 0 and tipo == 'Carro':
                instance.save()
                andar1.carro -= 1
                andar1.save()
                relacao.append(instance)
                return super().form_valid(form)
            elif andar1.moto > 0 and tipo == 'Motocicleta':
                instance.save()
                andar1.moto -= 1
                andar1.save()
                relacao.append(instance)
                return super().form_valid(form)
            else:
                form.add_error('andar', 'Este andar já está lotado.')
        
        elif andar == 'Andar 2':
            andar2 = get_object_or_404(Constante, pk=2)
            if andar2.carro > 0 and tipo == 'Carro':
                instance.save()
                andar2.carro -= 1
                andar2.save()
                relacao.append(instance)
                return super().form_valid(form)
            elif andar2.moto > 0 and tipo == 'Motocicleta':
                instance.save()
                andar2.moto -= 1
                andar2.save()
                relacao.append(instance)
                return super().form_valid(form)
            else:
                form.add_error('andar', 'Este andar já está lotado.')
        
        return self.form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        andar1 = get_object_or_404(Constante, pk=1)
        andar2 = get_object_or_404(Constante, pk=2)
        context['vagas_andar1'] = andar1.carro + andar1.moto
        context['vagas_andar2'] = andar2.carro + andar2.moto
        return context

    
    

class UpdateHoraAndarView(View):
    def get(self, request, pk):
        todo_obj = get_object_or_404(Todo, pk=pk)
        
        if todo_obj.andar == 'Andar 1':
            andar1 = get_object_or_404(Constante, pk=1)
            if todo_obj.tipo == 'Carro':
                andar1.carro += 1
                andar1.save()
            elif todo_obj.tipo == 'Motocicleta':
                andar1.moto += 1
                andar1.save()
        elif todo_obj.andar == 'Andar 2':
            andar2 = get_object_or_404(Constante, pk=2)
            if todo_obj.tipo == 'Carro':
                andar2.carro += 1
                andar2.save()
            elif todo_obj.tipo == 'Motocicleta':
                andar2.moto += 1
                andar2.save()
        
        todo_obj.hora_saida = datetime.now().time()
        todo_obj.andar = ''
        todo_obj.save()

        horario2 = todo_obj.hora_saida
        horario1 = todo_obj.hora_entrada
        diferenca_em_horas = (horario2.hour - horario1.hour) + (horario2.minute - horario1.minute) / 60 + (horario2.second - horario1.second) / 3600
        if todo_obj.tipo == 'Carro':
            todo_obj.valor = 10 + (ceil(diferenca_em_horas) - 1) * 5
        else:
            todo_obj.valor = 5 + (ceil(diferenca_em_horas) - 1) * 2
        todo_obj.save()
        relacao.append(todo_obj)
        return HttpResponseRedirect(reverse_lazy('todo_list'))
