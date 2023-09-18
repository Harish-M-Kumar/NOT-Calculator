from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('math', views.math, name='math'),
    path('conversion', views.conversion, name='conversions'),
    path('health', views.health, name="health"),
    path('currency', views.currency, name="currency"),

    # for math
    path('add', views.add, name="add"),
    path('subtract', views.subtract, name="subtract"),
    path('multiplicaion', views.multiplicaion, name="multiplicaion"),
    path('division', views.division, name="division"),
    path('integration', views.integration, name="integration"),
    path('differentiation', views.differentiation, name="differentiation"),

    # for health
    path('bmi', views.bmi, name='bmi'),
    path('calorie', views.calorie, name='calorie'),

    #for converstion
    path('km_mi', views.kmMi, name="kmMi"),
    path('kg_lb', views.kgLb, name="kgLb"),
    path('m_f', views.meFeet, name="meFeet"),
    path('binary', views.binary, name="binary"),
    path('octal', views.octal, name="octal"),
    path('hexa', views.hexa, name="hexa"),

    #for currency
    path('inr', views.inr, name="inr"),
    path('usd', views.usd, name="usd"),
    path('aud', views.aud, name="aud"),
    path('pound', views.pound, name="pound")
]