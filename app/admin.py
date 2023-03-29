from django.contrib import admin
from .models import Category, Course, Discipline, Region, City, Street, Post, User, Training, Schedule, Car, Driving


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name_category']
    ordering = ['id']
    search_fields = ['name']


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id_category', 'price', 'start_date_education', 'end_date_education')
    list_filter = ('start_date_education', 'end_date_education')
    ordering = ['id']
    search_fields = ['id_category', 'price', 'start_date_education', 'end_date_education']


@admin.register(Discipline)
class DisciplineAdmin(admin.ModelAdmin):
    list_display = ('name_discipline', 'count_hourse', 'type_class')
    list_filter = ('count_hourse', 'type_class')
    ordering = ['id']
    search_fields = ['name_discipline', 'count_hourse', 'type_class']


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['id']
    search_fields = ['name']


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'id_region']
    ordering = ['id']
    search_fields = ['name']


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['id']
    search_fields = ['name']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['id']
    search_fields = ['name']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Данные аккаунта', {
            'fields': ('username', 'password', 'date_joined')
        }),
        ('Данные пользователя', {
            'fields': ('last_name', 'first_name', 'patronymic', 'date_of_birthday', 'email', 'tel')
        }),
        ('Данные паспорта', {
            'fields': ('passport_series', 'passport_number', 'date_references', 'by_whom')
        }),
        ('Права', {
            'fields': ('is_superuser', 'is_cursant', 'is_worker', 'id_post')
        }),
        (None, {
            'fields': ['status']
        }),
    )
    list_display = ('username', 'email', 'last_name', 'first_name', 'patronymic', 'date_of_birthday', 'is_cursant', 'is_worker', 'is_superuser')
    list_filter = ('is_cursant', 'is_worker')
    ordering = ['id']
    search_fields = [
        'username',
        'email',
        'id_post',
        'last_name',
        'first_name',
        'patronymic',
    ]


@admin.register(Training)
class TrainingAdmin(admin.ModelAdmin):
    list_display = ('id_cursant', 'id_course', 'agreement_number', 'date_agreement', 'certificate', 'date_record', 'price', 'payment_status')
    list_filter = ('id_cursant', 'id_course')
    ordering = ['id']
    search_fields = ['id_cursant', 'id_course', 'agreement_number', 'date_agreement', 'certificate', 'date_record', 'price', 'payment_status']


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('id_worker', 'id_cursant', 'id_discipline', 'date_class', 'time_class')
    list_filter = ('id_worker', 'id_cursant', 'id_discipline')
    ordering = ['id']
    search_fields = ['id_worker', 'id_cursant', 'id_discipline', 'date_class', 'time_class']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('gos_number', 'model', 'mark', 'date_release')
    list_filter = ('model', 'mark', 'date_release')
    ordering = ['id']
    search_fields = ['gos_number', 'model', 'mark', 'date_release']


@admin.register(Driving)
class Drivingdmin(admin.ModelAdmin):
    list_display = ('id_cursant', 'id_schedule', 'id_car', 'result')
    list_filter = ('id_cursant', 'id_schedule', 'id_car', 'result')
    ordering = ['id']
    search_fields = ['id_cursant', 'id_schedule', 'id_car', 'result']