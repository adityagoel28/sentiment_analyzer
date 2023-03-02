from django.shortcuts import render
from transformers import pipeline

# Create your views here.
def home(request):
    return render(request, 'home.html')

def feedbackk(request):
    field1 = request.POST['field1']
    field2 = request.POST['field2']
    field3 = request.POST['field3']
    field4 = request.POST['field4']
    field5 = request.POST['field5']
    print(field1, field2, field3, field4, field5)
    context = {'hotels': 'aa'}
    return render(request, 'feedback.html', context)