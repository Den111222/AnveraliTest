from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    role = forms.ChoiceField(label='Role', choices=[('customer', 'Customer'), ('performer', 'Performer')])
    contact_info = forms.CharField(label='Contact Info', max_length=100)
    experience = forms.CharField(label='Experience', max_length=100)
    contact_name = forms.CharField(label='Contact Name', max_length=100)

