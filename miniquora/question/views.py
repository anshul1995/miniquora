from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import SuspiciousOperation
from django.views.decorators.http import require_http_methods, require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from .models import Question, Answer, Topic
from .forms import QuestionCreateForm

# Create your views here.
@login_required
@require_http_methods(['GET', 'POST'])
def create_question(request):
    if request.method == 'GET':
        f = QuestionCreateForm()
    else:
        f = QuestionCreateForm(request.POST)
        if f.is_valid():
            q = f.save(commit = False)
            q.by = request.user
            q.save()
            f.save_m2m()
            return redirect('myquestions')
    return render(request, 'questions/create.html', { 'form' : f})

@login_required
@require_GET
def myquestions(request, page_num = 1):
    questions = Question.objects.filter(by = request.user).order_by('-created_at')
    p = Paginator(questions, 1)
    current_page = p.page(page_num)
    return render(request, 'questions/myquestions.html', { 'questions' : current_page.object_list, 'page':current_page})

            

