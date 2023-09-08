from django.shortcuts import render, reverse
from .forms import FormGetLink
from .models import Links
# import hashlib

from utils.hasher import MD5


# Create your views here.

def index(request):
    context = {
        'has_errors': False,
        'has_success': False,
        'redirect_link': '',
        'redirect_link_10_char': '',
        'redirect_link_slug': '',
    }
    status_code = 200

    if request.method == 'POST':
        f = FormGetLink(request.POST)
        if f.is_valid():
            context['has_success'] = True
            url_address = f.cleaned_data['url_address']
            url_hashed = MD5(url_address).md5().__str__()

            obj = Links.objects
            if not obj.filter(hash_link=url_hashed).exists():
                Links(user_input_link=url_address).save()

            context['redirect_link'] = request.build_absolute_uri(
                reverse('hash_redirect', args=[url_hashed])
            )

            context['redirect_link_10_char'] = request.build_absolute_uri(
                reverse('hash_r_10_char', args=[url_hashed[:10]])
            )

            slug = obj.get(hash_link=url_hashed).slug

            context['redirect_link_slug'] = request.build_absolute_uri(
                reverse('hash_r_slug', args=[slug])
            )

        else:
            context['has_errors'] = True
            status_code = 422

    return render(
        request,
        template_name='get_link/index.html',
        context=context,
        status=status_code,
    )
