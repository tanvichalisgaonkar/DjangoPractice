from django import template

register = template.Library()

@register.filter(name = 'cut')  # another method to register template using decorators.
def cut(value,arg):
	"""
	cut all value of arg from string
	"""
	return value.replace(arg,'')

# register.filter('cut',cut) # one method to register template.
