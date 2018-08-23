from django.db.models import TextField, Model


class Creature(Model):
    input_text = TextField(max_length=8192)
    output_text = TextField(max_length=8192)

