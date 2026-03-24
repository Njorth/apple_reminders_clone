from django import forms

from .models import List


class AddListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["name", "colour"]
        widgets = {
            "colour": forms.RadioSelect,
        }
