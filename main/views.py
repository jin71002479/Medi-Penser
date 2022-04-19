from django.shortcuts import render
from django.template import loader

def index(request):
	return render(request, 'main/index.html')

def about(request):
<<<<<<< HEAD
	return render(request, 'main/about.html')
=======
	return render(request, 'main/about.html')

>>>>>>> main
