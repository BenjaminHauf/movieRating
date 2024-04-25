# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User

# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#         labels = {
#             'username': '',
#             'email': '',
#             'password1': '',
#             'password2': '',
#         }
#         widgets = {
#             'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
#             'email': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Email'}),
#             'password1': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Password'}),
#             'password2': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
#         }
