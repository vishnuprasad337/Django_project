from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.db.models import Sum
from .models import Expense
from .forms import RegisterForm, ExpenseForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# 🏠 Home Page
def index(request):
    return render(request, 'core/index.html')

# 👤 Register new user (register + user list combined)
def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'User registered successfully!')
            return redirect('register')
    else:
        form = RegisterForm()

    users = User.objects.all()
    return render(request, 'core/register.html', {'form': form, 'users': users})

# 💰 Expense tracker (add + list + summary)
def expense_tracker(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = User.objects.first()  # temporary – assign first user
            expense.save()
            messages.success(request, 'Expense added successfully!')
            return redirect('expense_tracker')
    else:
        form = ExpenseForm()

    expenses = Expense.objects.all().order_by('-date')
    summary = Expense.objects.values('category__name').annotate(total=Sum('amount'))

    return render(request, 'core/expense.html', {
        'form': form,
        'expenses': expenses,
        'summary': summary,
    })

# 👥 User list page (only user list)
def users_list(request):
    users = User.objects.all()
    return render(request, 'core/users.html', {'users': users})
def delete_user(request, user_id):
    try:
        user = User.objects.get(id=user_id)
        user.delete()
        messages.success(request, f'User "{user.username}" deleted successfully!')
    except User.DoesNotExist:
        messages.error(request, 'User not found!')
    return HttpResponseRedirect(reverse('users'))
@login_required
def users_list(request):
    users = User.objects.all()
    return render(request, 'core/users.html', {'users': users})
