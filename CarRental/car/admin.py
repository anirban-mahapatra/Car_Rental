from django.contrib import admin
from car.models import Contct, DriverDetail, UserDetail

# Register your models here.
admin.site.register(UserDetail)
admin.site.register(Contct)
admin.site.register(DriverDetail)
