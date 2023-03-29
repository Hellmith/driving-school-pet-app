from django.db import models
from django.contrib.auth.models import AbstractUser


# КАТЕГОРИЯ
class Category(models.Model):
    name_category = models.CharField(max_length=155, verbose_name='Название')

    class Meta:
        verbose_name = 'категория'
        verbose_name = 'категории'

    def __str__(self):
        return self.name_category


# КУРС
class Course(models.Model):
    id_category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Стоимость')
    start_date_education = models.DateField(verbose_name='Дата начала')
    end_date_education = models.DateField(verbose_name='Дата окончания')

    class Meta:
        verbose_name = 'курс'
        verbose_name = 'курсы'

    def __str__(self):
        return self.id


# ДИСЦИПЛИНА
class Discipline(models.Model):
    name_discipline = models.CharField(max_length=255, verbose_name='Название дисциплины')
    count_hourse = models.IntegerField(verbose_name='Часов')
    type_class = models.CharField(max_length=255, verbose_name='Тип класса')

    class Meta:
        verbose_name = 'дисциплина'
        verbose_name = 'дисциплины'

    def __str__(self):
        return self.id


# РЕГИОН
class Region(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'регион'
        verbose_name = 'регионы'

    def __str__(self):
        return self.name


# ГОРОД
class City(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    id_region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name='Регион')

    class Meta:
        verbose_name = 'город'
        verbose_name = 'города'

    def __str__(self):
        return self.name


# УЛИЦЫ
class Street(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'улица'
        verbose_name = 'улицы'

    def __str__(self):
        return self.name


# ДОЛЖНОСТИ
class Post(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'должность'
        verbose_name = 'должности'

    def __str__(self):
        return self.name


# ПОЛЬЗОВАТЕЛИ
class User(AbstractUser):
    patronymic = models.CharField(blank=True, null=True, max_length=255, verbose_name='Отчество')
    date_of_birthday = models.DateField(blank=True, null=True, verbose_name='Дата рождения')

    passport_series = models.IntegerField(blank=True, null=True, verbose_name='Серия')
    passport_number = models.IntegerField(blank=True, null=True, verbose_name='Номер')
    date_references = models.DateField(blank=True, null=True, verbose_name='Дата выдачи')
    by_whom = models.CharField(blank=True, null=True, max_length=255, verbose_name='Кем выдан')

    id_region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Регион')
    id_city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Город')
    id_street = models.ForeignKey(Street, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Улица')
    house = models.CharField(blank=True, null=True, max_length=4, verbose_name='Дом')
    apartment = models.IntegerField(blank=True, null=True, verbose_name='Квартира')

    tel = models.CharField(blank=True, null=True, max_length=12, verbose_name='Телефон')

    status = models.CharField(max_length=255, blank=True, null=True, verbose_name='Статус')
    is_cursant = models.BooleanField(default=False, verbose_name='Курсант')

    id_post = models.ForeignKey('Post', on_delete=models.CASCADE, blank=True, null=True, verbose_name='Должность')
    is_worker = models.BooleanField(default=False, verbose_name='Сотрудник')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name = 'пользователи'

    def __str__(self):
        return '%s %s %s' % (self.last_name, self.first_name, self.patronymic)


# ОБУЧЕНИЕ
class Training(models.Model):
    id_cursant = models.ForeignKey('User', limit_choices_to={'is_cursant': 1}, on_delete=models.CASCADE, verbose_name="Курсант", related_name='cursant')
    id_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="Курс")
    agreement_number = models.IntegerField(verbose_name='Номер договора')
    date_agreement = models.DateTimeField(verbose_name='Дата договора')
    certificate = models.CharField(max_length=255, verbose_name='Свидетельство')
    date_record = models.DateField(verbose_name='Дата зачисления')
    price = models.IntegerField(verbose_name='Стоимость')
    payment_status = models.BooleanField(verbose_name='Статус оплаты')

    class Meta:
        verbose_name = 'обучение'
        verbose_name = 'обучения'

    def __str__(self):
        return '%i %i' % (self.id_cursant, self.id_course)


# РАСПИСАНИЕ
class Schedule(models.Model):
    id_worker = models.ForeignKey(User, limit_choices_to={'is_worker': 1, 'post': 2}, on_delete=models.CASCADE, verbose_name='Сотрудник', related_name='Worker')
    id_cursant = models.ForeignKey(User, limit_choices_to={'is_cursant': 1}, on_delete=models.CASCADE, verbose_name='Курсант', related_name='Cursant')
    id_discipline = models.ForeignKey(Discipline, on_delete=models.CASCADE, verbose_name='Дисциплина')
    date_class = models.DateField(verbose_name='Дата занятия')
    time_class = models.TimeField(verbose_name='Время занятия')

    class Meta:
        verbose_name = 'расписание'
        verbose_name = 'расписания'

    def __str__(self):
        return self.id


# АВТОМОБИЛИ
class Car(models.Model):
    gos_number = models.CharField(max_length=8, verbose_name='Гос. номер')
    model = models.CharField(max_length=255, verbose_name='Модель')
    mark = models.CharField(max_length=255, verbose_name='Марка')
    date_release = models.DateField(verbose_name='Дата выпуска')

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name = 'автомобили'

    def __str__(self):
        return '%s %s %s %d' % (self.gos_number, self.model, self.mark, self.date_release)


# ВОЖДЕНИЕ
class Driving(models.Model):
    id_cursant = models.ForeignKey(User, limit_choices_to={'is_cursant': 1}, on_delete=models.CASCADE, verbose_name='Курсант')
    id_schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, verbose_name='Расписание')
    id_car = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Автомобиль')
    result = models.CharField(max_length=255, verbose_name='Результат')

    class Meta:
        verbose_name = 'вождение'
        verbose_name = 'вождения'

    def __str__(self):
        return self.id
