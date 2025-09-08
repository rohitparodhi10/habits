from django.db import models
from django.utils import timezone

class UserCustomHabits(models.Model):
    types=[
        ('Good', 'Good'),
        ('Bad', 'Bad')
    ]
    completion_history = models.JSONField(default=list, blank=True)
    name=models.CharField(max_length=100)
    habit_type=models.CharField(max_length=4, choices=types)
    frequency=models.CharField(max_length=50, help_text='e.g. Daily, Weekly, Monthly')
    start_date=models.DateField()
    end_date=models.DateField(null=True, blank=True)
    is_active=models.BooleanField(default=True)
    
    def __str__(self):
        return f'{self.name} - {self.habit_type}'
    


class HabitRecord(models.Model):
    habit = models.ForeignKey(UserCustomHabits, on_delete=models.CASCADE)
    date = models.DateField()
    completed = models.BooleanField(default=False)

    class Meta:
        unique_together = ('habit', 'date')


class Record(models.Model):
    habit = models.ForeignKey(UserCustomHabits, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.habit.name} - {self.date} - {'Done' if self.completed else 'Missed'}"
    