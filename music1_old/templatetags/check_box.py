# templatetags/tag_library.py

from django import template

register = template.Library()

@register.filter(name='get_checkbox')
def get_checkbox(value):
   return '<input type="button" id="' + 'button' + value + '" name="' + 'fasta_control' + value + '"' + ' value= "Show Sequence"'  + '"'+  ' onclick="click_show_more(\''+ value + '\')"'


