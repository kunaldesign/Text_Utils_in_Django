# i have create this file - Kunal Hedaoo

from os import read, remove
from typing_extensions import ParamSpec
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
    


def ex1(request):
    s=''' Navigation Bar <br> </h2>
    <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> News </a> <br>
    <a href="https://www.google.com/"> Google </a> <br>'''
    return HttpResponse(s)

def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover','off')
    
    #Check which checkbox is on
    #analyze the text
    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        djtext = analyzed
        
    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'analyzed_text': analyzed}
        djtext = analyzed
        
    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
            else:
                print("no")
            print("pre",analyzed)
        params = {'analyzed_text': analyzed}
        djtext = analyzed
        
    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1]==" ":
                pass
            else:
                analyzed = analyzed + char
        params = {'analyzed_text': analyzed}
        
    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and extraspaceremover!="on"):
        return HttpResponse("please select any operation and try Again..!")
    return render(request, 'analyze.html', params)
