from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Module(models.Model):
    module_title = models.CharField('Название модуля', max_length=200)
    eng_tag = models.CharField('Английский тэг', max_length=200)
    
    def __str__(self):
        return self.module_title

    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

class Lesson(models.Model):
    Module = models.ForeignKey(Module, on_delete = models.CASCADE)
    lesson_title = models.CharField('Название урока', max_length=200)
    lesson_text = RichTextUploadingField(config_name = 'special')
    lesson_pub_date = models.DateField('Дата публикации')
    eng_tag = models.CharField('Английский тэг', max_length=200)

    def __str__(self):
        return self.lesson_title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
