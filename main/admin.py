from django.contrib import admin
from .models import User, Member, Orders, Category, Section
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display= ('id', 'login','email',  'password')

class MemberAdmin(admin.ModelAdmin):
    list_display= ('id', 'name','address', 'min_price', 'min_price', 'purchase_count', 
                   'amount_accepted', 'order_count',  'rating', 'inn', 'average_order_time')
    
class OrderAdmin(admin.ModelAdmin):
    list_display= ('id', 'name','seller', 'buyer', 'price', 'status', 
                   'date_started', 'date_finished')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

class SectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

admin.site.register(User, UserAdmin)
admin.site.register(Member, MemberAdmin)
admin.site.register(Orders, OrderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Section, SectionAdmin)