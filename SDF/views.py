from django.shortcuts import render, redirect


def show_log(request):
    return render(request, 'SDF_login.html')

def show_reg(request):
    return render(request, 'SDF_register.html')

def show_index(request):
    return render(request, 'SDF_article.html')
