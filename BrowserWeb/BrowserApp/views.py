from tkinter.font import names

from django.shortcuts import render
from django.template.context_processors import request
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['Browser']
collection = db['SignUP']

# Create your views here.
def signup_views(request):
    if request.method == "POST":
        data = {
            "name": request.POST.get('name'),
            "email": request.POST.get('email'),
            "phone": request.POST.get('phone'),
            "gender": request.POST.get('gender'),
            "desgination": request.POST.get('desgination'),
            "company": request.POST.get('company'),
            "residence": request.POST.get('residence'),
            "monthly": request.POST.get('monthly'),
            "loan": request.POST.get('loan'),
            "marital": request.POST.get('marital'),
            "dependents": request.POST.get('dependents'),
            "city": request.POST.get('city'),
            "state": request.POST.get('state'),
        }
        collection.insert_one(data)
        return render(request, 'BrowserApp/success.html')
    return render(request, 'BrowserApp/signup.html')

def success_views(request):
    return render(request, 'BrowserApp/success.html')