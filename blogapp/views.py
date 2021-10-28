from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from . models import blog_data
from . forms import blog_data_form
#index
def index(request):
    blog_coontent = blog_data.objects.all()
    blog_cont_list = []
    for i in blog_coontent:
        i_data = [i.id,i.title,i.published_date,i.author,i.body]
        blog_cont_list.append(i_data)
    return render(request,'index.html',{'params':blog_cont_list})


#Createpost
def create(request):
    if request.method == 'POST':
        form = blog_data_form(request.POST)
        if form.is_valid():
            post_item = form.save(commit=False)
            post_item.save()
            return redirect('/')
    else:
        form = blog_data_form()
    return render(request, 'create.html',{'form':form})

#Createpost
def edit(request, post_id=None):
    item = get_object_or_404(blog_data, id=post_id)
    form = blog_data_form(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'create.html', {'form':form})


def details_view(request,post_id):
    blog_data_detail = blog_data.objects.filter(id=post_id)
    blog_cont_list = []
    for i in blog_data_detail:
        i_data = [i.title, i.published_date, i.author, i.body]
        blog_cont_list.append(i_data)

    return render(request,'detail.html',{'params':blog_cont_list,'id':post_id})
