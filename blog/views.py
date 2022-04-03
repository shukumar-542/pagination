from pyexpat import model
from django.shortcuts import render
from django.core.paginator import Paginator
from blog.models import blog
from django.views.generic import ListView,DetailView
from django.http import Http404

# Create your views here.

#### FUNCTION BASED PAGINATOR

# def home(request):
#       blogs = blog.objects.all().order_by('id')
#       paginator = Paginator(blogs,3,orphans=1)
#       page_number = request.GET.get('page')
#       page_obj = paginator.get_page(page_number)
#       return render(request,'blog/home.html',{'page_obj':page_obj}) 


##### CLASS BASED PAGINATOR

class postlistview(ListView):
      model = blog
      template_name = 'blog/home.html'
      ordering= ['id']
      paginate_by= 3


      def get_context_data(self,*args, **kwargs):
            try:
                  return super(postlistview, self).get_context_data(*args, **kwargs)
            except Http404 :
                  self.kwargs['page'] =1
                  return super(postlistview, self).get_context_data(*args, **kwargs)

class postdetailview(DetailView):
      model = blog
      template_name ='blog/detail.html'

