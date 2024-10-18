from django import forms
from .models import Question, Choice
from django.forms import DateInput

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']
class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']