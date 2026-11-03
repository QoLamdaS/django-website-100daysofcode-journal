from django.db import models

class DayLog(models.Model):
    day_number = models.IntegerField(unique=True)
    title = models.CharField(max_length=200)
    date = models.DateField()
    description = models.TextField()
    project_link = models.URLField(blank=True, null=True)
    twitter_link = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['day_number']

    def __str__(self):
        return f"Day {self.day_number}: {self.title}"