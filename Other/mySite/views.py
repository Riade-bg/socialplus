from django.shortcuts import render, get_object_or_404, reverse
from django.template import loader
from django.views import generic
from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choise
# Create your views here.

class index(generic.ListView):
    template_name = "mySite/index.html"
    context_object_name = "latest_question_text"

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]
    
    # latest_question_text = Question.objects.order_by('-pub_date')[:5]
    # contex = {
    #     'latest_question_text':latest_question_text,
    # }
    # return render(request, "mySite/index.html", contex)

class detail(generic.DetailView):
    model = Question
    template_name = 'mySite/detail.html'
    context_object_name = "obj"
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())

# def detail(request, question_id):
#     obj = get_object_or_404(Question, pk=question_id)
#     contex = {
#         'obj':obj,
#     }
#     return render(request, "mySite/detail.html", contex)


class result(generic.DetailView):
    model = Question
    template_name = 'mySite/result.html'

# def result(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'mySite/result.html', {'question':question})

def vote(request, question_id):
    obj = get_object_or_404(Question, pk=question_id)
    try:
        selected_choise = obj.choise_set.get(pk=request.POST['choise'])
    except (KeyError, Choise.DoesNotExist):
        return render(request, 'mySite/detail.html', {
            'obj':obj, 
            'error_message':"You hven't select a choise"
        })        
    else:
        selected_choise.votes += 1
        selected_choise.save()
        return HttpResponseRedirect(reverse('mySite:result', args=(obj.id,)))

