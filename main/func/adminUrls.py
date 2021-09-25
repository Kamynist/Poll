from django.urls import path, include

from .views.admin import AdminPolls, AdminPollById, AdminQuestions, AdminQuestionById

urlpatterns = [
    path('', include([
        path('polls', AdminPolls.as_view()),
        path('polls/<int:id>', AdminPollById.as_view()),
        path('polls/<int:id>/questions', AdminQuestions.as_view()),
        path('polls/<int:pollId>/questions/<int:questionId>', AdminQuestionById.as_view())
    ]))
]