from django.contrib import admin 

# Register your models here.
from .models import Profile ,client,contact,message,clientpiste
admin.site.register(Profile) 
admin.site.register(client) 
admin.site.register(contact) 
admin.site.register(message)
admin.site.register(clientpiste)
