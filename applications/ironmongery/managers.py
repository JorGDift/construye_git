# modelos
from django.db import models


class IronmongeryManager(models.Manager):
    # manager padre para la creación de ferreteria
    def create_ironmongery(self, name, logo, fk_location, phone, **extra_fields):
        ironmongery = self.model(
            name=name,
            logo=logo,
            fk_location=fk_location,
            phone=phone,
            **extra_fields
        )
        ironmongery.save(using=self.db)
        return ironmongery

    def search_ironmongery_categorie(self, ironmongery_pk):
        # busca los productos de la ferreteria relacionada con el usuario
        categorie_list = self.filter(
            fk_ironmongery=ironmongery_pk
        )
        return categorie_list

    def search_ironmongery(self):
        ironmongery_list = self.model.objects.all()
        return ironmongery_list

    def create_ironmongery_address(self, city, cologne, street, postal_code, outdoor_number, **extra_fields):
        ironmongery_address = self.model(
            city=city,
            cologne=cologne,
            street=street,
            postal_code=postal_code,
            outdoor_number=outdoor_number,
            **extra_fields
        )
        ironmongery_address.save(using=self.db)
        return ironmongery_address


class IronmongeryAddressManager(models.Manager):
    def create_ironmongery_address(self, city, cologne, street, postal_code, outdoor_number, **extra_fields):
        ironmongery_address = self.model(
            city=city,
            cologne=cologne,
            street=street,
            postal_code=postal_code,
            outdoor_number=outdoor_number,
            **extra_fields
        )
        ironmongery_address.save(using=self.db)
        return ironmongery_address
