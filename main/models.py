from django.db import models

NULLABLE = {'null': True, 'blank': True}

class Habbit(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(**NULLABLE)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="habbits"
    )
    place = models.CharField(max_length=100, **NULLABLE)
    action = models.CharField(max_length=100, **NULLABLE)
    healthy_habbit = models.BooleanField()
    linked_habbit = models.CharField(max_length=100, **NULLABLE)
    frequency = models.CharField(max_length=100, **NULLABLE)
    reward = models.CharField(max_length=100, **NULLABLE)
    time_to_do = models.TimeField(**NULLABLE)
    is_public = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
