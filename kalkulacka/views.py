from django.shortcuts import render, HttpResponse

def index(request):
    if request.method == 'GET':
        vysledok = 0
    if request.method == 'POST':
        a = int(request.POST["a"])
        b = int(request.POST["b"])
        operation = request.POST["operation"]
        if operation == "+":
            vysledok = a + b
        elif operation == "-":
            vysledok = a - b
        elif operation == "*":
            vysledok = a * b
        else:
            vysledok = a / b

    
    return render(request, 'kalkulacka/index.html', dict(vysledok=vysledok))