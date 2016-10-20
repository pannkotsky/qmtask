from django.contrib import admin

from . import models


admin.site.register([
    models.Good,
    models.Bucket,
    models.Purchase,
    models.SpecialOffer
])
