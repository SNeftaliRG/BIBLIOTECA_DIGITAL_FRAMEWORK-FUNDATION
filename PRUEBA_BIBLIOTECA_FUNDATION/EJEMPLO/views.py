from django.shortcuts import render

# Create your views here.
def baseview(request):
    #ESTO ES LA PAGINA PRINCIPAL
    return render(request,"base.html")

def ejemploview(request):
    #ejemplo llamando a base
    return render(request,"index.html")