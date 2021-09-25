from django.urls import path, include

urlpatterns = [
    path('admin/', include('func.adminUrls')),
    path('polls/', include('func.urls'))
]
