from django import forms
from django.contrib.auth.models import User

from .models import Article
from .models import Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'content', 'photo',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
        widgets = {
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }


class CreateUserForm(forms.Form):
    username = forms.CharField(max_length=30)
    password1 = forms.CharField(max_length=30, widget=forms.PasswordInput())
    password2 = forms.CharField(max_length=30, widget=forms.PasswordInput())
    email = forms.EmailField(required=True)

    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']

        raise forms.ValidationError("this user exist already")

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("passwords don't match each other")

        return self.cleaned_data

    def save(self):
        new_user = User.objects.create_user(username=self.cleaned_data['username'],
                                            password=self.cleaned_data['password1'],
                                            email=self.cleaned_data['email'],
                                            )

        return new_user
