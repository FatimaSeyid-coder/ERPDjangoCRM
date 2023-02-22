from django.shortcuts import render ,redirect ,get_object_or_404
from django.views.generic import TemplateView ,CreateView ,UpdateView
from .form import SignUpForm ,UserForm ,ProfileForm ,ajoutForm,clientpisteForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect,Http404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from apps.profil.models import * 

# Create your views here.
class home(TemplateView):
    template_name='common/home.html'
    
class dashbordView(TemplateView):
    template_name='base.html'
       
class SingUpView(CreateView):
    form_class=SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'common/register.html'
 
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'common/profile.html'  
     
class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'common/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data=request.FILES or None
        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data ,instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)     

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
    
class clientView(TemplateView):
    template_name = 'common/client.html'
      
    def get(self, request):
      title='liste de clients'
      queryset=client.objects.all()
      context={
        "title":title,
        "queryset":queryset   
         } 
      return render(request, self.template_name, context)
    
class societeView(TemplateView):
    template_name = 'common/societe.html'
      
    def get(self, request):
      title='liste des societes'
      queryset=client.objects.filter(type='societe')
      context={
        "title":title,
        "queryset":queryset   
         } 
      return render(request, self.template_name, context)
  
class ajoutView(TemplateView):
    template_name = 'common/ajout.html'

    def post(self, request, *args, **kwargs):
        form = ajoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client')
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = ajoutForm()
        return render(request, self.template_name, {'form': form})
        
    
      
    
class ContacterView(TemplateView):
    template_name = 'common/contacter.html'

    def post(self, request, *args, **kwargs):
        form = clientpisteForm(request.POST)
        if form.is_valid():
            message = form.save()
            return redirect('home')
        return render(request, self.template_name, {'form': form})

    def get(self, request, *args, **kwargs):
        form = clientpisteForm()
        return render(request, self.template_name, {'form': form})
   

class pisteView(TemplateView):
    template_name = 'common/piste.html'
      
    def get(self, request):
      title='liste de clients'
      queryset=clientpiste.objects.all()
      context={
        "title":title,
        "queryset":queryset   
         } 
      return render(request, self.template_name, context)
  
class messageView(TemplateView):
    template_name = 'common/message.html'

    def get(self, request, firstname):
        title = 'liste des societes'
        queryset = None
        try:
            clientpiste_instance = clientpiste.objects.get(firstname=firstname)
            messages = message.objects.filter(clientpiste=clientpiste_instance)
            queryset = messages
        except clientpiste.DoesNotExist:
            # Handle the case where the Clientpiste object with the specified firstname does not exist
            pass

        context = {
            "title": title,
            "queryset": queryset
        }
        return render(request, self.template_name, context)





def delete_client(request, id=None):
    client_obj = get_object_or_404(client, pk=id)
    if request.method == 'POST':
        client_obj.delete()
        if id:
            return redirect(reverse_lazy('client'))
    return render(request, 'common/delete_client.html')


class piplineView(TemplateView):
    template_name = 'common/pipline.html'  

class repondreView(TemplateView):
    template_name = 'common/repondre.html'  

class UpdateClientView(UpdateView):
    model = client
    fields = ['phone_number', 'email','post','etiquette']
    template_name = 'common/update_client.html'
    success_url = reverse_lazy('client')
    
    def get_object(self, queryset=None):
        obj = get_object_or_404(client, id=self.kwargs['id'])
        return obj

    def form_valid(self, form):
        form.save()
        return redirect(self.success_url)