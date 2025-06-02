from django.urls import path
from .views import *
from app import views

urlpatterns = [
    path('', index, name='index'),
    path('bodeguero/', bodeguero, name='bodeguero'),
    path('pedido/en_preparacion/<int:id_pedido>/', marcar_pedido_en_preparacion, name='aceptar_pedido'),
    path('pedido/listo/<int:id_pedido>/', marcar_pedido_listo_entregar, name='marcar_pedido_listo_entregar'),

    path('catalogo/', catalogo, name='catalogo'),
    path('contador/', contador, name='contador'),
    path('transferencia/confirmar/<int:id>/', confirmar_transferencia, name='confirmar_transferencia'),
    path('transferencia/rechazar/<int:id>/', rechazar_transferencia, name='rechazar_transferencia'),
    path('vendedor/', vendedor, name='vendedor'),
    path('vendedor/pedido/<int:id_pedido>/<int:tipo_entrega>/', actualizar_estado_pedido_vendedor, name='actualizar_estado_pedido_vendedor'),
    path('cliente/', cliente, name='cliente'),
    path('base/', base, name='base'),

    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('cambiar-clave/', views.cambiar_clave, name='cambiar_clave'),
    
    path('crear_admin/', crear_admin, name='crear_admin'),
    path('administrador/', administrador, name='administrador'),
    path('agregarTrab/', agregarTrab, name='agregarTrab'),
    path('detalleTrab/<str:rut_buscar>/', detalleTrab, name='detalleTrab'),
    path('detalleCliente/<str:rut_buscar>/', detalleCliente, name='detalleCliente'),
    path('eliminar_trabajador/<str:rut>/', eliminar_trabajador, name='eliminar_Trabajador'),
    path('modificar_trabajador/<str:rut>/', views.modificar_trabajador, name='modificar_trabajador'),
    path('modificarCliente/<str:rut>/', views.modificar_cliente, name='modificar_cliente'),

    path('carrito/', carrito, name='carrito'),
    path('checkout/', checkout, name='checkout'),
    path("agregar/<int:producto_id>/", agregar_al_carrito, name="agregar_al_carrito"),
    path("carrito/eliminar/<int:producto_id>/", eliminar_del_carrito, name="eliminar_del_carrito"),
    path("carrito/reducir/<int:producto_id>/", reducir_cantidad, name="reducir_cantidad"),
    path("carrito/aumentar/<int:producto_id>/", aumentar_cantidad, name="aumentar_cantidad"),
    path("mis_pedidos/", mis_pedidos, name="mis_pedidos"),
    path("paypalCompra/", paypalCompra , name="paypalCompra"),
    path("vaciar-carrito/", vaciar_carrito, name="vaciar_carrito"),
    path('pago-transferencia/', pago_transferencia, name='pago_transferencia'),
    path('agregarTrab/', agregarTrab, name='agregarTrab'),

    path('equiposMedicion/', equiposMedicion, name='equiposMedicion'),
    path('fijaciones_y_adhesivos/', fijaciones_y_adhesivos, name='fijaciones_y_adhesivos'),
    path('herramientasManu/', herramientasManu, name='herramientasManu'),
    path('herramientasElec/', herramientasElec, name='herramientasElec'),
    path('materialesBasic/', materialesBasic, name='materialesBasic'),
    path('tornillo_y_anclaje/', tornillo_y_anclaje, name='tornillo_y_anclaje'),
    path('equiposSeguridad/', equiposSeguridad, name='equiposSeguridad'),
    path('detalle_producto/<int:id_producto>/', detalle_producto, name='detalle_producto'),
    path('logout/', logout, name='logout'),

    path("recuperar_contrasena/", recuperar_contrasena, name="recuperar_contrasena"),
    path('restablecer_contrasena/<str:rut>/', views.restablecer_contrasena, name='restablecer_contrasena'),

    path('checkout/procesar/', procesar_checkout, name='procesar_checkout'),
    path('checkout/paypalCompra/', paypalCompra, name='paypalCompra'),
    path('finalizar_pago_paypal/', finalizar_pago_paypal, name='finalizar_pago_paypal'),
    path('boleta/<int:id_pedido>/', views.descargar_boleta, name='descargar_boleta'),
    path('marca/<int:id_marca>/', views.productos_por_marca, name='productos_por_marca'),

    path('informes/', views.informes, name='informes'),
    path('informes/descargar/pagos/', views.descargar_excel_pagos, name='descargar_excel_pagos'),
    path('informes/descargar/pedidos/', views.descargar_excel_pedidos, name='descargar_excel_pedidos'),
    path('informes/descargar/productos/', views.descargar_excel_productos, name='descargar_excel_productos'),


    path('eliminar_pedido/<int:id_pedido>/', views.eliminar_pedido, name='eliminar_pedido'),

    path('aplicar-cupon/', views.aplicar_cupon, name='aplicar_cupon'),

    path('cupon/validar', views.validar_cupon, name='validar_cupon'),

    path('eliminar-cupon/', views.eliminar_cupon, name='eliminar_cupon'),
]
