from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.http import Http404
from .models import Card

# Create your views here.
def index(request):
    latest_cards_list = Card.objects.order_by('-created_at')[:20]
    template = loader.get_template('cards/index.html')
    context = RequestContext(request, {
        'latest_cards_list': latest_cards_list,
    })
    return HttpResponse(template.render(context))


def details(request, card_id):
    card = get_object_or_404(Card, pk=card_id)
    return render(request, 'cards/detail.html', {'card': card})


