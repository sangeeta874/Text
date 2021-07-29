#views.py created
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    
    return render(request,'index2.html')
    #return HttpResponse('''<h1>hello</h1> <a href = "https://www.youtube.com/">Youtube</a>''')
def analyze(request):
    djtext = request.POST.get('text', 'default')  
    removepunc=request.POST.get('removepunc','off')
    cap = request.POST.get('cap','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    charcount=request.POST.get('charcount','off')
    print(djtext)  
    
    ana_text= djtext
    if removepunc == "on":
        ana_text1=" "
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                ana_text1 += char
        ana_text=ana_text1        
           
    if cap == "on":
        ana_text = ana_text.upper()  
        
        
    if newlineremover == "on":
        ana_text1=" "
        for char in ana_text:  
            if char != "\n" and char != "\r":
                ana_text1 +=char
        ana_text=ana_text1        
        
        
    if spaceremover == "on":
        ana_text1=" "
        length=len(ana_text)
        for i in  range (length-1):  
            if not (ana_text[i]==" " and ana_text[i+1]==" " ):
                ana_text1+= ana_text[i]                                       
        ana_text=ana_text1        
        
         
    if charcount == "on":
        count=0
        length=len(djtext)
        for char in djtext:  
            if char != " " :
                count+=1        
        params={'purpose':'Character Count :','ana':ana_text,'count':count}
        return render(request,'analyze2.html',params)     
    
    
    params={'ana':ana_text}
    return render(request,'analyze2.html',params)       
    
    