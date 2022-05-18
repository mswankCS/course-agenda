from django.db import models

class Item(models.Model):
    item_text = models.CharField(max_length = 255)
    item_due_month = models.IntegerField()
    item_due_day = models.IntegerField()