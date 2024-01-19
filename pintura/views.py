from django.shortcuts import render
from django.http import HttpResponse

def pintura_inicio(request):
    if request.method == "GET":
        print(request.method)
        return render(request,'html/index.html')
    elif request.method =="POST":
        largura = request.POST.get('Largura')
        comprimento = request.POST.get('Comprimento')
        rendimento = request.POST.get('Rendimento')
        resultado = float(largura) * float(comprimento)
        total = float(resultado) / float(rendimento)
        return HttpResponse(f'Com a Largura {largura} metros, e o comprimento {comprimento} metros, a metragem quadrada é: {resultado:.2f} metros quadrados. Será necessário {total:.1f} litros de tinta.')