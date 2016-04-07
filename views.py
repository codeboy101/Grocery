from django.shortcuts import render , redirect
from .models import List
from .forms import addForm , SimpleForm

def show_list(request):
	items = List.objects.order_by('item_name')
	return render(request,'grocery/items.html',{'items':items})

def addItem(request):
	if request.method == "POST":
		form = addForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.save()
			return redirect('show_list')
	else:
		form = addForm()
	return render(request,'grocery/addItem.html',{'form':form})

def removeItem(request,pk):
	items = List.objects.order_by('item_name')
	my_item = List.objects.get(pk=pk)
	my_item.delete()
	return render(request,'grocery/removeItem.html',{'items':items,})


def removeItemW(request):
	items = List.objects.order_by('item_name')
	return render(request,'grocery/removeItem.html',{'items':items,})
