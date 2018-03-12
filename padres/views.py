from django.shortcuts import render

# Create your views here.
def Index2(request):
	return render(request,'padres/indexPadres.html')