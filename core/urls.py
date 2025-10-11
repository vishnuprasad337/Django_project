from django.urls import path
from . import views, api_views  # ✅ this will now work

urlpatterns = [
    # 🌐 Template pages
    path('', views.index, name='index'),
    path('register/', views.register_user, name='register'),
    path('users/', views.users_list, name='users'),
    path('users/delete/<int:user_id>/', views.delete_user, name='delete_user'),
    path('expense/', views.expense_tracker, name='expense_tracker'),

    # ⚙️ REST API endpoints
    path('api/register/', api_views.register_user, name='api_register_user'),
    path('api/users/', api_views.list_users, name='api_list_users'),
    path('api/expenses/', api_views.list_expenses, name='api_list_expenses'),
    path('api/expenses/add/', api_views.add_expense, name='api_add_expense'),
    path('api/expenses/summary/', api_views.summary_report, name='api_summary_report'),
]
