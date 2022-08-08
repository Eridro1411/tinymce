from django.shortcuts import render
from .forms import TestoForm# Create your views here.
from .models import Testo
def HomeView(request):
    
    testi = Testo.objects.all()
    if request.method == "POST":
        testoform = TestoForm(request.POST)
        if testoform.is_valid():
            testoform.save(commit=False)
            testoform.area = request.POST.get('area')
            testoform.save()
    else:
        testoform = TestoForm()

    context={
        "testoform":testoform,
        "testi":testi
    }
    return render(request,"home.html",context)