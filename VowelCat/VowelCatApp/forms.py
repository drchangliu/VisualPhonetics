from django import forms
from models import MyUser
from django.forms.widgets import RadioSelect
from PIL import Image

class MyRegistrationForm(forms.ModelForm):
    """
    Form for registering a new account.
    """
    GENDER_CHOICES = (
        ('M', 'Male'), 
        ('F', 'Female'),
    )
    email = forms.EmailField(widget=forms.EmailInput,label="Email")
    date_of_birth = forms.DateField(widget=forms.DateInput(format='%m/%d/%Y'), label="Date of birth (MM/DD/YYYY)")
    gender = forms.ChoiceField(widget=RadioSelect, choices=GENDER_CHOICES, label="Gender")
    password1 = forms.CharField(widget=forms.PasswordInput,
                                label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput,
                                label="Password (again)")

    class Meta:
        model = MyUser
        fields = ['email', 'date_of_birth', 'gender', 'password1', 'password2']

    def clean(self):
        """
        Verifies that the values entered into the password fields match

        NOTE: Errors here will appear in ``non_field_errors()`` because it applies to more than one field.
        """
        cleaned_data = super(MyRegistrationForm, self).clean()
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again.")
        return self.cleaned_data

    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
	user.set_adult()
        if commit:
            user.save()
        return user

class MyChangeForm(forms.ModelForm):
    """
    Form for editing an account.
    """

    first_name = forms.CharField(widget=forms.TextInput, label="First name")
    last_name = forms.CharField(widget=forms.TextInput, label="Last name")
    avatar = forms.ImageField(label="Profile picture")

    def __init__(self, *args, **kwargs):
	super(MyChangeForm, self).__init__(*args, **kwargs)
        for key in self.fields:
	    self.fields[key].required = False

    class Meta:
        model = MyUser
        fields = ['first_name', 'last_name', 'avatar']

    def save(self, commit=True):
        user = super(MyChangeForm, self).save(commit=False)
        if commit:
            user.save()
        return user

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        try:
            w, h = Image.image(avatar).size

            #validate dimensions
            max_width = max_height = 100
            if w > max_width or h > max_height:
                raise forms.ValidationError(
                    u'Please use an image that is '
                     '%s x %s pixels or smaller.' % (max_width, max_height))

            #validate content type
            main, sub = avatar.content_type.split('/')
            if not (main == 'image' and sub in ['jpeg', 'pjpeg', 'png']):
                raise forms.ValidationError(u'Please use a JPEG, '
                    'or PNG image.')

          #validate file size
            if len(avatar) > (20 * 1024):
                raise forms.ValidationError(
                    u'Avatar file size may not exceed 20k.')

        except AttributeError:
            """
            Handles case when we are updating the user profile
            and do not supply a new avatar
            """
            pass

        has_picture = True
        return avatar
