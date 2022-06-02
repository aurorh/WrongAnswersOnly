  GNU nano 4.8                                                                                           views.py                                                                                                     
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from bs4 import BeautifulSoup
from PyDictionary import PyDictionary
import requests
import random
import nltk
from nltk.corpus import words
from nltk.probability import FreqDist

diction = PyDictionary()
word_list = words.words('en-basic')


def randomword():
return random.choice(word_list)


def wrongword(request):
if request.method == "POST":
word = request.POST['word']
wurd = randomword()
param = {'word': word, 'text': diction.meaning(wurd)}
return render(request, 'dictionary/index.html', param)
else:
return render(request, 'dictionary/index.html')

"""
def wrongdef():
    wurd = randomword()
    random = diction.meaning(wurd)
    return random
"""
"""
def home(request):
    return render(request, {'wrongdef': wrongdef})

#param = {'word': word, 'text': diction.meaning(wurd)}
#wurd = randomword()
"""