from rest_framework import serializers
from .models import Transaction

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'user', 'amount', 'category', 'type', 'description', 'date', 'created_at', 'updated_at']
        read_only_fields = ['user']

    def create(self, validated_data):
            user = self.context['request'].user
            transaction = Transaction.objects.create(
                user=user,
                amount=validated_data.get('amount'),
                category=validated_data.get('category'),
                type=validated_data.get('type'),
                description=validated_data.get('description', ''),
                date=validated_data.get('date')
            )
            
            return transaction 

    def validate_amount(self, value):
         if value <=0:
              raise serializers.ValidationError("Amount must be greater than zero.") 
         return value  
                
                