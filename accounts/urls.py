from django.urls import path
from .views import (UserAccountsHomeView,)
                    # crop_stock_detail_view,
                    # crop_stock_update_view, )

app_name = 'accounts'
urlpatterns = [
    path('home/', UserAccountsHomeView.as_view(), name="user_accounts_home"),
    # path('farm-crops-stock/', crop_stocks_list_view, name="crops_stock_list"),
    # path('<int:pk>/details', crop_stock_detail_view, name="crop_stock_details"),
    # path('<int:pk>/update', crop_stock_update_view, name="crop_stock_update"),
    # path('<int:pk>/delete', crop_stock_delete_view, name="farm_delete"),
]