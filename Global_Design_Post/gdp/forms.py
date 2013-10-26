import re
from django import forms
from django.contrib.auth import authenticate,login
from django.forms import ModelForm
from models import Feed,Profile,Upload

class MyProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['username','email','occupation','homeIs','myHomeIsSetIn','profileAccess','style','designStyle','favoriteSpot','environment','favoriteDesigner','colors','place','interestingPerson','constantSource','music','books','childhoodHero','beautifulSeason','favoriteTime','favoriteEra','amBestKnown','likeToBestKnown','believeDesign','alert','profileImage','inspriringImage']
  


class RegistrationForm(forms.Form):
    userName = forms.CharField(label=u'Name:', max_length=30, widget = forms.TextInput(attrs={'class': 'span5',}))
    emailAddress = forms.EmailField(label=u'Email Address',max_length=80,widget = forms.TextInput(attrs={'class': 'span5',}))
    choosePassword = forms.CharField(
        label=u'Choose Password:',
        widget=forms.PasswordInput(attrs={'class': 'span5',})
    )
    repeatPassword = forms.CharField(
        label=u'Repeat Password:',
        widget=forms.PasswordInput(attrs={'class': 'span5',})
    )
    """def clean_userName(self):
    username = self.cleaned_data['userName'].strip()
    objUserManagementDA=UserManagementDA()
    if not re.search(r'^\w*\@*\.*\w*\@*\.*\w*\.*\w*$', username):
        raise forms.ValidationError('Username can only contain '
            'alphanumeric characters and the underscore.')
    try:
        objEmailExists =objUserManagementDA.checkExistingUsername(username,0)
        if objEmailExists == "username already exists":
            raise forms.ValidationError('Username already exists')
        elif objEmailExists == "No Error":
            return username
    except:

        raise forms.ValidationError('Username already exists')  """

    def clean_repeatPassword(self):
        if 'choosePassword' in self.cleaned_data:
            choosePassword = self.cleaned_data['choosePassword']
            repeatPassword = self.cleaned_data['repeatPassword']
            if choosePassword == repeatPassword:
                return repeatPassword
        raise forms.ValidationError('Passwords do not match.')


    """def clean_emailAddress(self):

        email = self.cleaned_data['emailAddress'].strip()
        objUserManagementDA=UserManagementDA()
        if email not in ('','None',None):
             try:
                 objEmailExists =objUserManagementDA.checkExistingEmail(email,0)
                 if objEmailExists == "Email id already exists":
                     return email
                 elif objEmailExists == "No Error":
                     raise forms.ValidationError("The email id doesn't have an account.")

             except:

                  raise forms.ValidationError("The email id doesn't have an account.")"""
    


from captcha.fields import ReCaptchaField   
 
class PasswordReCaptchaForm(RegistrationForm):
    captcha = ReCaptchaField(label=u'Name:',attrs={'theme' : 'clean'})
    
    


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
    
    

class FeedForm(ModelForm):
    class Meta:
        model = Feed    
    

class AddForm(ModelForm):
    class Meta:
        model = Upload        
        