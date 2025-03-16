from django.contrib import tfa_store
from app.models import *
# Register your models here.

admin.site.register(User)
admin.site.register(Cart)
admin.site.register(stateModel)
admin.site.register(AddressModel)
admin.site.register(placeOrder)
admin.site.register(sub_placeorder)
admin.site.register(Contact)

admin.site.site_header = 'The Fashion Atelier Admin'