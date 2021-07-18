from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from django.utils import timezone
from .models import *

# Create your views here.
def home(request) :
    return render(request, 'home.html')