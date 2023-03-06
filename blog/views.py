from django.views.generic import View, TemplateView, CreateView, FormView, DeleteView, ListView
from django.contrib.auth import authenticate, login, logout 
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib import messages
from .models import *
from .forms import *
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect

class AdminLoginView(FormView):
    template_name = "adminlogin.html"
    form_class = CustomerLoginForm
    success_url = "../postslist/"

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Admin.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})
        return super().form_valid(form)

#  You can't use Decorators above class inherit LoginRequiredMixin in your class. Use adminrequired mixin
class AdminRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Admin.objects.filter(user=request.user).exists():
            pass
        else:
            return redirect("/admin-login/")
        return super().dispatch(request, *args, **kwargs)



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})




def homepage(request):
    return HttpResponse ("<h1>Homepage</h1>")


def chi_siamo(request):
    return HttpResponse ("<h2>Chi siamo</h2>")


def contatti(request):
    return HttpResponse ("<h3>Contattaci</h3>") 



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/")




def view_post(request, post_id):
    blogpost = BlogPost.objects.get(pk=post_id)
    blogpost.view_count += 1
    blogpost.save()
    return render(request, 'view_post.html', {'blogpost': blogpost})
    


class AdminPostsListView(AdminRequiredMixin, ListView):
    template_name = "adminpostslist.html"
    queryset = BlogPost.objects.all().order_by("-id")
    context_object_name = "allposts"


class CreaPost(AdminRequiredMixin,CreateView):
    template_name = "create_blog_post.html"
    form_class = BlogPostForm

    def get_success_url(self):
        return reverse('view_post',args=(self.object.id,))

class BlogPostModifica(AdminRequiredMixin,UpdateView):
    model = BlogPost
    form_class = BlogPostForm
    template_name = "create_post.html"
    success_url ="/"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        self.object = self.get_object()
        context['titolo'] = 'Modifica del Post' + ' nr. ' + str(self.object)
        return context

    def form_invalid(self, form):
        messages.error(self.request, "Errore durante la compilazione")
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, "Modifica effettuata con successo")
        original_instance = BlogPost.objects.get(pk=self.object.id)
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())
        
    def get_success_url(self):
        self.object = self.get_object()
        indirizzo =  str('/view_post/'+str(self.object.id))
        return  indirizzo 