from django.http import HttpResponse
from django.template import loader

from app_familia.models import Familiar


# Vista Index
def index(request):
    template = loader.get_template('index.html')
    context_dict = {
        'familiares': Familiar.objects.all()
    }
    return HttpResponse(template.render(context_dict))


def show(request, id: int):
    return HttpResponse(id)


def create(request):
    return HttpResponse("Formulario para agregar un Familiar")


def store(request):
    pass
