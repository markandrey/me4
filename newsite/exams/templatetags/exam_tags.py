from django import template
from exams.utils import cats_db


register = template.Library()


@register.simple_tag(name='getcats')
def get_cats_exams():
    return cats_db


@register.inclusion_tag('exams/list_categories.html')
def show_categories(cat_selected=0):
    cats = cats_db
    return {'cats': cats, 'cat_selected': cat_selected}
