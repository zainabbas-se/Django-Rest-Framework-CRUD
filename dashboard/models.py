from django.db import models

class Transactions(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField()
    transaction_type = models.CharField(max_length=100, choices=(
        ('CREDIT', 'CREDIT'),
        ('DEBIT', 'DEBIT')
    ))

    def save(self, *args, **kwargs):
        # Make amount negative for DEBIT transactions
        if self.transaction_type == 'DEBIT':
            self.amount = self.amount * -1
        return super().save(*args, **kwargs)

    # Define the string representation of the object
    def __str__(self):
        return f"{self.title} ({self.transaction_type})"


