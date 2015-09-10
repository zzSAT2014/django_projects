from django.views.generic import ListView
# from django.shortcuts import render
from models import Category


class CategoryIndex(ListView):
    model = Category
    template_name = 'sodagreen/category_index.html'
