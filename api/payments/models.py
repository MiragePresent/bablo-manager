from django.db import models
from django.conf import settings
from datetime import datetime

"""
When user pay for some stuff, he able to create a payment and divide amount into
other users.

Payment contains general information about paid payment (check)
"""
class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='snippets', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=1500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    upddated_at = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.title

"""
Quotient contains amounts of divided payment between users
"""
class Quotient(models.Model):

    """
    Statuses of Quotient:
        DEFAULT (0) – just created Quotient
        APPROVED (1) – user approved quotient as actual
        DISSAPROVED (2) – user disapproved quotient
        PAID (3) – user has paid full amount
    """
    DEFAULT = 0
    APPROVED = 1
    DISSAPROVED = 2
    PAID = 3

    STATUSES = (
        (DEFAULT, 'New'),
        (APPROVED, 'Approved'),
        (DISSAPROVED, 'Dissaproved'),
        (PAID, 'Paid'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='quotients', null=True, on_delete=models.SET_NULL)
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)
    amount = models.FloatField(default=0.0)
    status = models.PositiveSmallIntegerField(choices=STATUSES, default=DEFAULT)
    paid_at = models.DateTimeField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(default=datetime.now())
