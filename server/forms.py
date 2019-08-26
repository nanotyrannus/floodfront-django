from django import forms

class UploadedFileForm(forms.Form):
    image = forms.ImageField()
    marker_id = forms.IntegerField()