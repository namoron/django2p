from django import forms


class NippoFormClass(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Texarea())
