from django.contrib import admin

# Register your models here.
from .models import News,category,subCategory,profiles,profilesIndex,userRights

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at','updated_at','is_published')
    list_display_links = ('id','title')
    search_fields = ('title','content')
    list_editable = ('is_published',)

admin.site.register(News,NewsAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display = ('categoryTitle',)
    list_display_links = ('categoryTitle',)
    search_fields = ('categoryTitle',)

admin.site.register(category,categoryAdmin)


class subCategoryAdmin(admin.ModelAdmin):
    list_display = ('subCategoryTitle','subCategoryLink','subCategorySort')
    list_display_links = ('subCategoryTitle','subCategoryLink','subCategorySort')
    search_fields = ('subCategoryTitle',)

admin.site.register(subCategory,subCategoryAdmin)


class profilesIndexAdmin(admin.ModelAdmin):
    list_display = ('profileIndexTitle',)
    list_display_links = ('profileIndexTitle',)
    search_fields = ('profileIndexTitle',)

admin.site.register(profilesIndex,profilesIndexAdmin)



class profilesAdmin(admin.ModelAdmin):
    list_display = ('profileIndex_FK','categoryID_FK','subCategoryID_FK')
    list_display_links = ('profileIndex_FK','categoryID_FK','subCategoryID_FK')
    search_fields = ('profileIndex_FK__profileIndexTitle','categoryID_FK__categoryTitle','subCategoryID_FK__subCategoryTitle')

admin.site.register(profiles,profilesAdmin)


class userRightsAdmin(admin.ModelAdmin):
    list_display = ('userID','profilesIndex_FK')
    list_display_links = ('userID','profilesIndex_FK')
    search_fields = ('userID__username','profilesIndex_FK__profileIndexTitle')

admin.site.register(userRights,userRightsAdmin)

