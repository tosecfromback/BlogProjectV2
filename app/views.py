from django.shortcuts import render, redirect
from django.views import View
from django.urls import reverse_lazy, reverse

class IndexMain(View):
    def get(self, request):
        context = {
            'title' : '시작페이지'
        }
        return render(request, 'index.html', context)