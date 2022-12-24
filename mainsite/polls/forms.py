from django import forms
from captcha.fields import ReCaptchaField

class MyForm(forms.Form):
    captcha = ReCaptchaField()