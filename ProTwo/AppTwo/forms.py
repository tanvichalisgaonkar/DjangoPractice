from django import forms
from AppTwo.models import UserInfo


class SignUpForm(forms.ModelForm):
 	"""docstring for SignUpForm"""
 	class Meta:
 		model = UserInfo
 		fields = "__all__"
