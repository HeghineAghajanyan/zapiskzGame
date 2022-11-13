from typing import Any

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView

from core.forms import AddCard, TradeCard
from core.models import CardOwners, Card, Trade


class MainView(View):
    def get(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        return render(request, 'core/index.html')


class GetCardView(View):
    def get(self, request: WSGIRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        card = Card.Objects.get(id=0)
        return render(request, 'core/index (2).html', context={'card': card})

    def post(self, request):
        return render(request, 'core/index (2).html',)


class AddCard(FormView):
    template_name = 'core/index (2).html'
    form_class = AddCard
    success_url = reverse_lazy("collections/")
    def form_valid(self, form):
        CardOwners.objects.create(**form.cleaned_data)
        return super().form_valid(form)


class TradeCard(FormView):
    template_name = 'core/index (2).html'
    form_class = TradeCard
    success_url = reverse_lazy("tradenewcard/")

    def form_valid(self, form):
        form.cleaned_data["user"] = 0
        Trade.objects.create(**form.cleaned_data)
        return super().form_valid(form)


class TradeNewCard(View):
    def get(self, request: WSGIRequest, *args: Any, **kwargs: Any):
        for card in Trade.objects.all():
            if card.name != args.trading_card:
                return card
        return render(request, 'core/index (2).html', context={'card': card})


class CollectionListView(ListView):
    pass