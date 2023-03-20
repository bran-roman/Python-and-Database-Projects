from django.db import models

ACTIVITY_TYPE = [
    ('Dining', 'Dining'),
    ('Attractions', 'Attractions'),
    ('Travel', 'Travel'),
]

BUDGET_TYPE = [
    ('$', 'Cheap'),
    ('$$', 'Average'),
    ('$$$', 'Expensive'),
]

CREDIT_TYPE = [
    ('Y', 'Yes'),
    ('N', 'No'),
]


class Activities(models.Model):
    activity_name = models.CharField(max_length=100, blank=True, null=False)
    activity_type = models.CharField(max_length=100, default="", blank=True, null=False, choices=ACTIVITY_TYPE)
    budget_type = models.CharField(max_length=100, default="", blank=True, null=False, choices=BUDGET_TYPE)
    credit_for_submission = models.CharField(max_length=3, default="", blank=True, null=False, choices=CREDIT_TYPE)
    description = models.CharField(max_length=1000, blank=True, null=False)
    # temperature = models.IntegerField(default="", blank=True, null=False)

    objects = models.Manager()

    class Meta:
        verbose_name_plural = "Activities"

    def __str__(self):
        return self.activity_name


class User(models.Model):
    first_name = models.CharField(max_length=60, default="", blank=True, null=False)
    last_name = models.CharField(max_length=60, default="", blank=True, null=False)
    email = models.CharField(max_length=60, default="", blank=True, null=False)
    user_name = models.CharField(max_length=60, default="", blank=True, null=False)

    objects = models.Manager()

    def __str__(self):
        return self.first_name


class VegasTemp(models.Model):
    temperature = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    VegasTemps = models.Manager()

    def __str__(self):
        return self.temperature
        return self.date


class VegasNews(models.Model):
    postal_code = models.IntegerField()
    state = models.CharField(max_length=60, default="", blank=True, null=False)
    city = models.CharField(max_length=60, default="", blank=True, null=False)

    VegasNews = models.Manager()

    class Meta:
        verbose_name_plural = "VegasNews"

    def __str__(self):
        return self.postal_code
        return self.state
        return self.city
