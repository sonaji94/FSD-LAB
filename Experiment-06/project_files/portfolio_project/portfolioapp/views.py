from django.shortcuts import render


def main(request):
    return render(request, 'portfolioapp/home.html')


def about(request):
    return render(request, 'portfolioapp/about.html')


def contact(request):
    return render(request, 'portfolioapp/contactus.html')
