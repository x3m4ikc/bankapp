from django.contrib import admin

from wallet.models import Wallet, Transaction, User

admin.site.register(Wallet)
admin.site.register(Transaction)
admin.site.register(User)
