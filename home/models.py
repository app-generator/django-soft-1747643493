# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Detail(models.Model):

    #__Detail_FIELDS__
    job_id = models.IntegerField(null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    pc_ip = models.CharField(max_length=255, null=True, blank=True)
    git_ref = models.CharField(max_length=255, null=True, blank=True)
    pattern_name = models.CharField(max_length=255, null=True, blank=True)
    f1_ini_name = models.CharField(max_length=255, null=True, blank=True)
    project_name = models.CharField(max_length=255, null=True, blank=True)
    status = models.CharField(max_length=255, null=True, blank=True)
    start_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True, default=timezone.now)
    auto_dump_folder = models.CharField(max_length=255, null=True, blank=True)
    elapsed_time = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Detail_FIELDS__END

    class Meta:
        verbose_name        = _("Detail")
        verbose_name_plural = _("Detail")



#__MODELS__END
