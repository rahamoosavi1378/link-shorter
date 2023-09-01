from django.shortcuts import (
    render,
    redirect
)

from get_link.models import Links


# Create your views here.

def redirect_page(request):
    return redirect('get_link_page')


def redirect_hash(request, hash_redirect):
    context = {
        'info': Links.objects.get(hash_link=hash_redirect)
    }

    return render(request,
                  template_name='redirect_link/index.html',
                  context=context
                  )