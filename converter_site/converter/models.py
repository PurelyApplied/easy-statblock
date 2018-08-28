from django.db.models import TextField, Model


class Creature(Model):
    yaml = TextField(max_length=8192)
