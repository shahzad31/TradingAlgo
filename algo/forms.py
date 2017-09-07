from django import forms


class AlgoInfoForm(forms.Form):
    name = forms.CharField(max_length=100)
    ticker = forms.EmailField(max_length=100)
    trade = forms.CharField(max_length=1000)
    signal = forms.CharField(max_length=1000)