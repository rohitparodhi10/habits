from django.urls import path, include
from habits.views import *

urlpatterns = [
    path('add-habits/',user_custom_habits_view, name='add_habits'),
    path('habits/update/<int:habit_id>/', update_habit_view, name='update_habit'),
    path('habits/delete/<int:habit_id>/', delete_habit_view, name='delete_habit'),
    path('dashboard/', dashboard, name='dashboard'),
    path('mark/<int:habit_id>/', mark_completed, name='mark_completed'),
    path('history/', completed_habits, name='history')
]
