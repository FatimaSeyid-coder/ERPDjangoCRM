from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from apps.profil.models import Profile ,client ,clientpiste,message

# Sign Up Form
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2', 
            ]
        
        
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'location', 'birth_date','Profile_image')     
        
class ajoutForm(forms.ModelForm):
    class Meta:
        model=client
        fields = ('firstname', 'lastname', 'post','phone_number','email','siteweb','type','titre','etiquette')   
        

class clientpisteForm(forms.ModelForm):
    class Meta:
        model = message
        fields = fields = ['lastname', 'firstname', 'email', 'phone_number', 'msg']
    lastname = forms.CharField(max_length=100)
    firstname = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone_number=forms.CharField(max_length=100)
    def save(self, commit=True):
        clientpiste_obj= clientpiste.objects.create(
            lastname =self.cleaned_data['lastname'],
            firstname =self.cleaned_data['firstname'],
            phone_number =self.cleaned_data['phone_number'],
            email=self.cleaned_data['email']
        )
        message = super().save(commit=False)
        message.clientpiste = clientpiste_obj
        if commit:
            message.save()
        return message

class MessageForm(forms.Form):
    body = forms.CharField(label='Message', widget=forms.Textarea(attrs={'rows': 3}))