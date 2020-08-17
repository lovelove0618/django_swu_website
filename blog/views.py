from django.shortcuts import render, redirect

from django.views import generic

class Blog(generic.TemplateView):
    def get(self, request, *args, **kwargs):
        template_name = 'blog/index.html'
        return render(request, template_name)