from django import template
from ..models import blog_data

register = template.Library()

@register.simple_tag
def total_posts():
    return blog_data.objects.count()

@register.inclusion_tag('latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = blog_data.objects.filter(status='published').order_by('-published_date')[:count]
    return {'latest_posts': latest_posts}

