from django.urls import path
from pizza_app.views import create, view, close, stats

#'<int:question_id>/
app_name = 'pizza'
urlpatterns = [
    path('create/', create, name='create'),
    path('<int:pizza_order_id>/view/', view, name='view'),
    path('<int:pizza_order_id>/close/', close, name='close'),

    path('stats/', stats, name='stats'),
]
