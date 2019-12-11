from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post, Comment
from blog.forms import PostForm, CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    TemplateView, ListView, DetailView,
    CreateView, UpdateView, DeleteView)

#################################################################
####################### Class-based views #######################
#################################################################

class AboutView(TemplateView):

    # when asked for AboutView in urls.py, render about.html
    template_name = 'about.html'


class PostListView(ListView):

    model = Post

    def get_queryset(self):
        """
        Query all of the Post objects ordered by published date before
        returning them when PostListView is called.
            > __lte is the condition (less than or equal to)
            > -published_date means the most recent one first (-)
        """

        return Post.objects\
                .filter(publish_date__lte=timezone.now())\
                .order_by('-publish_date')


class PostDetailView(DetailView):

    model = Post


class CreatePostView(CreateView, LoginRequiredMixin):
    """
    LoginRequiredMixin is a class CreatePostView inherits from
    that does the same as @login_required decorator. That means
    only people who are logged in will access this class and its
    form version to create a post
    """

    # if not logged in and they call this View, redirect to /login
    login_url = '/login/'

    # if logged in and they call this View, redirect to /post_detail
    redirect_field_name = 'blog/post_detail.html'

    # The form to create the post (form_class) is PostForm
    form_class = PostForm

    model = Post


class PostUpdateView(UpdateView, LoginRequiredMixin):

    login_url = '/login/'

    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post


class PostDeleteView(DeleteView, LoginRequiredMixin):

    model = Post

    # WAIT for it to be deleted, and THEN redirect to home page
    success_url = reverse_lazy('post_list')


class DraftListView(ListView, LoginRequiredMixin):
    """
    This is essentialy the same as PostListView but NOT with the
    published_posts filter as before. In this casewhen this view is
    called, it will redirect to post_list.html with all post objects
    that are YET TO BE PUBLISHED (or drafted)
        > published_date__isnull=True
    """

    login_url = '/login/'

    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_queryset(self):
        """ get all drafted posts (not published yet) """

        return Post.objects\
                .filter(publish_date__isnull=True)\
                .order_by('create_date')


##################################################################
###################### Function-based views ######################
##################################################################

@login_required
def post_publish(request, pk):

    post = get_object_or_404(Post, pk=pk)

    # call the publish method in the post object, which saves the
    # published time and saves it.
    post = post.publish()

    # redirect to its details
    return redirect('post_detail', pk=pk)


# @login_required
def add_comment_to_post(request, pk):

    # try to fetch the Post object with the PK as the ID
    post = get_object_or_404(Post, pk=pk)

    # if the comment is being submitted
    if request.method == 'POST':

        # create a form object with the comment's posted data
        form = CommentForm(request.POST)

        if form.is_valid():

            comment = form.save(commit=False)

            # connect the comment to the fetched Post object
            comment.post = post

            # commit the save now
            comment.save()

            # redirect to post_detail.html with the pk of the
            # Post object
            return redirect('post_detail', pk=post.pk)

    # if a comment is not being submitted
    else:

        # create an empty comment form object to submit one
        form = CommentForm()

    # and render comment_form.html with that object as a context
    # dictionary
    return render(request, 'blog/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):

    # get the Comment object
    comment = get_object_or_404(Comment, pk=pk)

    # call its approve() method, which sets aprroved_comment to True
    comment.approve()

    # redirect to post_detail.html. Note that the comment object
    # already has a post object linked to it by the add_comment_to_post
    # function-based view, so we need to set its key as a pk to get to
    # the respective Post's page.
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):

    comment = get_object_or_404(Comment, pk=pk)

    # get the related post object's pk, as the redirect above.
    # We do need this because when we are to redirect later, the
    # comment is already deleted, so as its link to the Post's pk.
    # We won't be able to call it like 'pk=comment.post.pk'
    post_pk = comment.post.pk

    # call the delete method of Comment object.
    comment.delete()

    # redirect using the post's pk storage variable
    return redirect('post_detail', pk=post_pk)
