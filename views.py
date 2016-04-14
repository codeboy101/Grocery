from django.shortcuts import render ,redirect
from .forms import loginForm
from .models import Register

def home(request):
	if request.method == "POST":
		form = loginForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("greet")
	else:
		form = loginForm()	
	return render(request,'validator/home.html',{'form':form})

def greet(request,pk):
	user = Register.objects.get(pk=pk)
	return render(request,'validator/greet.html',{'user':user})
