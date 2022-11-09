from django.db import models
from django.utils.translation import gettext_lazy as _
from globals.models import AddressMixin, CommonBaseModel


# Create your models here.
class Property(CommonBaseModel, AddressMixin):
    responsible_user = models.ForeignKey(
        "users.User",
        verbose_name=_("responsible user"),
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_responsible_user",
    )
    all_tenants = models.ManyToManyField(
        "users.User",
        verbose_name=_("all tenants"),
        related_name="%(app_label)s_%(class)s_all_tenants",
    )
    manager = models.ForeignKey(
        "users.User",
        verbose_name=_("manager"),
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_manager",
    )

    class Meta:
        verbose_name_plural = _("properties")
