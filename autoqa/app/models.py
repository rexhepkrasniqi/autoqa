from django.db import models

# Create your models here.

class Task(models.Model):
    STATUS_CHOICES = [
        ("success", "Success"),
        ("failed", "Failed"),
        ("unknown", "Unknown"),
    ]

    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default="unknown")
    modified = models.DateTimeField(auto_now=True, blank=True)

    message = models.CharField(max_length=300, blank=True, null=True)
    screenshot = models.ImageField(upload_to="media/", null=True, blank=True)

    def __str__(self):
        return self.name


class Action(models.Model):
    name = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return str(self.name)


class Step(models.Model):
    task = models.ForeignKey(
        "Task",
        on_delete=models.DO_NOTHING,
    )
    action = models.ForeignKey(
        "Action",
        on_delete=models.DO_NOTHING,
    )
    order = models.IntegerField(blank=True)
    target = models.CharField(max_length=100, blank=True, null=True)
