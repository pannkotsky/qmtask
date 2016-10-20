from django.db import models


class Good(models.Model):
    name = models.CharField(max_length=50)
    ordinary_price = models.IntegerField()
    pricing_unit = models.IntegerField(default=1)

    def __str__(self):
        return self.name


class Bucket(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)


class Purchase(models.Model):
    bucket = models.ForeignKey(Bucket, on_delete=models.CASCADE)
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
    good_count = models.IntegerField(default=0)


class SpecialOffer(models.Model):
    target_good = models.ForeignKey(Good, on_delete=models.CASCADE,
                                    related_name='target_good')
    condition_good = models.ForeignKey(Good, on_delete=models.CASCADE,
                                       related_name='condition_good')
    condition_good_count = models.IntegerField()
    special_price = models.IntegerField()
    good_count = models.IntegerField()

    def __str__(self):
        return '{0}x{1}'.format(self.condition_good, self.condition_good_count)
