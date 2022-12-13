import string
from random import random

from django.db import models


def generate_name():
    name = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    while Wallet.objects.filter(Wallet.objects.filter(name=name)):
        name = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return name


class Wallet(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, verbose_name="Владелец карты")
    name = models.CharField(max_length=9, default=generate_name)
    TYPE_OF_WALLET = [("Visa", "Visa"), ("Mastercard", "Mastercard")]
    type = models.CharField(max_length=15, choices=TYPE_OF_WALLET, default="Visa", verbose_name="Тип кошелька")
    CURRENCIES = [("USD", "US Dollar"), ("EUR", "Euro"), ("RUB", "Ruble")]
    currency = models.CharField(max_length=4, choices=CURRENCIES, default="USD", verbose_name="Валюта")
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Баланс")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    modified_on = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    def __str__(self):
        return self.name


class Transaction(models.Model):
    sender = models.ForeignKey(Wallet, verbose_name="Отправитель", on_delete=models.PROTECT, related_name='sender')
    receiver = models.ForeignKey(Wallet, verbose_name="Получатель", on_delete=models.PROTECT, related_name='receiver')
    transfer_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Сумма")
    commission = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Комиссия")
    PAID_OR_FAILED = [("True", "PAID"), ("False" ,"FAILED")]
    status = models.CharField(max_length=15, choices=PAID_OR_FAILED, default="FAILED", verbose_name="Тип кошелька")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")


class User(models.Model):
    user = models.CharField(max_length=255, verbose_name="Владелец")
