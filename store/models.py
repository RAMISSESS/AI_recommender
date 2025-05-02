from django.db import models as djmodels  # Use Django's models explicitly for compatibility

class Product(djmodels.Model):
    name = djmodels.CharField(max_length=255)
    price = djmodels.FloatField()
    description = djmodels.TextField()
    category = djmodels.CharField(max_length=100, default='Uncategorized')  # ✅ Added with a default
    tags = djmodels.JSONField(default=list)  # ✅ Stores AI-generated tags as JSON array

    def __str__(self):
        return self.name
