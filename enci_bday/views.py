from django.shortcuts import render

# Create your views here.
def enci_bday(request):
    return render(request, 'enci_bday_index.html')
