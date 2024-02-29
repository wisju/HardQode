from django.contrib.auth.models import User
from django.db.models import F, Avg, Count
from rest_framework import serializers
from .models import Product, Lesson, UserProductAccess


class ProductSerializer(serializers.ModelSerializer):
    """Сериализатор для продукта"""

    start_date = serializers.DateTimeField(format="%Y.%m.%d %H:%M")
    lessons_count = serializers.IntegerField(source="lessons.count", read_only=True)

    class Meta:
        model = Product
        fields = ["id", "name", "price", "lessons_count", "start_date"]


class LessonSerializer(serializers.ModelSerializer):
    """Сериализатор для урока"""

    class Meta:
        model = Lesson
        fields = "__all__"


class ProductStatisticSerializer(serializers.ModelSerializer):
    """Сериализатор для статистики продукта"""

    pupils_count = serializers.SerializerMethodField()
    percentage_of_filling = serializers.SerializerMethodField()
    percentage_of_purchase = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "name",
            "pupils_count",
            "percentage_of_filling",
            "percentage_of_purchase",
        ]

    def get_pupils_count(self, obj):
        return UserProductAccess.objects.filter(product=obj).count()

    def get_percentage_of_filling(self, obj):
        avg_fullness = obj.groups.all().annotate(
            fullness=Count("pupils") * 100 / F("max_pupils")
        )
        return avg_fullness.aggregate(Avg("fullness"))

    def get_percentage_of_purchase(self, obj):
        users = User.objects.count()
        pupils_count = self.get_pupils_count(obj)
        return users * 100 / pupils_count if users != 0 else 0
