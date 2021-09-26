# Polls Manager

# /admin

### admin/polls - Все опросы

  Тело ответа:
```
  [
    {
        "id": 1,
        "title": "Проверка",
        "description": "Проверка работы",
        "startDate": "2021-09-24",
        "finishDate": "2021-10-24"
    },
    {
        "id": 2,
        "title": "1",
        "description": "ТЕст",
        "startDate": "2021-09-24",
        "finishDate": "2021-09-24"
    }
]
```



### admin/polls/[id] - Опрос

  Тело ответа:
  ```
  {
    "id": 1,
    "title": "Проверка",
    "description": "Проверка работы",
    "startDate": "2021-09-24",
    "finishDate": "2021-10-24",
    "questions": [
        {
            "id": 1,
            "type": "CHOICE",
            "text": "Работает?",
            "options": []
        }
    ]
}
  ```

  
  
### admin/polls/[id]/questions - вопросы опроса
  
  Тело ответа:
```
{
    "detail": "Method \"GET\" not allowed."
}
```
  
  
  
### admin/polls/[id]/questions/<id> - Вопрос опроса
  
  Тело ответа:
```
{
    "detail": "Not found."
}
```
  
  
  
# /polls

### polls - опросы
  
Тело ответа:
  ```
  [
    {
        "id": 1,
        "title": "Проверка",
        "description": "Проверка работы",
        "startDate": "2021-09-24",
        "finishDate": "2021-10-24"
    }
]
  ```
  
  
  
### polls/<id> - опрос
  
  Тело ответа:
```  
{
  "id": 1,
  "title": "Проверка",
  "description": "Проверка работы",
  "startDate": "2021-09-24",
  "finishDate": "2021-10-24",
  "questions": [
      {
          "id": 1,
          "type": "CHOICE",
          "text": "Работает?",
          "options": []
      }
  ]
}
```
