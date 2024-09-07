from django import forms
from .models import Task, Tag
from crispy_forms.helper import FormHelper


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['content', 'deadline', 'priority', 'tags', 'is_done']

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
