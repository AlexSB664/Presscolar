from django.shortcuts import render

# Create your views here.
def LogIn(request):    
	return render(request,'log/in.html')
def Index2(request):    
	return render(request,'padres/indexPadres.html')
