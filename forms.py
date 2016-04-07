from django import forms
from .models import List

items = List.objects.order_by('item_name')
choices = (items)

class addForm(forms.ModelForm):

	class Meta:
		model = List
		fields = ('item_name','item_price',)

class SimpleForm(forms.ModelForm):
	
	class Meta:
		model = List
		fields = ('item_name','item_price')
