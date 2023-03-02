from django.shortcuts import render
from transformers import pipeline

nlp = pipeline(task='sentiment-analysis', model='nlptown/bert-base-multilingual-uncased-sentiment')

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

    def analyse(text):
        result = nlp(text)

        sent = ''
        if (result[0]['label'] == '1 star'):
            sent = 'very negative'
        elif (result[0]['label'] == '2 star'):
            sent = 'negative'
        elif (result[0]['label'] == '3 stars'):
            sent = 'neutral'
        elif (result[0]['label'] == '4 stars'):
            sent = 'positive'
        else:
            sent = 'very positive'

        prob = result[0]['score']

        # Format and return results
        a =  {'sentiment': sent, 'probability': prob}

        return {'sentiment': a}
    
    a = analyse(field1)
    print(a)
    context =  {'sentiment': a}
    return render(request, 'feedback.html', context)