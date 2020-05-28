from django.shortcuts import render, redirect
from .forms import SurveyForm
from .models import Delve_form

# Create your views here.
def survey_list(request):
    context = {'survey_list':Delve_form.objects.all()}
    return render(request,"survey_register/survey_list.html", context)

def survey_form(request, id=0):
    if request.method == 'GET':
        if id==0:
            form = SurveyForm()
        else:
            delve = Delve_form.objects.get(pk=id)
            form = SurveyForm(instance=delve)
       
        return render(request,"survey_register/survey_form.html", {'form': form})
    else:
        if id == 0:
            form = SurveyForm(request.POST)
        else:
            delve = Delve_form.objects.get(pk=id)
            form = SurveyForm(request.POST, instance=delve)
        if form.is_valid():
            form.save()
        return redirect('/survey/list')
            
def survey_delete(request, id=0):
    delve = Delve_form.objects.get(pk=id)
    delve.delete()
    return redirect('/survey/list')