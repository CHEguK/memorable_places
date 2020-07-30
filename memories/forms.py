''' memories/forms.py '''
from django import forms

from memories.models import MemoryItem


class MemoryItemForm(forms.ModelForm):
    ''' Memory Form '''
    class Meta:
        ''' Meta class '''
        model = MemoryItem
        fields = ('name', 'comment')
        labels = {"name": "Название", "comment": "Комментарий"}
        widgets = {"comment": forms.Textarea(attrs={'rows': 5})}
