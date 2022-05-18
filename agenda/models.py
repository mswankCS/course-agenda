from django.db import models

# Item object holds text, due month, and due day for an individual agenda item
class Item(models.Model):
    item_text = models.CharField(max_length = 255)
    item_due_month = models.IntegerField()
    item_due_day = models.IntegerField()

    #to string function
    def __str__(self):
        return self.item_text