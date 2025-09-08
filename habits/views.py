from django.shortcuts import render, redirect, get_object_or_404
from habits.models import *
from django.utils import timezone



def user_custom_habits_view(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        htype=request.POST.get('habit_type')
        freq=request.POST.get('frequency')
        sdate=request.POST.get('start_date')
        edate=request.POST.get('end_date')
        active=request.POST.get('is_active')
        
        if name and htype and freq and sdate and active:
            is_active=True if active=='True' else False
            end_date=edate if edate else None
            UserCustomHabits.objects.create(
                name=name,
                habit_type=htype,
                frequency=freq,
                start_date=sdate,
                end_date=end_date,
                is_active=is_active
            )
        return redirect('dashboard')
        
    habits=UserCustomHabits.objects.all()
    return render(request, 'habits.html', {'habits':habits})


def update_habit_view(request, habit_id):
    habit = get_object_or_404(UserCustomHabits, id=habit_id)

    if request.method == 'POST':
        habit.name = request.POST.get('name')
        habit.habit_type = request.POST.get('habit_type')
        habit.frequency = request.POST.get('frequency')
        habit.start_date = request.POST.get('start_date')
        habit.end_date = request.POST.get('end_date') or None
        habit.is_active = request.POST.get('is_active') == 'True'
        habit.save()
        return redirect('dashboard')

    return render(request, 'update.html', {'habit': habit})


def delete_habit_view(request, habit_id):
    habit = get_object_or_404(UserCustomHabits, id=habit_id)
    habit.delete()
    return redirect('dashboard')


def dashboard(request):
    today = timezone.now().date()
    habits = UserCustomHabits.objects.all()  

    incomplete_habits = []
    for habit in habits:
        record = Record.objects.filter(habit=habit, date=today).first()
        if not record or not record.completed:
            incomplete_habits.append(habit)

    records = Record.objects.filter(date=today)

    context = {
        'habits': incomplete_habits,  
        'records': records,
        'today': today,
    }
    return render(request, 'dashboard.html', context)

def mark_completed(request, habit_id):
    if request.method == 'POST':
        habit = UserCustomHabits.objects.get(id=habit_id)
        today = timezone.now().date().isoformat()

        record, created = Record.objects.get_or_create(habit=habit, date=today)
        record.completed = True
        record.save()

        if today not in habit.completion_history:
            habit.completion_history.append(today)
            habit.save()

    return redirect('dashboard')


def completed_habits(request):
    habits = UserCustomHabits.objects.all()
    
    habits_with_history = []
    for habit in habits:
        if habit.completion_history:  
            habits_with_history.append({
                'habit': habit,
                'history': habit.completion_history,
            })
    
    context = {
        'habits_with_history': habits_with_history,
    }
    
    return render(request, 'history.html', context)