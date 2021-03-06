from django.db import models


class Element(models.Model):
    """
    element class
    """
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    element_description = models.TextField(null=True)
    why = models.TextField(null=True)
    sub_benefits = models.TextField(null=True)
    vertical_image = models.ImageField(null=True, blank=True)
    horizontal_image = models.ImageField(null=True, blank=True)
    price = models.DecimalField(null=True, max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name
