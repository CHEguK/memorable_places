''' memories/forms.py '''
from django import forms

from memories.models import MemoryItem


class MemoryItemForm(forms.ModelForm):
    ''' Memory Form '''
    class Meta:
        ''' Meta class '''
        model = MemoryItem
        fields = ('name', 'comment', 'coordinates', 'longitude', 'latitude')
        labels = {"name": "Название", "comment": "Комментарий"}
        widgets = {"comment": forms.Textarea(attrs={'rows': 5}),
                   "coordinates": forms.HiddenInput(),
                   "longitude": forms.HiddenInput(),
                   "latitude": forms.HiddenInput()}
