from django import forms
from memories.models import MemoryItem


class MemoryItemForm(forms.ModelForm):
    class Meta:
        model = MemoryItem
        fields = ('name', 'comment')
        labels = {"name": "Название", "comment": "Комментарий"}