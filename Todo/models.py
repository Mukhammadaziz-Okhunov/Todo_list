from django.db import models

class Todo(models.Model):
    s = (
        ("Yangi", "Yangi"),
        ("Bajarilgan", "Bajarilgan")
    )
    nom = models.CharField(max_length=50)
    batafsil = models.CharField(max_length=60)
    status = models.CharField(max_length=30, choices=s)
    vaqt = models.TimeField()

    def __str__(self):
        return f"{self.nom}, {self.batafsil},{self.vaqt}, {self.status}"