from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.accounts.models import User

class AgeBand(models.Model):
    age_from = models.CharField("From", max_length=20)
    age_to = models.CharField("To", max_length=20)
    is_active = models.BooleanField(_('active'), default=True)

    class Meta:
        verbose_name = _('Age Band')
        verbose_name_plural = _('Age Bands')

    def __str__(self):
        band_name = '%s - %s' % (self.age_from, self.age_to)
        return band_name

    def get_band_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        band_name = '%s - %s' % (self.age_from, self.age_to)
        return band_name.strip()

class PolicyType(models.Model):
    type_name = models.CharField("Type", max_length=20, unique=True)
    is_active = models.BooleanField(_('active'), default=True)

    class Meta:
        verbose_name = _('Policy Type')
        verbose_name_plural = _('Policy Types')

    def __str__(self):
        return self.type_name


class Policy(models.Model):
    name= models.CharField("Insurance Name", max_length=200, unique=True)
    types = models.ForeignKey(PolicyType, on_delete=models.CASCADE)
    premium = models.CharField("Premium", max_length=20,null=True,blank=True)
    cover = models.CharField("Cover", max_length=20,null=True,blank=True)
    age_band = models.ForeignKey(AgeBand, on_delete=models.CASCADE)

    created_at = models.DateTimeField(_('date joined'), auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_('active'), default=True)

    class Meta:
        verbose_name = _('Policy')
        verbose_name_plural = _('Policy')

    def __str__(self):
        return str(self.types.type_name)


class Quote(models.Model):
    STATUS = (("NEW","NEW"),("ACTIVE","ACTIVE"),("ACCEPTED","ACCEPTED"),)

    quote = models.CharField("Quote Text", max_length=20, unique=True)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    types = models.ForeignKey(PolicyType, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField("State", max_length=20,choices=STATUS)

    created_at = models.DateTimeField(_('date joined'), auto_now_add=True)
    last_updated_on = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(_('active'), default=True)

    class Meta:
        verbose_name = _('Quote')
        verbose_name_plural = _('Quotes')

    def __str__(self):
        return self.quote
