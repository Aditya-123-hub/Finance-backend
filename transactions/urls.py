from rest_framework import routers
from transactions.views import TransactionViewSet

router = routers.DefaultRouter()
router.register('transactions', TransactionViewSet)
urlpatterns = router.urls
