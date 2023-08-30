from django.shortcuts import render
from .forms import FormGetLink


# Create your views here.

def index(request):
    if request.method == 'POST':
        f = FormGetLink(request.POST)
        if f.is_valid():
            print(f.cleaned_data)
        else:
            return render(request, template_name='get_link/index.html', context={
                'has_errors': True
            })

    return render(request, template_name='get_link/index.html', context={
        'has_errors': False
    })
