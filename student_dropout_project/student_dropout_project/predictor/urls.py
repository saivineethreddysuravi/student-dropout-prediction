from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('predict/', views.predict_view, name='predict'),
    path('result/<int:pk>/', views.prediction_result_view, name='prediction_result'),
    path('history/', views.history_view, name='history'),
    path('field-info/', views.field_info_view, name='field_info')
]
