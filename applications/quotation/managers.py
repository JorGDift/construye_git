# modelos
from django.db import models


class QuotationManager(models.Manager):
    # manager padre para la creación de ferreteria
    def _create_ironmongery(self, mail, name, last_name, avatar, phone, password, is_staff, is_active, is_superuser,
                            **extra_fields):
        user = self.model(
            mail=mail,
            name=name,
            last_name=last_name,
            avatar=avatar,
            phone=phone,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    # manager para la creación de una ferreteria
    def create_superuser(self, mail, name=None, last_name=None, avatar=None, phone=None, password=None, **extra_fields):
        return self._create_user(mail, name, last_name, avatar, phone, password, True, True, True, **extra_fields)

    def search_ironmongery_categorie(self, ironmongery_pk):
        # busca los productos de la ferreteria relacionada con el usuario
        categorie_list = self.filter(
            fk_ironmongery=ironmongery_pk
        )
        return categorie_list


class QuotationDetailManager(models.Manager):
    # busca los todos los detalles de la cotización
    def search_details_quotation(self, quote_pk):
        detail_list = self.filter(
            fk_quotation=quote_pk
        )
        return detail_list
