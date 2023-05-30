from django.contrib import admin
from .models import MappingPoint_I, MappingPoint_E, ContactForm_E, ContactForm_I
# Register your models here.

class QuestionAdmin_I(admin.ModelAdmin):
    search_fields = ['name']

class QuestionAdmin_E(admin.ModelAdmin):
    search_fields = ['name']


admin.site.register(MappingPoint_I, QuestionAdmin_I)
admin.site.register(MappingPoint_E, QuestionAdmin_E)
admin.site.register(ContactForm_E)
admin.site.register(ContactForm_I)


