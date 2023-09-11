from django.contrib import admin

class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = ('id','created',('first_name', 'last_name'),'email', 'address', ' ')
    readonly_fields = ('created',)
