from django.contrib import admin
from core.models import Collection, Card, CardOwners, Trade


@admin.register(Collection)
class CollectionsAdmin(admin.ModelAdmin):
    pass


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass


@admin.register(CardOwners)
class CardOwnersAdmin(admin.ModelAdmin):
    pass


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    pass
