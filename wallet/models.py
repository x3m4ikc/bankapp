import string
from random import random

from django.db import models


def generate_name() -> str:
    name = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    while Wallet.objects.filter(Wallet.objects.filter(name=name)):
        name = "".join(random.choices(string.ascii_uppercase + string.digits, k=8))
    return name


class Wallet(models.Model):
    """Model wallet"""
    TYPE = models.Choices("Visa", "Mastercard",)
    CURRENCIES = ("USD", "EUR", "RUB",)

    name = models.CharField(
        max_length=8, blank=True, verbose_name="Номер кошелька")
    type = models.CharField(
        max_length=10, choices=CURRENCIES, verbose_name="Тип кошелька")
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0, verbose_name="Баланс")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    modified_on = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    owner = models.ForeignKey("User", on_delete=models.CASCADE, related_name="wallets")

    def __str__(self):
        return self.name


class Transaction(models.Model):
    sender = models.ForeignKey(Wallet, related_name='sender', on_delete=models.CASCADE, verbose_name="Отправитель")
    receiver = models.ForeignKey(Wallet, related_name='receiver' , on_delete=models.CASCADE, verbose_name="Получатель")
    transfer_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Сумма")
    commission = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Комиссия")
    PAID_OR_FAILED = [("True", "PAID"), ("False", "FAILED")]
    status = models.CharField(max_length=15, choices=PAID_OR_FAILED, default="FAILED", verbose_name="Тип кошелька")
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")


class User(models.Model):
    username = models.CharField(max_length=150, unique=True, default=None, error_messages=
    {'unique': "A user with that username already exists."}, verbose_name="Владелец")

    def __str__(self):
        return self.username
