from django.db import models
from django.contrib.auth.models import AbstractUser


class TrainingGroup(models.Model):
    label = models.CharField(max_length=255, verbose_name='Название')

    class Meta:
        verbose_name = 'группа'
        verbose_name_plural = 'группы'

    def __str__(self):
        return self.label


# Модель договоров
class Agreement(models.Model):
    label = models.IntegerField(unique=True, verbose_name='Номер договора')
    group_id = models.ForeignKey(TrainingGroup, on_delete=models.CASCADE, verbose_name='Учебная группа')
    TRAINING_CATEGORY_CHOICES = [('M', 'Мопед'), ('A', 'Мотоцикл'), ('B', 'Легковой автомобиль'), ('BE', 'Легковой автомобиль с прицепом'), ('C', 'Грузовик'),
                                 ('CE', 'Грузовик с прицепом'), ('D', 'Автобус'), ('DE', 'Автобус с прицепом'), ('TM', 'Трамвай'), ('TB', 'Троллейбус')]
    training_category = models.CharField(max_length=30, choices=TRAINING_CATEGORY_CHOICES, verbose_name='Категория прав обучение')
    start_date_training = models.DateField(verbose_name='Дата начала обучения')
    end_date_training = models.DateField(verbose_name='Дата окончания обучения')
    payment_confirm = models.BooleanField(help_text='0 - Не оплачено, 1 - Оплачено', verbose_name='Статус оплаты')

    class Meta:
        verbose_name = 'договор'
        verbose_name_plural = 'договора'

    def __str__(self):
        return 'Договор | Оплата: %s | %s' % (self.label, self.payment_confirm)


# Модель расписаания
class Timetable(models.Model):
    monday = models.CharField(max_length=155, blank=True, null=True, verbose_name='Понедельник')
    tuesday = models.CharField(max_length=155, blank=True, null=True, verbose_name='Вторник')
    wednesday = models.CharField(max_length=155, blank=True, null=True, verbose_name='Среда')
    thursday = models.CharField(max_length=155, blank=True, null=True, verbose_name='Четверг')
    friday = models.CharField(max_length=155, blank=True, null=True, verbose_name='Пятница')
    saturday = models.CharField(max_length=155, blank=True, null=True, verbose_name='Суббота')
    sunday = models.CharField(max_length=155, blank=True, null=True, verbose_name='Воскресенье')

    class Meta:
        verbose_name = 'расписание'
        verbose_name_plural = 'расписания'

    def __str__(self):
        return '%i' % self.id


# Модель пользователей (
#   - Курсанты user.role == 'cadet'
#   - Инструкторы user.role == 'instuctor'
#   - Сотрудники (уч. часть) user.role == 'oper'
# )
class User(AbstractUser):
    sur_name = models.CharField(max_length=155, verbose_name='Отчество')

    ROLE_CHOICES = [('cadet', 'Кадет'), ('instructor', 'Инструктор'), ('oper', 'Сотрудник')]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, verbose_name='Права')

    agreement_id = models.ForeignKey(Agreement, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Идентификатор договора')
    timetable_id = models.ForeignKey(Timetable, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Идентификатор расписания практических занятий')
    exam = models.BooleanField(help_text='0 - Не сдано, 1 - Сдано', default=False, verbose_name='Практическое занятие')

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.last_name + ' ' + self.first_name + ' ' + self.sur_name


# Модель автомобилей
class Car(models.Model):
    model = models.CharField(max_length=255, verbose_name='Модель')
    mark = models.CharField(max_length=255, verbose_name='Марка')

    class Meta:
        verbose_name = 'автомобиль'
        verbose_name_plural = 'автомобили'

    def __str__(self):
        return '%s %s - %i' % (self.model, self.mark, self.id)


# Модель практических занятий
class PracticalLesson(models.Model):
    instuctor_id = models.ForeignKey(User,
                                     on_delete=models.CASCADE,
                                     limit_choices_to={'role': 'instructor'},
                                     verbose_name='Идентификатор инструктора',
                                     related_name='Cadet')
    cadet_id = models.ForeignKey(User,
                                 on_delete=models.CASCADE,
                                 limit_choices_to={'role': 'cadet'},
                                 verbose_name='Идентификатор курсанта',
                                 related_name='Instructor')
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE, verbose_name='Идентификатор автомобиля')
    practic_time = models.DateTimeField(verbose_name='Время')

    class Meta:
        verbose_name = 'практика'
        verbose_name_plural = 'практики'

    # def __str__(self):
    #     return 'Практическое занятие: %i' % (self.id)