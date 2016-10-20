from django import test

from market import models
from market import views


class MockQuerySet(list):
    def get(self, id):
        for item in self:
            if item.id == id:
                return item


class TestTotalValue(test.TestCase):
    def setUp(self):
        super(TestTotalValue, self).setUp()
        self.goods = MockQuerySet((
            models.Good(id=1, name='A', ordinary_price=50),
            models.Good(id=2, name='B', ordinary_price=30),
            models.Good(id=3, name='C', ordinary_price=199, pricing_unit=1000),
            models.Good(id=4, name='D', ordinary_price=120),
            models.Good(id=5, name='E', ordinary_price=90),
        ))
        self.specials = [
            models.SpecialOffer(target_good_id=1, condition_good_id=1,
                                condition_good_count=3, special_price=130,
                                good_count=3),
            models.SpecialOffer(target_good_id=5, condition_good_id=4,
                                condition_good_count=2, special_price=0,
                                good_count=1),
        ]

    def test_ordinary_prices(self):
        purchases = [
            models.Purchase(bucket_id=1, good_id=1, good_count=2),
            models.Purchase(bucket_id=1, good_id=2, good_count=1),
            models.Purchase(bucket_id=1, good_id=3, good_count=1568),
        ]
        total = views.calculate_total(purchases, self.goods, self.specials)
        expected = int(2 * 50 + 1 * 30 + 1568 * 199 / 1000.0)
        self.assertEqual(total, expected)

    def test_multiprice(self):
        purchases = [models.Purchase(bucket_id=1, good_id=1, good_count=3)]
        total = views.calculate_total(purchases, self.goods, self.specials)
        self.assertEqual(total, 130)

    def test_get_one_free(self):
        purchases = [
            models.Purchase(bucket_id=1, good_id=4, good_count=2),
            models.Purchase(bucket_id=1, good_id=5, good_count=1),
        ]
        total = views.calculate_total(purchases, self.goods, self.specials)
        self.assertEqual(total, 120 * 2)

    def test_dont_get_two_free(self):
        purchases = [
            models.Purchase(bucket_id=1, good_id=4, good_count=2),
            models.Purchase(bucket_id=1, good_id=5, good_count=2),
        ]
        total = views.calculate_total(purchases, self.goods, self.specials)
        self.assertEqual(total, 120 * 2 + 90)
