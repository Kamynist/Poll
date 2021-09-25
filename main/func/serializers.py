from rest_framework import serializers
from django.core.exceptions import ValidationError

# Проверка на ошибки от формы или модели
def validateQuestionType(value):
    if not value in ['TEXT', 'CHOICE', 'MULTIPLE_CHOICE']:
        raise ValidationError('Invalid question type')

# Опрос
class PollSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=300)
    startDate = serializers.DateField()
    finishDate = serializers.DateField()

# Вопрос
class QuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    type = serializers.CharField(max_length=30, validators=[validateQuestionType])
    text = serializers.CharField(max_length=300)

# Вариант ответа
class OptionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    index = serializers.IntegerField(required=False)
    text = serializers.CharField(max_length=100)

# Заполненный опрос
class SubmissionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    submitTime = serializers.DateTimeField(format='%Y-%m-%dT%H:%M:%S')

class UserOptionSerializer(serializers.Serializer):
    'Вариант ответа для пользователя'
    index = serializers.IntegerField()
    text = serializers.CharField(max_length=100)