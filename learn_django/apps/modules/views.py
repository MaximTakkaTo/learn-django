from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Module

def modules(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('registration:signin'))
    else:   
        modules = Module.objects.order_by('module_id')
        lessons = []
        for m in modules:
            lessons.append(m.lesson_set.order_by('lesson_id'))
        return render(request, 'modules/list.html', {'modules': modules, 'lessons' : lessons})


def detail(request, module_eng_tag, lesson_eng_tag):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('registration:signin'))
    else:
        try:
            m = Module.objects.get(eng_tag = module_eng_tag)
        except:
            raise Http404("Извините, урок не существует.")

        lesson = m.lesson_set.get(eng_tag = lesson_eng_tag)
        return render(request, 'modules/detail.html', {'lesson': lesson})

def about(request):
    return render(request, 'modules/about.html')