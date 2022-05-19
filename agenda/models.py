from tkinter import END
from django.db import models

END_OF_SEMESTER_DATE = '2000-01-01'

# Item object holds text, due month, and due day for an individual agenda item
class Item(models.Model):
    text = models.CharField(max_length = 255)
    due_date = models.DateField(default=END_OF_SEMESTER_DATE)

    #to string function
    def __str__(self):
        return self.text