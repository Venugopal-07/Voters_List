from django.db import models

class Voter(models.Model):
    voter_name = models.CharField(max_length=100)
    voter_age = models.IntegerField()
    def _str_(self):
        return self.name