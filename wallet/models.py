from django.db import models


class Wallet(models.Model):
    """Model wallet"""
    TYPE_CHOICES = (
        ("VISA", "VISA"),
        ("MASTERCARD", "MASTERCARD")
    )

    CURRENCIES_CHOICES = (
        ("USD", "USD"),
        ("EUR", "EUR"),
        ("RUB", "RUB"),
    )

    name = models.CharField(
        max_length=8, blank=True, verbose_name="Номер кошелька")
    type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, verbose_name="Тип кошелька")
    currency = models.CharField(
        max_length=3, choices=CURRENCIES_CHOICES, verbose_name="Валюта")
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=True, verbose_name="Баланс")
    created_on = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    modified_on = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    owner = models.ForeignKey("User", on_delete=models.CASCADE, related_name="wallets")

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """Model transaction"""
    PAID_OR_FAILED = (
        ("True", "PAID"),
        ("False", "FAILED")
    )

    sender = models.ForeignKey(Wallet,
                               related_name='sender',
                               on_delete=models.CASCADE,
                               verbose_name="Отправитель")
    receiver = models.ForeignKey(Wallet,
                                 related_name='receiver',
                                 on_delete=models.CASCADE,
                                 verbose_name="Получатель")
    transfer_amount = models.DecimalField(max_digits=10,
                                          decimal_places=2,
                                          default=0.00,
                                          verbose_name="Сумма")
    commission = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, verbose_name="Комиссия")
    status = models.CharField(
        max_length=15, choices=PAID_OR_FAILED, verbose_name="Тип кошелька")
    timestamp = models.DateTimeField(
        auto_now_add=True, verbose_name="Время создания")


class User(models.Model):
    """Model user"""
    username = models.CharField(max_length=50, blank=True, verbose_name="Владелец")

    def __str__(self):
        return self.username
