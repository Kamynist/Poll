from django.db import models
from django.core.exceptions import ValidationError

# Проверка на ошибки от формы или модели
def validateQuestionType(value):
    if not value in ['TEXT', 'CHOICE', 'MULTIPLE_CHOICE']:
        raise ValidationError('Invalid question type')

# Типы вопросов
OPTION_TYPES = ['CHOICE', 'MULTIPLE_CHOICE']

# Опрос
class Poll(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    startDate = models.DateField()
    finishDate = models.DateField()

    # Нормальное отображение в админке
    def __str__(self):
        return self.title


# Вопрос
class Question(models.Model):
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    type = models.CharField(max_length=30, validators=[validateQuestionType])
    text = models.CharField(max_length=300)

    @property
    def hasOptionType(self):
        return self.type in OPTION_TYPES

    def __str__(self):
        return self.type



# Вариант ответа
class Option(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    index = models.PositiveIntegerField()
    text = models.CharField(max_length=100)

    # Нормальное отображение в админке
    def __str__(self):
        return self.question


# Заполненный опрос
class Submission(models.Model):
    userId = models.IntegerField(db_index=True)
    poll = models.ForeignKey('Poll', on_delete=models.CASCADE)
    submitTime = models.DateTimeField(auto_now_add=True)


# При записи ответа на вопрос мы копируем тип и текст вопроса.
# Также копируется текст вариантов ответа (для соотв. вопросов).
# Это позволит сохранить вопросы и варианты ответов такими, какими они были на момент прохождения опроса.
# Ответ на вопрос

class Answer(models.Model):
    submission = models.ForeignKey('Submission', on_delete=models.CASCADE)
    question = models.ForeignKey('Question', on_delete=models.CASCADE)
    questionType = models.CharField(max_length=30, validators=[validateQuestionType])
    questionText = models.CharField(max_length=300)
    answerText = models.CharField(max_length=300)

# Обновить структуру таблиц:
# python manage.py makemigrations backend
# python manage.py migrate