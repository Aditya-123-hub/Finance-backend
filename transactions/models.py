from django.db import models
from django.conf import settings

INCOME = 'income'
EXPENSE = 'expense'
class Transaction(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)
    TYPE_CHOICES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]
    type = models.CharField(max_length=10, choices=TYPE_CHOICES ,default=INCOME)  # 'income' or 'expense'
    description = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.type} - {self.amount}"

    
