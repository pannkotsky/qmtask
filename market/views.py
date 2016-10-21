from django import shortcuts
from django.views import generic

from market import models


class IndexView(generic.TemplateView):
    template_name = 'market/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)

        # create new bucket if no active ones present
        active_buckets = models.Bucket.objects.filter(active=True)
        if active_buckets:
            bucket = active_buckets.order_by('-updated')[0]
        else:
            bucket = models.Bucket()
            bucket.save()

        # retrieve list of goods to offer
        goods = models.Good.objects.all()
        purchases = models.Purchase.objects.filter(bucket_id=bucket.id)
        specials = models.SpecialOffer.objects.all()

        # calculate current total value
        total = calculate_total(purchases, goods, specials)

        context.update({'goods': goods,
                        'total': '{0:.02f}'.format(total / 100.0)})

        return context

    def post(self, request, *args, **kwargs):
        goods = models.Good.objects.all()
        bucket = models.Bucket.objects.order_by('-updated')[0]
        purchases = models.Purchase.objects.filter(bucket_id=bucket.id)
        if 'add' in request.POST:
            # add the last purchase to the bucket
            good_id = int(request.POST['good'])
            good = goods.get(id=good_id)
            quantity = request.POST['quantity'] or '1'
            quantity = int(float(quantity) * good.pricing_unit)
            goods_in_bucket = [p.good_id for p in purchases]
            if good_id in goods_in_bucket:
                purchase = purchases.get(good_id=good_id)
                purchase.good_count += quantity
                purchase.save()
            else:
                new_purchase = models.Purchase(bucket_id=bucket.id,
                                               good_id=good_id,
                                               good_count=quantity)
                new_purchase.save()
        elif 'clear' in request.POST:
            purchases.delete()
        elif 'end' in request.POST:
            bucket.active = False
            bucket.save()

        return shortcuts.redirect('index', *args, **kwargs)


def calculate_total(purchases, goods, specials):
    purchases_dict = {p.good_id: {'target_count': p.good_count,
                                  'condition_count': p.good_count}
                      for p in purchases}
    total = 0

    # check special offers
    for s in specials:
        actual_condition_good = purchases_dict.get(s.condition_good_id)
        actual_target_good = purchases_dict.get(s.target_good_id)
        if not actual_condition_good or not actual_target_good:
            continue
        necessary_condition_count = s.condition_good_count
        actual_condition_count = \
            actual_condition_good['condition_count']
        max_special_sets = \
            actual_condition_count // necessary_condition_count
        if not max_special_sets:
            continue
        actual_target_count = actual_target_good['target_count']
        target_sets = actual_target_count // s.good_count
        special_sets = min(target_sets, max_special_sets)
        ordinary_goods = \
            actual_target_count - special_sets * s.good_count
        total += special_sets * s.special_price
        actual_condition_good['condition_count'] -= \
            special_sets * s.condition_good_count
        actual_target_good['target_count'] = ordinary_goods

    # calculate the rest of purchases by ordinary price
    for good_id in purchases_dict:
        good = goods.get(id=good_id)
        good_price = good.ordinary_price * 1.0 / good.pricing_unit
        total += good_price * purchases_dict[good_id]['target_count']

    return int(total)
