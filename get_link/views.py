from django.shortcuts import render
from .forms import FormGetLink
from .models import Links

# Create your views here.

def index(request):
    context = {
        'has_errors': False,
        'has_success': False,
    }
    if request.method == 'POST':
        f = FormGetLink(request.POST)
        if f.is_valid():
            context['has_success'] = True
            l = Links(user_input_link=f.cleaned_data['url_address'])
            l.save()
        else:
            context['has_errors'] = True
            return render(request, template_name='get_link/index.html', context=context)

    return render(request, template_name='get_link/index.html', context=context)
