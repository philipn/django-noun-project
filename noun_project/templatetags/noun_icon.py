from lxml import etree
from classytags.core import Tag, Options
from classytags.arguments import Argument, MultiKeywordArgument
import slumber

from django import template

register = template.Library()


def resize(svg, size):
    if not size:
        return svg
    root = etree.fromstring(svg)
    for k, v in size.iteritems():
        root.attrib[k] = v
    return etree.tostring(root)


class NounIcon(Tag):
    name = 'noun_icon'
    options = Options(
        Argument('name', required=True, default='world'),
        MultiKeywordArgument('size', required=False,),
        'as',
        Argument('varname', required=False, resolve=False)
    )

    def render_tag(self, context, name, varname, size=None):
        icon = ''
        api = slumber.API("http://thenounproject.com")
        result = api.search.get(q=name)
        if result['msg'] == 'Success':
            # Grab the first icon for this noun.
            name = result['svg'].keys()[0]
            svg = result['svg'][name]
            icon = resize(svg, size)

        if varname:
            context[varname] = icon
            return ''
        return icon

register.tag(NounIcon)
