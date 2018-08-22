from django.db import models


class Creature(models.Model):
    arbitrary_yaml_text = models.CharField(max_length=8192)


class GeneratedStatblock(models.Model):
    parsed_yaml_stuff = models.CharField(max_length=8192)
    output = models.CharField(max_length=8192)
