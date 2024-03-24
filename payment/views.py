from django.shortcuts import render

def test(request):
    return render(request, 'payment/test_template.html')
