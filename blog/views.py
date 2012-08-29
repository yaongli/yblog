# Create your views here.

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_protect
from django.utils.translation import ugettext_lazy as _
from django.utils.html import escapejs
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator,InvalidPage,EmptyPage,PageNotAnInteger
from models import Blog, BlogForm
from forms import SignupForm, LoginForm,MarkdownForm, ChangePasswdForm
import markdown
import time
BLOGS_PER_PAGE = 5
BLOGS_PER_LISTPAGE = 10

def get_page(objs, page):
    paginator = Paginator(objs, BLOGS_PER_PAGE)
    
    try:
        ret = paginator.page(page)
    except (EmptyPage, InvalidPage):
        ret = paginator.page(paginator.num_pages)

    return ret

def index(req, page=1):
    try:
        page = int(page)
    except ValueError:
        page = 1
    
    blogs = get_page(Blog.objects.all(), page)
    return render_to_response('index.html', {'settings' : settings, 'blogs' : blogs}, context_instance=RequestContext(req))

def addblog(req):
    blog = Blog()
    blog.user = req.user
    form = BlogForm(instance=blog)
    return render_to_response('post.html', {'settings' : settings, 'form' : form}, context_instance=RequestContext(req))
    
def editblog(req, blogid):
    blog = Blog.objects.get(id=blogid)
    if blog.user != req.user:
        return HttpResponseRedirect('/')
    form = BlogForm(instance=blog)
    return render_to_response('post.html', {'settings' : settings, 'form' : form}, context_instance=RequestContext(req))

def saveblog(req):
    form = BlogForm(req.POST)
    blog = form.save(commit=False)
    blog.user = req.user
    #blog.content = markdown.markdown(blog.markdown)
    blog.save()
    #return index(req)
    return HttpResponseRedirect(reverse('showblog', args=[blog.id]))
    
def showblog(req, blogid):
    blogid = int(blogid)
    blog = Blog.objects.select_related().get(id=blogid)
    return render_to_response('blog.html', {'settings' : settings, 'blog' : blog}, context_instance=RequestContext(req))

def bloglist(req, page=1):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, BLOGS_PER_LISTPAGE)
    
    try:
        blogs = paginator.page(page)
    except (EmptyPage, InvalidPage):
        blogs = paginator.page(paginator.num_pages)
    return render_to_response('bloglist.html', {'settings' : settings, 'blogs' : blogs}, context_instance=RequestContext(req))

def login(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.login(req):
            return HttpResponseRedirect(reverse('index', args=[]))
    else:
        form = LoginForm()
    return render_to_response('login.html', {'settings' : settings, 'form': form}, context_instance=RequestContext(req))

def change_passwd(req):
    if req.method == 'POST' and req.user.is_authenticated():
        form = ChangePasswdForm(req.user, req.POST)
        if form.save():
            return render_to_response('change_passwd_success.html', {'settings' : settings}, context_instance=RequestContext(req))
    else:
        form = ChangePasswdForm(req.user)
    return render_to_response('change_passwd.html', {'settings' : settings, 'form': form}, context_instance=RequestContext(req))

def register(req):
    if req.method == 'POST':
        form = SignupForm(req.POST)
        if form.save(req):
            ctx = {'settings' : settings, 'email': form.cleaned_data['email'], }
            return render_to_response('singup_success.html', ctx, context_instance=RequestContext(req))
    else:
        form = SignupForm()
    return render_to_response('singup.html', {'settings' : settings, 'form': form}, context_instance=RequestContext(req))

def signout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')

def bloghelp(req):
    return HttpResponseRedirect(reverse('index', args=[]))

def markdownblog(req, blogid=None):
    if req.method == 'POST':
        form = MarkdownForm(req.POST)
        blog = form.save(req)
        if blog:
            return HttpResponseRedirect(reverse('showblog', args=[blog.id]))
    else:
        if blogid:
            blog = Blog.objects.get(id=blogid)
            blogid = blog.id
            title = blog.title
            markdown = blog.markdown
            form = MarkdownForm({'blogid' : blog.id, 'title' : blog.title, 'markdown' : blog.markdown})
        else:
            form = MarkdownForm()
            
    return render_to_response('markdown.html', {'settings': settings, 'form': form}, context_instance=RequestContext(req))


