from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

def index(request):
return render(request, 'calculator/index.html')

def wrongcalc(request):
if request.method == "POST":
num = request.POST['num']
param = {'num': num, 'text': '6'}
return render(request, 'calculator/index.html', param)
else:
return render(request, 'calculator/index.html')


 # if request.method == "POST":
 #     word = request.POST['word']
 #     wurd = randomword()
 #     param = {'word': word, 'text': diction.meaning(wurd)}
 #     return render(request, 'index.html', param)
 # else:
 #     return render(request, 'index.html')


