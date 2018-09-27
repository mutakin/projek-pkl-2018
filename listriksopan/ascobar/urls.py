from django.urls import path,include
from . import views

urlpatterns = [
	path('',views.index, name='home'),
	path('paket/',views.paket),
	path('faq/',views.faq),
	path('projects/',views.projects),
	path('listrik_sopan/',views.listrik_sopan),
	path('kontak/',views.kontak),
]



