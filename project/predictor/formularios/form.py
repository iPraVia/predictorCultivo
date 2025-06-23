from django import forms

class FormSuelo(forms.Form):
    nitrogeno = forms.CharField(label='nitrogeno')
    fosforo = forms.CharField(label='fosforo')
    potasio = forms.CharField(label='potasio')
    ph = forms.CharField(label='ph')
    temperatura = forms.CharField(label='temperatura')
    humedad = forms.CharField(label='humedad')
    lluvia = forms.CharField(label='lluvia')