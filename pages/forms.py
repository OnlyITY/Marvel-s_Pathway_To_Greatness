from django.contrib.auth.forms import UserCreationForm
from django import forms
from pages.models import Users


class RegistrationForm(UserCreationForm):
    """docstring for RegistrationForm"""
    user_email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    city = forms.CharField(max_length=255, required=True)
    state = forms.CharField(max_length=255, required=True)
    zipcode = forms.IntegerField()

    class Meta:  # define a metadata related to this class
        model = Users
        fields = (
            'username',
            'user_email',
            'first_name',
            'last_name',
            'city',
            'state',
            'zipcode'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.user_email = self.cleaned_data['user_email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.city = self.cleaned_data['city']
        user.state = self.cleaned_data['state']
        user.zipcode = self.cleaned_data['zipcode']

        if commit:
            user.save()  # running sql in database to store data
        return user
