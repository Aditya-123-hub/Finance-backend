from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from transactions.models import Transaction
from django.db.models import Sum
from transactions.permissions import TransactionPermission

class DashboardView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user

        transactions = Transaction.objects.filter(user=user)

        income_transactions = transactions.filter(type='income')
        expense_transactions = transactions.filter(type='expense')

        total_income = income_transactions.aggregate(Sum('amount'))['amount__sum']
        total_expense = expense_transactions.aggregate(Sum('amount'))['amount__sum']

        if total_income is None:
            total_income = 0

        if total_expense is None:
            total_expense = 0

        net_balance = total_income - total_expense

        data = {
            "total_income": total_income,
            "total_expense": total_expense,
            "net_balance": net_balance
        }

        return Response(data)
