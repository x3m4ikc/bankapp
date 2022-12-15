"""bankapp URL Configuration"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from wallet.views import WalletViewSet, UserViewSet, TransactionViewSet, UserRegisterViewSet

router = routers.DefaultRouter()
router.register(r'wallets', WalletViewSet, basename='wallet')
router.register(r'user', UserViewSet, basename='user')
router.register(r'wallets/transaction', TransactionViewSet, basename='transaction')
router.register(r'register', UserRegisterViewSet, basename='registration')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('drf-auth/', include('rest_framework.urls')),
]

# TODO: POST user username, email, password
# TODO: POST /wallets { "type": "visa", "currency": "RUB"} User can't create more than 5 wallets.
# TODO: GET /wallets/<name> - get wallet where name=<name>. Example - /wallets/VB07N96L
# TODO: DELETE /wallets/<name> - delete wallet
# TODO: POST /wallets/transactions/ - create new transaction. Example:
# {
# "sender": "VB07N96L"
# "receiver": "MJYR096L",
# "transfer_amount": "100.00"
# }
# TODO: GET /wallets/transactions/<transaction_id> - get transaction
# TODO: GET /wallets/transactions/<wallet_name> - get all transactions where wallet was sender or receiver
