from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated  
from .permissions import TransactionPermission

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated , TransactionPermission]

    
    def get_queryset(self):
        user = self.request.user
        queryset = Transaction.objects.filter(user=user)

        type = self.request.query_params.get('type')
        category = self.request.query_params.get('category')

        if type:
            queryset = queryset.filter(type=type)

        if category:
            queryset = queryset.filter(category=category)

        return queryset
