from django.shortcuts import render, reverse, redirect
from .forms import FormGetLink
from .models import Links
import hashlib


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
            url_address = f.cleaned_data['url_address']
            url_hashed = hashlib.md5(url_address.encode()).hexdigest()
            if not Links.objects.filter(hash_link=url_hashed).exists():
                Links(user_input_link=url_address).save()

            return redirect('hash_redirect', hash_redirect=url_hashed)

        else:
            context['has_errors'] = True
            return render(request, template_name='get_link/index.html', context=context)

    return render(request, template_name='get_link/index.html', context=context)
