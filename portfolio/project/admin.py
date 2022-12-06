from django.contrib import admin
from .models import Project # из этой же директории
# из файла models.py импортируем таблицу Project

admin.site.register(Project) # зарегистрировали таблицу
# для панели администратора
