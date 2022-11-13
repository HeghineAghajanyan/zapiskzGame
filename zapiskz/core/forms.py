from django import forms
from core.models import CardOwners, Trade


class AddCard(forms.ModelForm):
    class Meta:
        model = CardOwners
        exclude = ["id"]


class TradeCard(forms.ModelForm):
    class Meta:
        model = Trade
        exclude = ["id"]

