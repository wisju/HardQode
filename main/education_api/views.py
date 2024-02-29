from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Lesson, Product
from .serializers import LessonSerializer, ProductSerializer, ProductStatisticSerializer


class ProductListView(generics.ListAPIView):
    """Список продуктов с дополнительной информацией"""

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]


class LessonListView(generics.ListAPIView):
    """Выведение списка уроков по конкретному продукту к которому пользователь имеет доступ"""

    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        product_id = self.kwargs["product_id"]
        user = self.request.user
        try:
            product = Product.objects.get(id=product_id, owner=user)
        except:
            return []
        return Lesson.objects.filter(
            product=product, product__pupil_product__check_access=True
        ).select_related("product")


class ProductStatisticListView(generics.ListAPIView):
    """Статистика продукта с дополнительной информацией"""

    queryset = Product.objects.all().select_related("owner")
    serializer_class = ProductStatisticSerializer
    permission_classes = [IsAuthenticated]
