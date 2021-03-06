from django.db import models
from django.conf import settings

from projects.models import Project


class Issue(models.Model):

    TAG_CHOICES = [
        ("Bug", "Bug"),
        ("Improve", "Improve"),
        ("Task", "Task"),
    ]
    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Middle", "Middle"),
        ("High", "High"),
    ]
    STATUS_CHOICES = [
        ("To do", "To do"),
        ("In progress", "In progress"),
        ("Finished", "Finished"),
    ]

    title = models.CharField(max_length=128)
    description = models.CharField(max_length=250)
    tag = models.CharField(max_length=7, choices=TAG_CHOICES, default="Task")
    priority = models.CharField(max_length=6, choices=PRIORITY_CHOICES, default="Low")
    project = models.ForeignKey(
        to=Project, on_delete=models.CASCADE, blank=True, null=True
    )
    status = models.CharField(max_length=11, choices=STATUS_CHOICES, default="To do")
    author = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="author",
        blank=True,
        null=True,
    )
    assignee_user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="assignee_user",
        blank=True,
        null=True,
    )
    created_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"PROJECT : {self.project.title}, ISSUE : {self.title}, AUTHOR : {self.author}"
