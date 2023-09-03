from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

from get_link.models import Links


# Create your views here.

def redirect_page(request):
    return redirect('get_link_page')


def redirect_hash(request, hash_redirect):
    context = {
        # 'info': Links.objects.get(hash_link=hash_redirect),
        'info': get_object_or_404(Links, hash_link=hash_redirect),
    }

    return render(request, template_name='redirect_link/index.html',
                  context=context)


def redirect_hash_10_char(request, hash_r_10_char):
    context = {
        # 'info': Links.objects.get(hash_link__startswith=hash_r_10_char),
        'info': get_object_or_404(Links, hash_link__startswith=hash_r_10_char),
    }

    return render(request, template_name='redirect_link/index.html',
                  context=context)


def redirect_hash_slug(request, hash_r_slug):
    context = {
        # 'info': Links.objects.get(slug=hash_r_slug),
        'info': get_object_or_404(Links, slug=hash_r_slug),
    }

    return render(request, template_name='redirect_link/index.html',
                  context=context)
