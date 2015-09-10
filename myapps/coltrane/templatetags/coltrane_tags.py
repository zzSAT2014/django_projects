from django import template
from coltrane.models import Entry
from django.apps import apps


class LatestEntriesNode(template.Node):
    def render(self, context):
        context['latest_entries'] = Entry.objects.all()[:5]
        return ''


def do_latest_entries(parser, token):
    return LatestEntriesNode()


register = template.Library()
register.tag('get_latest_entries', do_latest_entries)


# example tag {%get_latest_content coltrane.entry 5 as latest_entry%}""

def do_latest_content(parser, token):
    info = token.split_contents()
    if len(info) != 5:
        raise template.TemplateSyntaxError("Exactly for arguments are required")
    mymodel_lis = info[1].split('.')
    if len(mymodel_lis) != 2:
        raise template.TemplateSyntaxError("invalid model systax")
    mymodel = apps.get_model(*mymodel_lis)
    if mymodel is None:
        raise template.TemplateSyntaxError("defined model does not exists")
    return LatestContentNode(mymodel, int(info[2]), info[4])


class LatestContentNode(template.Node):

    def __init__(self, mymodel, num, contextname):
        self.mymodel = mymodel
        self.num = num
        self.contextname = contextname

    def render(self, context):
        context[self.contextname] = self.mymodel._default_manager.all()[:self.num]

        return ''

register.tag('get_latest_content', do_latest_content)
