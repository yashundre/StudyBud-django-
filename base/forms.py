from importlib.abc import ExecutionLoader
from django.forms import ModelForm
from .models import Room,User


class RoomForm(ModelForm):
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host','participants']