from tfa_store.models import *  
from common.models import *
from django.contrib import admin

# Register your models here.

admin.site.register(User)
admin.site.register(Cart)
admin.site.register(stateModel)
admin.site.register(AddressModel)
admin.site.register(placeOrder)
admin.site.register(sub_placeorder)
admin.site.register(Contact)

admin.site.site_header = 'The Fashion Atelier Admin'