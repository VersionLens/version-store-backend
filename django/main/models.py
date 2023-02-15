from django.db import models as m
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location="media")


class Product(m.Model):
    name = m.CharField(max_length=50)
    price = m.PositiveSmallIntegerField()
    image = m.FileField(storage=fs)
