from django.shortcuts import render, HttpResponseRedirect, redirect, get_object_or_404
from . models import blog_data, category
from . forms import blog_data_form, category_form
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger

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
    return render(request, 'index.html', {'page': page, 'params': posts})



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
    if blog_data_detail:
        if request.method == 'POST':
            blog_data_detail.delete()
            return HttpResponseRedirect('/')
        return render(request, 'detail.html', {'params': blog_data_detail, 'id': post_id})
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