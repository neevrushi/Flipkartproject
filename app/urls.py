from django.urls import path
from . import views
from app.views import productList,productRegister,ProductDelete,ProductUpdate
urlpatterns = [
    path("", views.index, name="index"),
    path("signup/", views.signup, name="signup"),
    path("signin/", views.signin, name="signin"),
    path("userlogout/", views.userlogout, name="userlogout"),
    path("fashionlist/", views.fashionlist, name="fashionlist"),
    path("shoeslist/", views.shoeslist, name="shoeslist"),
    path("mobilelist/", views.mobilelist, name="mobilelist"),
    path("electronicslist/", views.electronicslist, name="electronicslist"),
    path("clothlist/", views.clothlist, name="clothlist"),
    path("grocerylist/", views.grocerylist, name="grocerylist"),
    path("searchproduct/", views.searchproduct, name="searchproduct"),
    path(
        "request_password_reset/",
        views.request_password_reset,
        name="request_password_reset",
    ),
    path("reset_password/<username>/", views.reset_password, name="reset_password"),
    path("showpricerange/", views.showpricerange, name="showpricerange"),
    path("sortingbyprice/", views.sortingbyprice, name="sortingbyprice"),
    path("showcarts/", views.showcarts, name="showcarts"),
    path("addtocart/<int:productid>", views.addtocart, name="addtocart"),
    path("removecart/<int:productid>", views.removecart, name="removecart"),
    path("updateqty/<int:qv>/<int:productid>", views.updateqty, name="updateqty"),
    path("addaddress/", views.addaddress, name="addaddress"),
    path("showaddress/", views.showaddress, name="showaddress"),
    path("contact/", views.contact, name="contact"),
    path("about/", views.about, name="about"),
    path("make_payment/", views.make_payment, name="make_payment"),
    path("showorders/", views.showorders, name="showorders"),
    path("showorders/", views.showorders, name="showorders"),
    path("productRegister/",productRegister.as_view(), name="productRegister"),
    # path("productList/",productList.as_view(), name="productList"),
    path("ProductDelete/<int:pk>",ProductDelete.as_view(), name="ProductDelete"),
    path("ProductUpdate/<int:pk>",ProductUpdate.as_view(), name="ProductUpdate"),
    path("productList/", views.productList, name="productList"),




]
