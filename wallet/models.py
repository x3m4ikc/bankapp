from django.db import models


class User(models.Model):
    """Model user"""
    username = models.CharField(
        max_length=50, blank=True, db_index=True)

    def __str__(self):
        return self.username


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

    name = models.CharField(max_length=8, blank=True)
    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    currency = models.CharField(max_length=3, choices=CURRENCIES_CHOICES)
    balance = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

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
    transfer_amount = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00,)
    commission = models.DecimalField(
        max_digits=10, decimal_places=2, default=0.00)
    status = models.CharField(max_length=15, choices=PAID_OR_FAILED)
    timestamp = models.DateTimeField(auto_now_add=True)
