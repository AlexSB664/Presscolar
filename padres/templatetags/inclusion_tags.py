from django import template
from alumnos.models import alumnos
from padres.models import Tutor
from django.contrib.auth.models import User
from padres import views

register = template.Library()

@register.filter
def get_at_index(list,index):
	data = list.index(index)
	return data

@register.filter
def get_data(list, index):
	return list[index]

class AssignNode(template.Node):
	"""docstring for AssignNode"""
	def __init__(self, name, value):
		self.name = name
		self.value = value
	
	def render(self, context):
		context[self.name]	= self.value.resolve(context, True)
		return ''

def do_assign(parser, token):
	bits = token.content.split()
	if len(bits) != 3:
		raise template.TemplateSyntaxError("'%s' tag takes two arguments" %bits[0])

	value = parser.compile_filter(bits[2])
	return AssignNode(bits[1], value)

register.tag('assign', do_assign)