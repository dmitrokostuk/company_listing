from __future__ import unicode_literals
from django.conf import settings
from django.core.urlresolvers import reverse

\

from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

class Company(MPTTModel):
    company_name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True)
    company_estimated_earnings=models.CharField(max_length=1024)
    content = models.TextField()



    class MPTTMeta:
        order_insertion_by = ['company_name']
    def __unicode__(self):
        return u"%s "%(self.company_name)


    def __str__(self):
        return self.company_name

    def __unicode__(self):
        return u"%s "%(self.content)


    def __str__(self):
        return self.content


    class Meta:
        ordering = ['parent__id'
                    ]
    def get_absolute_url(self):
        return reverse("company:detail", kwargs={"id": self.id})