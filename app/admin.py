from django.contrib import admin
from .models import TrainingGroup, Agreement, Timetable, User, Car, PracticalLesson


@admin.register(TrainingGroup)
class TrainingGroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'label')
    ordering = ['id']
    search_fields = ['label']


@admin.register(Agreement)
class AgreementAdmin(admin.ModelAdmin):
    list_display = ('label', 'group_id', 'training_category', 'start_date_training', 'end_date_training', 'payment_confirm')
    list_filter = ('label', 'group_id', 'training_category', 'start_date_training', 'end_date_training', 'payment_confirm')
    ordering = ['id']


@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('id', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    list_filter = ('id', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
    ordering = ['id']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'last_name', 'first_name', 'sur_name', 'role', 'is_superuser', 'date_joined')
    list_filter = ('role', 'is_superuser', 'date_joined')
    ordering = ['id']
    search_fields = [
        'username',
        'last_name',
        'first_name',
        'sur_name',
    ]


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'mark')
    ordering = ['id']
    list_filter = ('model', 'mark')


@admin.register(PracticalLesson)
class PracticalLessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'instuctor_id', 'cadet_id', 'car_id', 'practic_time')
    ordering = ['id']
    list_filter = ('instuctor_id', 'cadet_id', 'car_id')


# admin.site.register(User)