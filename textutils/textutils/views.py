from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def about(request):
    return render(request, 'about.html')


def analyze(request):
    # getting the text and the putting it in a variable

    newtext = (request.GET.get('text', 'default'))
    removepunc = request.GET.get('removepunc', 'off')
    capitalise = request.GET.get('capitalise', 'off')
    nlr = request.GET.get('newlineremover', 'off')


    print(removepunc)  # true/false
    print(newtext)
    print (capitalise)
    print (nlr)

    puncs = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''

    if removepunc == 'on':
        analyzed = ""
        for char in newtext:
            if char not in puncs:
                analyzed += char

    if nlr == 'on':
        analyzed =""
        for char in newtext:
            if char != '\n':
                analyzed += char

    if capitalise == 'on':
        analyzed = ""
        for char in newtext:
            if char in newtext:
                analyzed += char.upper()


        
        
    params = {'purpose': 'is analyzed and modified as per requested', 'analyzed_text': analyzed}
    
    return render(request, 'analyze.html', params)
    



     
    
    