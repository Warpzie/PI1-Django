from django.shortcuts import render

def index(request):
    if request.method == "GET":
        a = 0
        b = 0
    if request.method == "POST":
        a = float(request.POST["a"])
        b = float(request.POST["b"])
        comp = ""
        evenA = ""
        evenB = ""
        primeA = ""
        primeB = ""
        if a > b:
            comp = "A"
        elif a < b:
            comp = "B"
        if a % 2 == 0:
            evenA = "parne"
        else:
            evenA = "neparne"
        if b % 2 == 0:
            evenB = "parne"
        else:
            evenB = "neparne"
        if a > 3:
            primeA = "je" 
            for i in range(2, int(a)):
                if (a % i) == 0:
                    primeA = "nie je "
                    break 
        else:
            primeB = "je " 
        if b > 3:
            primeB = "je" 
            for i in range(2, int(b)):
                if (b % i) == 0:
                    primeB = "nie je "
                    break 
        else:
            primeB = "je " 
    return render(request, 'appCisla/index.html', {"a":a, "b":b, "comp":comp, "evenA":evenA, "evenB":evenB, "primeA":primeA, "primeB":primeB})