﻿"""
Definition of models.
"""

from django.db import models
from django.contrib import admin
from datetime import datetime
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User




class Blog(models.Model):

  title = models.CharField(max_length = 100, unique_for_date = "posted", verbose_name = "Заголовок")

  description = models.TextField(verbose_name = "Краткое содержание")

  image = models.FileField(default = 'temp.png', verbose_name = "Путь к картинке")

  content = models.TextField(verbose_name = "Полное содержание")

  author = models.ForeignKey(User, null=True, blank=True, on_delete = models.SET_NULL, verbose_name = "Автор")

  posted = models.DateTimeField(default = datetime.now(), db_index = True, verbose_name = "Опубликована")

# Методы класса:

  def __str__(self): # метод возвращает название, используемое для представления отдельных записей в административном разделе

    return self.title

  def get_absolute_url(self): # метод возвращает строку с URL-адресом записи

    return reverse("blogpost", args=[str(self.id)])



# Метаданные – вложенный класс, который задает дополнительные параметры модели:

class Meta:

  db_table = "Posts" # имя таблицы для модели

  ordering = ["-posted"]

  verbose_name = "статья блога" # имя, под которым модель будет отображаться в административном разделе (для одной статьи блога)

  verbose_name_plural = "статьи блога" # тоже для всех статей блога

admin.site.register(Blog)

class Comment(models.Model):
    text = models.TextField(verbose_name = "Комментарий")
    date = models.DateTimeField(default = datetime.now(),db_index = True, verbose_name = "Дата")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name = "Автор")
    post = models.ForeignKey(Blog, on_delete = models.CASCADE, verbose_name = "Статья")

    def __str__(self):
        return 'Комментарий %s к %s' % (self.author, self.post)

    class Meta:
        db_table = "Comments"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии к статьям блога"
        ordering = ["-date"]

admin.site.register(Comment)

