from django.shortcuts import render
from django.template import loader

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, FileResponse
from .models import Question, Answer
from django.utils import timezone
from django.core.paginator import Paginator
from django.views.generic.detail import SingleObjectMixin
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required #로그인여부

def index(request):
	return render(request, 'main/index.html')

def about(request):
	return render(request, 'main/about.html')

def contact(request):
    now_page = request.GET.get('page', 1)
    question_list = Question.objects.order_by('-pub_date')
    p = Paginator(question_list, 10)
    info = p.get_page(now_page)
    start_page = (int(now_page) - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages

    context = {'info': info,
        'page_range' : range(start_page, end_page + 1)
    }
    return render(request, 'main/contact.html', context)