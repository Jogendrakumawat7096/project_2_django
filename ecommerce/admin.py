from django.contrib import admin
from .models import User,Whishlist,Product,Cart,Coupon

# Register your models here.
admin.site.register(User)
admin.site.register(Product)
admin.site.register(Whishlist)
admin.site.register(Cart)
admin.site.register(Coupon)