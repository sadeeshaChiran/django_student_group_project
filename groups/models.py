from django.db import models

from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()


# Create your models here.
class Group(models.Model):
    admin = models.ForeignKey(User,related_name='group_admin',on_delete=models.CASCADE)
    slug = models.SlugField(allow_unicode=True, unique=True) 
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, default='')
    members = models.ManyToManyField(User,through="GroupMember")
    created_date = models.DateTimeField(default=timezone.now)
    approved_group = models.BooleanField(default=False)

    
    def approve(self):
        self.approved_group = True
        self.save()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)  
        super().save(*args, **kwargs)
       

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "groups:single",
            kwargs={
                "slug": self.slug
            }
        )
        


    class Meta:
        ordering = ["name"]


class GroupMember(models.Model):
    group = models.ForeignKey(Group,related_name='memberships',on_delete=models.CASCADE)
    user = models.ForeignKey(User,related_name='user_groups',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ("group", "user")
