from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from .models import UserProductAccess, Group


@receiver(post_save, sender=UserProductAccess)
def handle_user_product_access(sender, instance, created, **kwargs):
    if created:
        product = instance.product
        groups = Group.objects.filter(product=product)
        print(f"The group update signal for the {product.name} was triggered")
        update_group_membership(instance, groups)
        adjust_group_students(instance, groups)


def update_group_membership(instance, groups):
    for group in groups:
        pupils_count = group.pupils.count()
        if pupils_count < group.max_pupils:
            group.pupils.add(instance.pupil)
            print(f"The pupil {instance.pupil} has been added to the {group.name}.")


def adjust_group_students(instance, groups):
    if instance.product.start_date > timezone.now():
        total_pupils = sum([group.pupils.count() for group in groups])
        avg_pupils_per_group = total_pupils // len(groups)
        for group in groups:
            pupils_count = group.pupils.count()
            if pupils_count > avg_pupils_per_group + 1:
                group.students.remove(instance.pupil)
                print(
                    f"The pupil {instance.pupil} has been deleted from the {group.name}."
                )
            elif pupils_count < avg_pupils_per_group - 1:
                group.pupils.add(instance.pupil)
                print(f"The pupil {instance.pupil} has been added to the {group.name}.")
                break
