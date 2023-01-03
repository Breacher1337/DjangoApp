from django import forms
from django.forms.utils import ErrorList
from captcha.fields import ReCaptchaField
class QuestionForm(forms.Form):

    question_text = forms.CharField(label="Question Text", max_length=200, required=True)
    captcha = ReCaptchaField()


class MyErrorList(ErrorList):
    ErrorList = ErrorList(error_class="bading")
    ErrorList.error_class = "errorlist test"
