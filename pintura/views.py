from django.shortcuts import render
from django.http import HttpResponse

def pintura_inicio(request):
    if request.method == "GET":
        return render(request,'html/index.html')
    
    elif request.method =="POST":
        largura = request.POST.get('Largura')
        comprimento = request.POST.get('Comprimento')
        rendimento = request.POST.get('Rendimento')
        resultado = float(largura) * float(comprimento)
        total = float(resultado) / float(rendimento)
       
        
        context = {
            'Largura' : largura ,
            'Comprimento' : comprimento,
            'Resultado' : str(resultado),
            'Rendimento' : rendimento,
            'Total' : str(total),
        }
     
        return render(request,'html/resultado_pintura.html', context)

