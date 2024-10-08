from django.shortcuts import render, get_object_or_404
from .models import Car
# Create your views here.
def car_list(request):
    cars = Car.objects.all()
    return render(request, 'cars/car_list.html', {'cars': cars})

def car_detail(request, id):
    car = get_object_or_404(Car, id=id)
    return render(request, 'cars/car_detail.html', {'car': car})
