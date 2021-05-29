from django import forms
from .models import Task, User

class SignUpForm(forms.ModelForm):
    def save(self,commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.set_password(self.cleaned_data.get('password'))
        if commit:
            user.save()
        return user
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = [{'password':forms.PasswordInput}]

class SignInForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)


class TaskForm(forms.ModelForm):
    task_title = forms.CharField(required=True, min_length=10, max_length=20)
    task_description = forms.CharField(required=False)
    task_pic = forms.ImageField(required=False)
    class Meta:
        model = Task
        fields = ('task_title', 'task_description', 'task_pic')