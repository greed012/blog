from django import template
from ..models import blog_data, no_views

register = template.Library()

@register.simple_tag
def total_posts():
    return blog_data.objects.count()

@register.inclusion_tag('latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = blog_data.objects.filter(status='published').order_by('-published_date')[:count]
    return {'latest_posts': latest_posts}

@register.inclusion_tag('popular_posts.html')
def show_popular_posts(count=5):
    popular_posts = blog_data.objects.filter(status='published').order_by('-no_views')[:count]
    return {'popular_posts': popular_posts}

@register.inclusion_tag('dashboard.html')
def dashboard():
    pass
