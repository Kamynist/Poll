from django.urls import path, include

from .views.user import Polls, PollById, PollsByUser

urlpatterns = [
    path('', Polls.as_view()),
    path('<int:id>', PollById.as_view()),
    path('pollsByUser/<int:id>', PollsByUser.as_view()),

]
