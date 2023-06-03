from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DeleteView, UpdateView, CreateView, ListView, DetailView
from .models import Post, Category, Comment, Add_images
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse 
from django.http import HttpResponseRedirect
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect
from album.models import Album
from .models import Neuigkeit, Live, Mitmachen, Mitmachen_index
from datetime import datetime, date
from .forms import NeuigkeitForm, LiveForm, Mitmachen_indexForm


#def home(request):
#	return render(request, 'home.html', {})

#-------------------------- IndexView -------------------------------


def IndexView(request):
	post = Post.objects.all()
	ordering = ['-post_date']
	ordering = ['-id']

	neu = Neuigkeit.objects.all()
	ordering = ['-id']

	live = Live.objects.all()
	ordering = ['-live_date']
	ordering = ['-id']

	sei = Mitmachen_index.objects.all()
	ordering = ['-mit_date']
	ordering = ['-id']

	return render(request, 'index.html',
	 	{
	 		'post': post, 
	 		'neu': neu,
	 		'live': live,
	 		'sei': sei

	 		}
	 )


class AddNeuigkeitView(CreateView):
	model = Neuigkeit
	form_class = NeuigkeitForm  
	template_name = 'add_neuigkeit.html'
	#fields = '__all__'             On désactive ces deux-là => form_class.
	#fields = ('title', 'body')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddNeuigkeitView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context
	success_url = reverse_lazy('index')


class AddLiveView(CreateView):
	model = Live
	form_class = LiveForm  
	template_name = 'add_live.html'
	#fields = '__all__'             On désactive ces deux-là => form_class.
	#fields = ('title', 'body')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddLiveView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context
	success_url = reverse_lazy('index')

class AddMitmachen_indexView(CreateView):
	model = Mitmachen_index 
	form_class = Mitmachen_indexForm  
	template_name = 'add_mitmachen_index.html'
	#fields = '__all__'             On désactive ces deux-là => form_class.
	#fields = ('title', 'body')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddMitmachen_indexView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context
	success_url = reverse_lazy('index')


#-------------------------- End IndexView -----------------------------

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__'

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)

	success_url = reverse_lazy('home')



def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else:
		post.likes.add(request.user)
		liked = True
	
	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))



class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-post_date']
	ordering = ['-id']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

		

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'cat_menu_list': cat_menu_list})



def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-', ' '))
	return render(request, 'categories.html', {'cats': cats.title().replace('-', ' '), 'category_posts': category_posts})


	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(CategoryView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id):
			liked = True

		context["cat_menu"] = cat_menu
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context



class AddPostView(CreateView):
	model = Post
	form_class = PostForm  
	template_name = 'add_post.html'
	#fields = '__all__'             On désactive ces deux-là => form_class.
	#fields = ('title', 'body')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddPostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class UpdatePostView(UpdateView):
	model = Post 
	template_name = 'update_post.html'
	form_class = EditForm  

	#fields = ['title', 'author', 'body']


class AddCategoryView(CreateView):
	model = Category 
	template_name = 'add_category.html'
	fields = '__all__'
	#fields = ['title', 'author', 'body']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context


class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'

	success_url = reverse_lazy('home')


class Add_Images(TemplateView):
	model = Add_images
	template_name = "add_images.html"
	fields = '__all__'

class Mitmachen(TemplateView):
	model = Mitmachen
	template_name = 'mitmachen.html'

"""
	def post(self, *args, **kwargs):
		try:
			images = self.request.FILES.getlist('images')

			for image in images:
				post_images = Add_images.objects.create(
						images = image

					)
			return redirect('home')
		except ValueError as e:
			print(e)
		
		except images.DoesNotExist as e:
			print(e)
		"""

def Unterstutzen(request):
	context = {}
	return render(request, 'unterstutzen.html', context)


def uber_uns(request):
	context = {}
	return render(request, 'uber_uns.html', context)

















