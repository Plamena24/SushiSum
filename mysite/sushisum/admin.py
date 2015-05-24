from django.contrib import admin

# Register your models here.
from .models import SushiSitting, SushiType, SushiPieces

class SushiPiecesInline(admin.TabularInline):
	model = SushiPieces
	extra = 3

class SushiSittingAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['location_name']}),
		('Date Information', {'fields': ['sitting_date'],'classes':['collapse']}),
	]
	inlines = [SushiPiecesInline]
	list_display = ('sitting_date',"location_name")

class SushiTypeAdmin(admin.ModelAdmin):
	pass


admin.site.register (SushiSitting, SushiSittingAdmin)
admin.site.register (SushiType, SushiTypeAdmin)