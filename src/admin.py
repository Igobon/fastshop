from src.users.admin import register_hr_admin_views
from src.orders.admin import register_order_admin_views
from src.baskets.admin import register_basket_admin_views

def register_admin_views(admin):
    register_hr_admin_views(admin=admin)
    register_order_admin_views(admin=admin)
    register_basket_admin_views(admin=admin)