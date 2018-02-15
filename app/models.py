from django.contrib.auth.models import User
from django.db import models


class Asset(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='asset_owner')
    member = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'asset'


class Bug(models.Model):
    title = models.CharField(max_length=200)
    addedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'bug'
