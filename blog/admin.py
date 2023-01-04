from django.contrib import admin
from blog.models import Post, Category
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(Post)
# we can use this one(code in the blow) instead of that one(code up there with @) no diffrence
# admin.site.register(Post, PostAdmin)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = "-empty-" 
    list_display = ('title','status','author','created_date','published_date','updated_date','counted_views')  
    list_filter = ('status','counted_views')
    search_fields = ['title','content']
    summernote_fields = ('content',)

admin.site.register(Category)