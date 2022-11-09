from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


# Create your models here.
class CommonBaseModel(models.Model):
    name = models.CharField(_("name"), max_length=50)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("created by"),
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_created",
        editable=False,
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_("updated by"),
        on_delete=models.PROTECT,
        related_name="%(app_label)s_%(class)s_updated",
        editable=False,
    )
    created_at = models.DateTimeField(_("created datetime"), auto_now_add=True)
    updated_at = models.DateTimeField(_("updated datetime"), auto_now=True)
    slug = models.SlugField(unique=True, editable=False)

    class Meta:
        abstract = True
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name, allow_unicode=True)

        return super().save(*args, **kwargs)


class State(models.Model):
    name = models.CharField(_("name"), max_length=50)
    code = models.CharField(
        _("code"), help_text=_("e.g., 'WA' for Washington"), max_length=10
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class AddressMixin(models.Model):
    address_line_1 = models.CharField(_("line 1"), max_length=50)
    address_line_2 = models.CharField(_("line 2"), max_length=50, blank=True)
    zip_code = models.CharField(_("ZIP code"), max_length=15)
    city = models.CharField(_("city"), max_length=50)
    state = models.ForeignKey(
        State, verbose_name=_("state"), on_delete=models.PROTECT, null=True
    )

    class Meta:
        abstract = True
