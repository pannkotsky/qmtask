from django.contrib import admin

from . import models


class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'ordinary_price', 'pricing_unit')


class SpecialOfferAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'target_good', 'condition_good',
                    'condition_good_count', 'special_price', 'good_count')

admin.site.register(models.Good, GoodAdmin)
admin.site.register(models.SpecialOffer, SpecialOfferAdmin)

admin.site.register(models.Bucket)
admin.site.register(models.Purchase)
