from django.db import models
from django.db.models import Q


class ProductManager(models.Manager):
    # crear un producto
    def create_product(self, name, description, image, category, sub_category, price, brand, fk_ironmongery, **extra_fields):
        new_product = self.model(
            name=name,
            description=description,
            image=image,
            category=category,
            sub_category=sub_category,
            price=price,
            brand=brand,
            fk_ironmongery=fk_ironmongery,
            **extra_fields
        )

        new_product.save(using=self.db)
        return new_product

    def search_product_ironmongery_user(self, user):
        # busca los productos de la ferreteria relacionada con el usuario
        product_list = self.filter(
            fk_ironmongery=user.fk_ironmongery
        )
        return product_list

    def search_product_ironmongery(self, pk_ironmongery):
        # busca los productos relacionados con la ferreteria
        product_list = self.filter(
            fk_ironmongery=pk_ironmongery
        )
        return product_list

    def search_products(self, product_name):
        product_list = self.filter(
            name__icontains=product_name
        )
        return product_list

    def search_product_ironmongery_distinct(self, ironmongery):
        # busca los productos relacionados con la ferreteria
        product_list_distinct = self.filter(
            fk_ironmongery=ironmongery
        )
        return product_list_distinct
    
    def admin_search_product(self, fk_ironmongery, name, status, category, sub_category, brand):
        # Construir la expresión Q inicial con fk_ironmongery y name
        filters = Q(fk_ironmongery=fk_ironmongery) & Q(name__icontains=name)
        
        # Añadir filtros adicionales si se proporcionan
        if status is not None:
            filters &= Q(status=status)
        if category:
            filters &= Q(category=category)
        if sub_category:
            filters &= Q(sub_category=sub_category)
        if brand:
            filters &= Q(brand=brand)
        
        # Filtrar los productos basados en las expresiones Q construidas
        product_list = self.filter(filters)
        
        return product_list
        


class ProductCategoryManager(models.Manager):
    def search_ironmongery_categories(self, pk_ironmongery):
        # busca las categorias relacionadas con la ferreteria
        category_list = self.filter(
            product__fk_ironmongery=pk_ironmongery
        ).distinct()
        return category_list


    def search_product_category_ironmongery(self, ironmongery):
        #busca las categorias relacionadas con la ferreteria
        category_list = self.filter(
            fk_ironmongery=ironmongery
        )
        return category_list

class ProductBrandManager(models.Manager):
    # busca las marcas relacionadas con la ferreteria
    def search_brand_ironmongery(self, ironmongery):
        brand_list = self.filter(
            fk_ironmongery=ironmongery
        )
        return brand_list

