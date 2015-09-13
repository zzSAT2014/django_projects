from django.db import models
from django.utils import timezone
from tagging.fields import TagField


def roundup(fun):
    def inner(arg):
        return round(fun(arg), 1)
    return inner


class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return ('sodagreen:category', (), {'category': self.title})

    def __unicode__(self):
        return self.title

    @roundup
    def get_total(self):
        return sum([budget.amount for budget in self.budget_set.all()])

    @roundup
    def get_spent(self):
        return sum([budget.get_spent() for budget in self.budget_set.all()])

    @roundup
    def get_left(self):
        return sum([budget.get_left() for budget in self.budget_set.all()])


class Budget(models.Model):
    pub_date = models.DateTimeField(default=timezone.now)

    title = models.CharField(max_length=250, help_text='maxlength: 250 chars', default='test')
    amount = models.FloatField()
    category = models.ForeignKey(Category)
    slug = models.SlugField(unique_for_date='pub_date', default="")

    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title

    def get_year(self):
        return self.pub_date.year

    def get_absolute_url(self):
        return ('sodagreen:budget', (), {'title': self.title})

    @roundup
    def get_spent(self):
        return sum([entry.amount for entry in self.entry_set.all()])

    @roundup
    def get_left(self):
        return self.amount - self.get_spent()


class Entry(models.Model):
    title = models.CharField(max_length=250, help_text='maxlength: 250 chars', default='blank')
    amount = models.FloatField()

    tax_included = models.BooleanField()
    tax_rate = models.FloatField(default=1.08)
    slug = models.SlugField(unique_for_date='pub_date', default="")
    budget = models.ForeignKey(Budget, default=0)
    detail = models.TextField(blank=True)

    tag = TagField()
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-pub_date']

    def save(self):
        if not self.tax_included:
            self.amount = self.tax_rate * self.amount
            self.tax_included = True
        super(Entry, self).save()
