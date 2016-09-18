from django.contrib import admin
import app.models as dd_models

# Register your models here.
admin.site.register(dd_models.Character)
admin.site.register(dd_models.Bagpack)
admin.site.register(dd_models.Feature)
admin.site.register(dd_models.Trait)
admin.site.register(dd_models.Weapon)