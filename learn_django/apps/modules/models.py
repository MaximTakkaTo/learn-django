from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.core.exceptions import ValidationError

class Module(models.Model):
    module_id = models.PositiveIntegerField(default = 0, editable = True)
    module_title = models.CharField('Название модуля', max_length=200)
    eng_tag = models.CharField('Английский тег', max_length=200)
    
    def __str__(self):
        return self.module_title

    def clean(self):
        modules = Module.objects.filter(eng_tag=self.eng_tag)
        tp = False
        for m in modules:
            if m != self:
                tp = True

        modules = Module.objects.filter(module_title=self.module_title)
        tip = False
        for m in modules:
            if m != self:
                tip = True

        modules = Module.objects.filter(module_id=self.module_id)
        ip = False
        for m in modules:
            if m != self:
                ip = True

        if tp:
            raise ValidationError('Модуль с таким тегом уже существует')
        if tip:
            raise ValidationError('Модуль с таким названием уже существует')
        if ip:
            for m in Module.objects.all():
                if m != self and m.module_id >= self.module_id:
                    m.module_id += 1
                    m.save()
    class Meta:
        verbose_name = 'Модуль'
        verbose_name_plural = 'Модули'

class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete = models.CASCADE)
    lesson_id = models.PositiveIntegerField(default = 0, editable = True)
    lesson_title = models.CharField('Название урока', max_length=200)
    lesson_text = RichTextUploadingField(config_name = 'special')
    lesson_pub_date = models.DateField('Дата публикации')
    eng_tag = models.CharField('Английский тег', max_length=200)

    def clean(self): 
        less = Lesson.objects.filter(eng_tag__iexact=self.eng_tag, module=self.module)
        tp = False
        for l in less:
            if l != self:
                tp = True

        less = Lesson.objects.filter(lesson_title__iexact=self.lesson_title, module=self.module)
        tip = False
        for l in less:
            if l != self:
                tip = True

        less = Lesson.objects.filter(lesson_id__iexact=self.lesson_id, module=self.module)
        ip = False
        for l in less:
            if l != self:
                ip = True

        if tp:
            raise ValidationError('Урок с таким тегом уже существует')
        if tip:
            raise ValidationError('Урок с таким названием уже существует')
        if ip:
            for l in Lesson.objects.all():
                if l != self and l.lesson_id >= self.lesson_id and l.module == self.module:
                    l.lesson_id += 1
                    l.save()
    
    def __str__(self):
        return self.module.module_title + '.' +self.lesson_title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
        ordering = ('-module',)