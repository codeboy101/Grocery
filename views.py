from django.shortcuts import render ,redirect
from .forms import loginForm
from .models import Register

def home(request):
	if request.method == "POST":
		form = loginForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect(greet)
	else:
		form = loginForm()	
	return render(request,'validator/home.html',{'form':form})

def greet(request):
	users = Register.objects.all()
	user_total = len(users)
	return render(request,'validator/greet.html',{'user_total':user_total})
