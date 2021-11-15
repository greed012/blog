from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from . models import blog_data, category, ip_filter, no_views
from . forms import blog_data_form, category_form
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from datetime import *

#index
def index(request):
    object_list = blog_data.objects.all().filter(status='published')
    paginator = Paginator(object_list, 4)  # 4 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', {'page': page, 'params': posts})

def drafts(request):
    object_list = blog_data.objects.all().filter(status='draft')
    paginator = Paginator(object_list, 4)  # 4 posts in each page
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    return render(request, 'draft.html', {'page': page, 'params': posts})



#Createpost
def create(request):
    category_data = category.objects.all()
    cat = []
    for i in category_data:
        cat.append(i.category_name)
    if request.method == 'POST':
        form = blog_data_form(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/')
    else:
        form = blog_data_form()
    return render(request, 'create.html',{'form':form,'cat':cat})

#Createpost
def edit(request, post_id=None):
    category_data = category.objects.all()
    cat = []
    for i in category_data:
        cat.append(i.category_name)

    item = get_object_or_404(blog_data, id=post_id)
    form = blog_data_form(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'create.html', {'form':form,'cat':cat})


def details_view(request,post_id):
    blog_data_detail = blog_data.objects.filter(id=post_id)
    no_view = no_views.objects.filter(post=blog_data(post_id))
    if blog_data_detail:

        def get_client_ip():
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            return ip

        def del_ip():
            object = ip_filter.objects.all()
            for i in object:
                today = date.today()
                if today-i.entered_date >= timedelta(days=5):
                    i.delete()

        del_ip()
        ip = get_client_ip()

        if ip_filter.objects.filter(post=blog_data(post_id), ip_address=ip).exists():
            print("this ip has already seen you need to wait atleast 5 days to add a count view")
        else:
            view_data = no_views.objects.filter(post=blog_data(post_id)).first()
            if view_data:
                view_data.views = view_data.views + 1
                view_data.save()
            else:
                view_data_obj = no_views(post=blog_data(post_id), views=1)
                view_data_obj.save()

            ip_add_obj = ip_filter(post=blog_data(post_id), ip_address=ip, entered_date=date.today())
            ip_add_obj.save()

        if request.method == 'POST':
            blog_data_detail.delete()
            return HttpResponseRedirect('/')
        return render(request, 'detail.html', {'params': blog_data_detail, 'id': post_id, 'views':no_view[0].views})
    else:
        raise Http404('Page Not Found')


def add_category(request):
    if request.method == 'POST':
        form = category_form(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/')
    else:
        form = category_form()
    return render(request, 'add_category.html', {'form': form})


def dashboard(request):
    return render(request,'dashboard.html')