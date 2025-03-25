from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, resolve_url
from django.views.decorators.http import require_POST
from .models import Item


def home_view(request: HttpRequest):
    items = Item.objects.all()

    context = {"items": items}
    return render(request, "a_home/home.html", context)


@require_POST
def create_item(request):
    if request.user.is_authenticated:
        name = request.POST.get("name")
        item = Item(name=name)
        item.save()
        return HttpResponse(f'<li class="font-1 text-4xl">{item.name}</li>')

    response = HttpResponse()
    response.headers["HX-Redirect"] = resolve_url("account_login")
    return response
