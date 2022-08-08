from tkinter.tix import Form


from django import forms
from tinymce.widgets import TinyMCE

from .models import Testo

class TestoForm(forms.ModelForm):
    form = Testo

    area = forms.CharField(widget=TinyMCE(attrs={'cols':30,"row":10}))
    
    
    class Meta:
        model=Testo
        fields = ["area"]