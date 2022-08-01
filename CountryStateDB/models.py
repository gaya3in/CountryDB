from django.db import models

class Country(models.Model):
    country_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    iso3 = models.CharField(max_length=45, blank=True, null=True)
    iso2 = models.CharField(max_length=45, blank=True, null=True)
    numeric_code = models.CharField(max_length=100, blank=True, null=True)
    phone_code = models.CharField(max_length=100, blank=True, null=True)
    capital = models.CharField(max_length=100, blank=True, null=True)
    currency = models.CharField(max_length=45, blank=True, null=True)
    currency_name = models.CharField(max_length=100, blank=True, null=True)
    currency_symbol = models.CharField(max_length=100, blank=True, null=True)
    tld = models.CharField(max_length=45, blank=True, null=True)
    native = models.CharField(max_length=200, blank=True, null=True)
    region = models.CharField(max_length=200, blank=True, null=True)
    sub_region = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    emoji = models.CharField(max_length=200, blank=True, null=True)
    emojiU = models.CharField(max_length=200, blank=True, null=True)  # Field name made lowercase.


class State(models.Model):
    state_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    state_code = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=200, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING)

class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    state = models.ForeignKey('State', models.DO_NOTHING, blank=True, null=True)
    country = models.ForeignKey('Country', models.DO_NOTHING, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)

class TimeZones(models.Model):
    time_zone_id = models.AutoField(primary_key=True)
    gmt_offset = models.CharField(max_length=200, blank=True, null=True)
    gmt_offset_name = models.CharField(max_length=200, blank=True, null=True)
    abreviation = models.CharField(max_length=100, blank=True, null=True)
    tz_name = models.CharField(max_length=200, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)
    zone_name = models.CharField(max_length=200, blank=True, null=True)


class Translations(models.Model):
    translations_id = models.AutoField(primary_key=True)
    kr = models.CharField(max_length=45, blank=True, null=True)
    br = models.CharField(max_length=45, blank=True, null=True)
    pt = models.CharField(max_length=45, blank=True, null=True)
    nl = models.CharField(max_length=45, blank=True, null=True)
    hr = models.CharField(max_length=45, blank=True, null=True)
    fa = models.CharField(max_length=45, blank=True, null=True)
    de = models.CharField(max_length=45, blank=True, null=True)
    es = models.CharField(max_length=45, blank=True, null=True)
    fr = models.CharField(max_length=45, blank=True, null=True)
    ja = models.CharField(max_length=45, blank=True, null=True)
    it = models.CharField(max_length=45, blank=True, null=True)
    cn = models.CharField(max_length=45, blank=True, null=True)
    tr = models.CharField(max_length=45, blank=True, null=True)
    country = models.ForeignKey(Country, models.DO_NOTHING, blank=True, null=True)


