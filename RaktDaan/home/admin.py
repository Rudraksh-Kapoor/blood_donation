from django.contrib import admin # type: ignore
from home.models import *

admin.site.register(RequestBlood)
admin.site.register(BloodGroup)
admin.site.register(Donor)