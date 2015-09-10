from django.shortcuts import render, get_object_or_404
from models import Entry, Link, Category
from django.views.generic import DateDetailView, ListView, DetailView
from tagging.models import Tag, TaggedItem
from django.views.generic.dates import YearArchiveView, MonthArchiveView
import calendar

# entries


def index(request):
    # print "inside views.index"
    return render(request, 'coltrane/entry_index.html', {'object_list': Entry.objects.all()})


class EntryDetail(DateDetailView):
    model = Entry
    date_field = 'pub_date'
    # context_object_name = 'entry'
    template_name = 'coltrane/entry_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EntryDetail, self).get_context_data(**kwargs)
        myentry = context['entry']
        if myentry.tags:
            context['tags'] = map(lambda a: a.strip, myentry.tags.split(","))
        return context


class EntryYearArchive(YearArchiveView):
    model = Entry
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
    template_name = 'coltrane/entry_archive_year.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EntryYearArchive, self).get_context_data(**kwargs)
        month_lis = {}
        # print kwargs
        all_objs = Entry.live.all().filter(pub_date__year=kwargs['date_list'][0].year)
        # print "all objects used %s" % (all_objs)
        month_lis = []
        for m in range(1, 13):
            curmonth = all_objs.filter(pub_date__month=m)
            tup = (calendar.month_name[m], curmonth)
            if curmonth:
                month_lis.append(tup)
        context['month_lis'] = month_lis
        context['myyear'] = str(kwargs['date_list'][0].year)
        # print context['yearfuck']
        return context


class EntryMonthArchive(MonthArchiveView):
    queryset = Entry.objects.all()
    date_field = "pub_date"
    make_object_list = True
    allow_future = True
    template_name = 'coltrane/entry_index.html'

    def get_context_data(self, *args, **kwargs):
        context = super(EntryMonthArchive, self).get_context_data(**kwargs)
        context['special_title'] = kwargs['date_list'][0].strftime("%b,%Y")
        print context
        return context

# link_set


class LinkIndex(ListView):
    model = Link
    template_name = 'coltrane/link_list.html'


class LinkDetail(DateDetailView):
    model = Link
    date_field = 'pub_date'
    template_name = 'coltrane/link_detail.html'


# categories


class CategoryIndex(ListView):
    model = Category
    template_name = 'coltrane/url_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryIndex, self).get_context_data(**kwargs)
        context['special_title'] = "Category Index"
        return context


class CategoryDetail(DetailView):
    model = Category
    template_name = "coltrane/entry_index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(CategoryDetail, self).get_context_data(**kwargs)
        # print context

        category = context[u'object']
        context['object_list'] = category.entry_set.all()
        context['special_title'] = 'Entries for %s' % (category.title)
        # print context
        return context

# tags


class TagIndex(ListView):
    queryset = Tag.objects.all()
    template_name = 'coltrane/tag_index.html'


def tag_detail_view(request, name):
    tag = get_object_or_404(Tag, name=name)
    context = {}
    context['tag_name'] = name
    context['entry_set'] = TaggedItem.objects.get_by_model(Entry, tag)
    context['link_set'] = TaggedItem.objects.get_by_model(Link, tag)
    print context
    return render(request, "coltrane/tag_detail.html", context)

