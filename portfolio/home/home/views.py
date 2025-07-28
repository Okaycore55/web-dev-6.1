from django.shortcuts import render, HttpResponse

def home(request):
    #return HttpResponse("This is the home page(/)")
    return render(request, 'home.html')

# You can add more views here as needed
def portfolio(request):
     #return HttpResponse("This is the portfolio page(/portfolio)")
     return render(request, 'portfolio.html')

def about(request):
     #return HttpResponse("This is the about page(/about)")
     return render(request, 'about.html')
def contact(request):
     #return HttpResponse("This is the contact page(/contact)")
     return render(request, 'contact.html')
