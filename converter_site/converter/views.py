from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView

from .models import Creature


class CreatureView(TemplateView):
    model = Creature
    template_name = "creature/index.html"

    def get(self, request, *args, **kwargs):
        return HttpResponse(f"Hello from the other side."
                            f"\nrequest = {request}"
                            f"\nargs = {args}"
                            f"\nkwargs = {kwargs}")


class CreatureAsHtmlView(generic.TemplateView):
    template_name = 'converter/creature/valloric.html'


def index(request):
    return HttpResponse("Hello, world.")
