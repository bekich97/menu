from django.db import models
from django.urls import reverse

# Create your models here.

# Menu
class Menu(models.Model):
    title = models.CharField(
        max_length=255,
        verbose_name="Название пункт меню"
    )
    slug = models.CharField(
        max_length=255,
        verbose_name="Slug"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = "Меню"
        verbose_name_plural = "Меню"

    def __str__(self):
        return self.title


# Menu items
class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="items",
        verbose_name="Меню"
    )
    title = models.CharField(
        max_length=255,
        verbose_name="Название пункт меню"
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
        verbose_name="Родительский элемент"
    )
    url = models.CharField(
        max_length=255,
        verbose_name="URL"
    )
    named_url = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Named URL',
        help_text="Имя URL, записанное в urls.py"
    )
    order = models.IntegerField(
        default=100,
        verbose_name="Порядок пункт меню"
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    uni_url = models.CharField(
        max_length=255,
    )

    class Meta:
        verbose_name = "Пункт меню"
        verbose_name_plural = "Пункт меню"

    def get_parents_id_list(self):
        pi_list = []
        parent = self
        while parent.parent:
            pi_list.append(parent.parent.id)
            parent = parent.parent

        return pi_list

    def get_url(self):
        if self.named_url:
            try:
                url = reverse(self.named_url)
            except:
                if self.url:
                    url = self.url
                else:
                    url = "/"
        elif self.url:
            url = self.url
        else:
            url = "/"
        return url

    def save(self):
        get_url = self.get_url()
        if get_url != self.uni_url:
            self.uni_url = self.get_url()
        super(MenuItem, self).save()

    def __str__(self):
        return self.title
