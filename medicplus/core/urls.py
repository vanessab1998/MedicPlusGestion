from django.urls import path 
from . import views

urlpatterns = [
    path("base/", views.base, name="base"),
    path("", views.index, name="index"),
    path("tomahora/", views.tomahora, name="tomahora"),
    path("contact/", views.contact, name="contact"),
    path("passr/", views.passr, name="passr"),
    path("register/", views.register, name="register"),
    path("docs/", views.docs, name="docs"),
    path("gmail/", views.gmail, name="gmail"),
    path("informeHoras/<idDoc>/", views.informeHoras, name="informeHoras"),
    path("informePagos/<idDoc>/", views.informePagos, name="informePagos"),
    path("geninfoHM/<idDoc>/", views.geninfoHM, name="geninfoHM"),
    path("geninfoPagosHM/<idDoc>/", views.geninfoPagosHM, name="geninfoPagosHM"),
    path("infoDoc/<idDoc>/", views.infoDoc, name="infoDoc"),
    path("comisiones/", views.comisiones, name="comisiones"),
    path("informeComisiones/", views.informeComisiones, name="informeComisiones"),
    path("geninfoComision/", views.geninfoComision, name="geninfoComision"),
    path("agenda/", views.agenda, name="agenda"),
    path("borrarcita/<id>/", views.borrarcita, name="borrarcita"),
    path("login/", views.login, name="login"),
]
