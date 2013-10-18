import re
from django import forms

class RegistrationForm(forms.Form):
    userName = forms.CharField(label=u'Username:', max_length=30,widget = forms.TextInput(attrs={'class': 'span3',}))
    emailAddress = forms.EmailField(label=u'Email Address',max_length=80,widget = forms.TextInput(attrs={'class': 'span3',}))
    choosePassword = forms.CharField(
        label=u'Choose Password:',
        widget=forms.PasswordInput(attrs={'class': 'span3',})
    )
    repeatPassword = forms.CharField(
        label=u'Repeat Password:',
        widget=forms.PasswordInput(attrs={'class': 'span3',})
    )



    def clean_repeatPassword(self):
        if 'choosePassword' in self.cleaned_data:
            choosePassword = self.cleaned_data['choosePassword']
            repeatPassword = self.cleaned_data['repeatPassword']
            if choosePassword == repeatPassword:
                return repeatPassword
        raise forms.ValidationError('Passwords do not match.')


class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()

class RequestPasswordForm(forms.Form):
    emailAddress = forms.EmailField(label=u'Email Address')

    def clean_emailAddress(self):

        email = self.cleaned_data['emailAddress'].strip()

        if email not in ('','None',None):

            try:

                objEmailExists =''#
                if objEmailExists == "Email id already exists":
                    return email
                elif objEmailExists == "No Error":
                    raise forms.ValidationError("The email id doesn't have an account.")

            except:

                raise forms.ValidationError("The email id doesn't have an account.")


class ResetPasswordForm(forms.Form):
    userName = forms.CharField(label=u'Username:', max_length=30,widget = forms.TextInput(attrs={'class': 'span8',}))
    choosePassword = forms.CharField(
        label=u'Choose Password:',
        widget=forms.PasswordInput(attrs={'class': 'span8',})
    )
    repeatPassword = forms.CharField(
        label=u'Repeat Password:',
        widget=forms.PasswordInput(attrs={'class': 'span8',})
    )

    def clean_repeatPassword(self):
        if 'choosePassword' in self.cleaned_data:
            choosePassword = self.cleaned_data['choosePassword']
            repeatPassword = self.cleaned_data['repeatPassword']
            if choosePassword == repeatPassword:
                return repeatPassword
        raise forms.ValidationError('Passwords do not match.')