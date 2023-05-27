from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, DeleteView, UpdateView, CreateView, ListView, DetailView
from .models import Post, Category, Comment, Add_images
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse 
from django.http import HttpResponseRedirect
from django.http import FileResponse, Http404
from django.shortcuts import render, redirect
from album.models import Album
from .models import Neuigkeit, Live, Mitmachen


#def home(request):
#	return render(request, 'home.html', {})

#-------------------------- IndexView -------------------------------


class IndexView(ListView):
	model = Post
	neu = Neuigkeit
	live = Live
	collab = Mitmachen
	template_name = 'index.html'
	ordering = ['-post_date']
	ordering = ['-id']


	def get_context_data(self, *args, **kwargs):
		post = Post.objects.all()
		context = super(IndexView, self).get_context_data(*args, **kwargs)
		context["post"] = post
		ordering = ['-post_date']
		ordering = ['-id']


		#☺ listes sur les menus en haut-----------------
		cat_menu = Category.objects.all()
		context = super(IndexView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu


		neu_list = Neuigkeit.objects.all()
		context_002 = super(IndexView, self).get_context_data(*args, **kwargs)
		context_002["neu_list"] = neu_list
		ordering = ['-neu_date']
		ordering = ['-id']

		live_list = Live.objects.all()
		context_003 = super(IndexView, self).get_context_data(*args, **kwargs)
		context_003["live_list"] = live_list
		ordering = ['-live_date']
		ordering = ['-id']

		mitmachen_list = Mitmachen.objects.all()
		context_004 = super(IndexView, self).get_context_data(*args, **kwargs)
		context_004["mitmachen_list"] = mitmachen_list
		ordering = ['-mit_date']
		ordering = ['-id']

		return {
			"post": post, 
			"cat_menu": cat_menu, 
			"neu_list": neu_list, 
			"live_list": live_list, 
			"mitmachen_list": mitmachen_list 
		}

	


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


class Mitmachen(TemplateView):
	model = Mitmachen
	template_name = 'mitmachen.html'















