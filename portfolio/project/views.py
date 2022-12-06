from django.shortcuts import render
from .models import Project

def project_index(request):
    projects = Project.objects.all() # .all() - запрос все записи
    # переменная содержит все записи в таблище Project
    # которые мы создаем через панель администратора
    context = {'projects': projects}
    return render(request, 'project_index.html', context)

def project_detail(request, primary_key): # primary_key первичный ключ
    project = Project.objects.get(pk = primary_key)
    context = {'project': project}
    return render(request, 'project_detail.html', context)