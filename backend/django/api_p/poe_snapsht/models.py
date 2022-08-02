from django.db import models


class Accounts(models.Model):
    account_name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.account_name

class Characters(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    character = models.CharField(max_length=200)
    league = models.CharField(max_length=200)
    tracked = models.BooleanField()

    def __str__(self) -> str:
        return self.character

class SnapShots(models.Model):
    character_id = models.ForeignKey(Characters, on_delete=models.CASCADE)
    character_info = models.JSONField()
    items = models.JSONField()
    passives = models.JSONField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.character_id}:{self.time}'
