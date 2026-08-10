from .user_route import user_router
from .category_route import category_router
from .product_route import product_router
from .registration_route import registration_router

__all__ = [
    "user_router",
    "category_router",
    "product_router",
    "registration_router"
]