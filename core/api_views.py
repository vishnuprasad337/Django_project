from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.db.models import Sum
from .models import Expense, Category
from .serializers import UserSerializer, ExpenseSerializer, CategorySerializer


# 👤 Register User (API)
@api_view(['POST'])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'User registered successfully!'})
    return Response(serializer.errors, status=400)


# 👥 List all users (API)
@api_view(['GET'])
def list_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


# 💰 Add Expense (API)
@api_view(['POST'])
def add_expense(request):
    serializer = ExpenseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Expense added successfully!'})
    return Response(serializer.errors, status=400)


# 📋 List all expenses (API)
@api_view(['GET'])
def list_expenses(request):
    expenses = Expense.objects.all()
    serializer = ExpenseSerializer(expenses, many=True)
    return Response(serializer.data)


# 📊 Expense Summary (API)
@api_view(['GET'])
def summary_report(request):
    summary = Expense.objects.values('category__name').annotate(total=Sum('amount'))
    data = {item['category__name']: item['total'] for item in summary}
    return Response(data)
