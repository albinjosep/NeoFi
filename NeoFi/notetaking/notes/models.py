# notes/models.py
from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    shared_with = models.ManyToManyField(User, related_name='shared_notes', blank=True)

    def __str__(self):
        return self.title

class NoteHistory(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    version = models.PositiveIntegerField()
    content = models.TextField()

    def __str__(self):
        return f"{self.note.title} - Version {self.version}"
