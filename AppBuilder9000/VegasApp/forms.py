from django.forms import ModelForm
from .models import User, Activities, VegasTemp, VegasNews


# Creating User Form Class
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class ActivityForm(ModelForm):
    class Meta:
        model = Activities
        fields = '__all__'


class VegasTempForm(ModelForm):
    class Meta:
        model = VegasTemp
        fields = '__all__'


class VegasNewsForm(ModelForm):
    class Meta:
        model = VegasNews
        fields = '__all__'
