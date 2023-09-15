from slugify import slugify
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from datetime import datetime


from stories.models import Recipe

@receiver(post_save, sender=Recipe)
def recipe_post(sender, instance, created, **kwargs):
    replacements=['a', 'e']
    if created:
        instance.slug = slugify(instance.title, replacements=[replacements]) + datetime.utcnow().strftime('%Y-%m-%d-%H-%M-%S-%f')
        print(instance.slug)
        instance.save()


# @receiver(pre_save, sender=Recipe)
# def recipe_save(sender, instance, **kwargs):
#     replacements=['a', 'e']
#     instance.slug = slugify(instance.title, replacements=replacements)
#     instance.save()
    