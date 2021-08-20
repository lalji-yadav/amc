from django.shortcuts import render, redirect
from .forms import AmcForm
from django.contrib import messages
from .models import Amc

# Create your views here.


def data(request):
    return render(request, 'table.html')


def data2(request):
    return render(request, 'table2.html')


def dashboard(request):
    return render(request, 'dashboard.html')


def addAmc(request):

    if request.method == "POST":
        form = AmcForm(request.POST)
        print('hiiii')
        if form.is_valid():
            form.save()
            print('success')
            messages.success(request, 'Contact request submitted successfully.')
            return redirect('/dashboard/addAmc')
        else:
            messages.error(request, 'Invalid form submission.')
            # messages.error(request, form.errors)
    else:
        form = AmcForm()
    return render(request, 'addAmc.html', {'form':form})


def paidAmc(request):
    amclist = Amc.objects.all()
    print('AMC List', amclist)
    return render(request, 'paidAmc.html', {'amclist':amclist})


def pendingAmc(request):
    return render(request, 'pendingAmc.html')