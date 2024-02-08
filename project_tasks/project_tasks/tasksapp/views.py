from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# def home(request):
#     return HttpResponse("helo iam the homepage")
#
# def over(request):
#     return render(request, "over.html")
#
# def contact(request):
#     return HttpResponse("hello ,welcome to contact page")
#
# def details(request):
#     return render(request, "details.html")
#
# def thanks(request):
#     return render(request, "thanks.html")
def result(request):
    name="   here....."
    return render(request,"result.html",{'obj':name})
def results(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res_add=x+y
    res_sub=x-y
    res_div=x/y
    res_mul=x*y
    return render(request,"results.html",{'result1':res_add,'result2':res_sub,'result3':res_div,'result4':res_mul})



