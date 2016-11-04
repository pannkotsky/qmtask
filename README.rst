Supermarket pricing
-------------------

The app allows to calculate the total value of the bucket with goods (I know
it should be basket, but I screwed up at some point and it was too much of a
hassle to rename everything).

Admin can add any goods to the database, specifying its name, ordinary price
(in cents) and pricing unit (i.e. how many units of the good you will get if
you pay its price). Pricing unit may be needed to specify amount of good in
grams and set the price for a kilogram, thus both amount and price are stored
as integers. By default pricing unit is equal to 1.

Admin can add some special offers as well. He need to specify the following
fields for that:

* target_good - what good we can get for less price if special offer is used
* condition_good - what good we need to buy to use the special offer
* condition_good_count - how many that good we need to buy
* special_price - what will be the price of target goods with discount
* good_count - how many goods we will get with discount

For example, for special offer *"A costs 50 cents and three A cost $1.30"* the
values will be:

* target_good - A
* condition_good - A
* condition_good_count - 3
* special_price - 130
* good_count - 3

For offer *"D costs $1.20, E costs $0.90, buy two D, get one E free"*:

* target_good - E
* condition_good - D
* condition_good_count - 2
* special_price - 0
* good_count - 1

For offer *"D costs $1.20, E costs $0.90, buy three D, get two E for $1.20"*:

* target_good - E
* condition_good - D
* condition_good_count - 3
* special_price - 120
* good_count - 2

User chooses the needed good from the list. If he chooses good which
needs specifying the amount, the extra number field is displayed to enter that
value. User then clicks "Add good". The new good is added to the bucket (sigh)
and current total value of the bucket is calculated considering special offers.

The site is hosted at https://fathomless-ocean-86436.herokuapp.com/

Admin page is available at https://fathomless-ocean-86436.herokuapp.com/admin

Admin username: *admin*

Admin password: *P@ssw0rd*
