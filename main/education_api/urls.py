from django.urls import path
from .views import ProductListView, LessonListView, ProductStatisticListView

urlpatterns = [
    path("products/", ProductListView.as_view()),
    path("products/<int:product_id>/lessons/", LessonListView.as_view()),
    path("statistics/", ProductStatisticListView.as_view()),
]
