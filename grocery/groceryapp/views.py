from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from . models import Grocery
from .forms import GroceryForm
# Create your views here.
def display(request):
    obj = Grocery.objects.all()
    return render(request, 'display.html', context={'obj': obj})
def insert_form(request):
    if request.method=='POST':
       form = GroceryForm(request.POST)
       if form.is_valid():
          data = form.cleaned_data
          Name = data["Name"]
          Type = data["Type"]
          Quantity = data["Quantity"]
          RatePerUnit = data["RatePerUnit"]
          Amount = Quantity*RatePerUnit
          obj = Grocery(Name=Name,Type=Type,Quantity=Quantity,RatePerUnit=RatePerUnit,Amount=Amount)
          obj.save()
          return HttpResponseRedirect("./")

    else:
        form = GroceryForm()
        return render(request,'create.html',context={'form':form})
