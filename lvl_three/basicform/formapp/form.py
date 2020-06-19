from django import forms
from django.core import validators
 
# def check_for_z(value):
# 	"""
# 	check wether passed valued with z or not
# 	function can be called from any form field validation option. 
# 	"""
# # 	if value[0].lower() != 'z':
# # 		raise forms.ValidationError("Name Needs to start with Z")



class FormName(forms.Form):
	"""docstring for FormName"""
	name = forms.CharField()
	email = forms.EmailField()
	verify_email = forms.EmailField(label = 'Re enter the email')
	text = forms.CharField(widget = forms.Textarea)
	botcatcher = forms.CharField(required = False,
		widget = forms.HiddenInput,
		validators = [validators.MaxLengthValidator(0)])

	def clean(self):
		all_clean_data = super().clean()
		email = all_clean_data['email']
		vmail = all_clean_data['verify_email']
		if email != vmail:
			raise forms.ValidationError("Make Sure Email matches")
	# def clean_botcatcher(self):
	# 	botcatcher = self.cleaned_data['botcatcher']
	# 	if len(botcatcher) > 0:
	# 		raise forms.ValidationError("GOTCHA BOT!")
	# 	return botcatcher
	
 	