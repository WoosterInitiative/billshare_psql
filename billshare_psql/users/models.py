# from address.models import AddressField
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField, Q, UniqueConstraint
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# from billshare_psql.globals.models import CommonBaseModel


class User(AbstractUser):
    """
    Default custom user model for BillShare.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    # billing_address = AddressField(
    #     verbose_name=_("billing address"), blank=True, null=True
    # )
    address_line_1 = models.CharField(_("line 1"), max_length=50)
    address_line_2 = models.CharField(_("line 2"), max_length=50, blank=True)
    zip_code = models.CharField(_("ZIP code"), max_length=15)
    city = models.CharField(_("city"), max_length=50)
    state = models.ForeignKey(
        "globals.State", verbose_name=_("state"), on_delete=models.PROTECT, null=True
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class PhoneNumberType(models.Model):
    name = models.CharField(_("type"), max_length=50)

    def __str__(self):
        return self.name


class PhoneNumber(models.Model):
    number = PhoneNumberField(_("phone number"), region="US")
    type = models.ForeignKey(
        PhoneNumberType, verbose_name=_("type"), on_delete=models.PROTECT
    )
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    primary = models.BooleanField(_("primary contact number"), default=False)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["user"],
                condition=Q(primary="True"),
                name="only_one_primary_number",
            )
        ]
