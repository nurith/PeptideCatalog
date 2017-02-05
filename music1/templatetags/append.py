# templatetags/tag_library.py

from django import template

register = template.Library()

@register.filter(name='get_href')
def get_href(value):
    value=value[0:6]
    return '<a href="http://www.uniprot.org/uniprot/' + value + '" target="_blank">'+ value +'</a>'

@register.filter(name='get_detail')
def get_detail(value):
       return '<input type="button" id="' + 'button' + value + '" name="' + 'entry_control' + value + '"' + ' value= '  + value+ ''+  ' onclick="show_entry(\''+ value + '\')"'






