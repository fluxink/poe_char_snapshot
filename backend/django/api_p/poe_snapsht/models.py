from django.db import models


class Accounts(models.Model):
    account_name = models.CharField(max_length=200)

class Characters(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    character = models.CharField(max_length=200)
    league = models.CharField(max_length=200)
    tracked = models.BooleanField()

class SnapShots(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    character_info = models.JSONField()
    items = models.JSONField()
    passives = models.JSONField()
    time = models.DateTimeField(auto_now_add=True)
