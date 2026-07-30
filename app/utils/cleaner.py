from app.models.product import Product


class DataCleaner:
    @staticmethod
    def clean(product: Product) -> Product:
        return Product(
            title=product.title.strip(),
            price=round(product.price, 2),
            availability=" ".join(product.availability.split()),
            rating=product.rating,
            product_url=product.product_url,
            image_url=product.image_url,
        )
