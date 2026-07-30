from pydantic import BaseModel, ConfigDict, HttpUrl


class Product(BaseModel):
    title: str
    price: float
    availability: str
    rating: int
    product_url: HttpUrl
    image_url: HttpUrl

    model_config = ConfigDict(
        str_strip_whitespace=True,
        frozen=True,
    )