from django import forms

from .models import List


class AddListForm(forms.ModelForm):
    class Meta:
        model = List
        fields = ["name", "colour", "icon"]
        widgets = {
            "colour": forms.RadioSelect,
            "icon": forms.RadioSelect,
        }
