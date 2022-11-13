from django.contrib.auth.models import User
from django.db import models


class Collection(models.Model):
    name = models.CharField("CollectionName", max_length=225, null=False, blank=False)
    number_of_cards = models.IntegerField("NumberOfCards")
    bonus_first_stage = models.IntegerField("BonusFirstStage")
    bonus_second_stage = models.IntegerField("BonusSecondStage")
    bonus_third_stage = models.IntegerField("BonusThirdStage")
    image = models.ImageField(
        "CollectionImage",
        upload_to='Collections',
        null=True,
        blank=True,
    )

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()
        return 1


class Card(models.Model):
    name = models.CharField("NameOfCard", max_length=255, null=False, blank=False)
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    image = models.ImageField(
        "CardImage",
        upload_to='Cards',
        null=True,
        blank=True,
    )

    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def delete(self, using=None, keep_parents=False):
        self.deleted = True
        self.save()
        return 1


class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET('Deleted'))
    card = models.ForeignKey(Card, on_delete=models.SET('Deleted'))


class CardOwners(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET('Deleted'))
    card = models.ForeignKey(Card, on_delete=models.SET('Deleted'))
    date_acquired = models.DateTimeField("DateTime", auto_now_add=True)
