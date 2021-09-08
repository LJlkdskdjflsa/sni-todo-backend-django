from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE
from todo.user.models import User
import django.utils.timezone as timezone

# softDelete model
class SoftDeleteBaseModel(SafeDeleteModel):
    """
    軟刪除基本表

    Args:
        SafeDeleteModel ([type]): [description]
    """

    _safedelete_policy = SOFT_DELETE

    class Meta:
        abstract = True


class TrackingBaseModel(SoftDeleteBaseModel):
    """
    追蹤基本表

    Args:
        BaseSoftDeleteModel ([type]): [description]
    """

    id = models.AutoField(primary_key=True)
    # user
    creator = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="创建者",
        related_name="+",
    )
    owner = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="拥有者",
        related_name="+",
    )
    updater = models.ForeignKey(
        to=User,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="修改者",
        related_name="+",
    )
    # time
    create_time = models.DateTimeField(
        default=timezone.now,
        verbose_name="创建时间",
        help_text="创建时间",
        null=True,
        blank=True,
    )
    update_time = models.DateTimeField(
        auto_now=True, verbose_name="修改时间", help_text="修改时间", null=True, blank=True
    )

    class Meta:
        abstract = True
