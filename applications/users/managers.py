# modelos
from django.db import models
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager, models.Manager):
    # manager padre para la creación de usuario
    def _create_user(self, email, firs_name, last_name, avatar, phone, fk_ironmongery, password, is_staff, is_active, is_superuser,
                     **extra_fields):
        user = self.model(
            email=email,
            firs_name=firs_name,
            last_name=last_name,
            avatar=avatar,
            phone=phone,
            fk_ironmongery=fk_ironmongery,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_active=is_active,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self.db)
        return user

    # manager para la creación de un super usuario
    def create_superuser(self, email, firs_name=None, last_name=None, avatar=None, phone=None, fk_ironmongery=None, password=None, **extra_fields):
        return self._create_user(email, firs_name, last_name, avatar, phone, fk_ironmongery, password, True, True, True, **extra_fields)

    def create_user(self, email, firs_name, last_name, phone, fk_ironmongery, avatar=None, password=None, **extra_fields):
        return self._create_user(email, firs_name, last_name, avatar, phone, fk_ironmongery, password, True, True, False, **extra_fields)

    def create_staff(self, email, firs_name, last_name, avatar, phone, fk_ironmongery, password=None, **extra_fields):
        return self._create_user(email, firs_name, last_name, avatar, phone, fk_ironmongery, password, True, True, False, **extra_fields)

    # buscar los usuario de la ferreteria
    def search_user_by_ironmongery(self, ironmongery):
        user_list = self.model.objects.filter(
            fk_ironmongery=ironmongery
        )
        return user_list
