import cafe as cafe
from django.contrib import admin

# Register your models here.
from main.models import CafeCount, CafeStatus, CafeFranchise, Population, Traffic, Culture, CommercialArea

admin.site.register(CafeCount)
admin.site.register(CafeStatus)
admin.site.register(CafeFranchise)
admin.site.register(CommercialArea)
admin.site.register(Culture)
admin.site.register(Population)
admin.site.register(Traffic)

