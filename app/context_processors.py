import requests

def carrito_context(request):
    carrito = request.session.get("carrito", [])
    productos = []

    for item in carrito:
        try:
            response = requests.get(f"http://localhost:3000/productos/{item['id_producto']}")
            producto = response.json()
            producto["cantidad"] = item["cantidad"]
            producto["subtotal"] = producto["precio_prod"] * item["cantidad"]
            productos.append(producto)
        except Exception:
            continue 

    return {
        "carrito_productos": productos,
        "carrito_cantidad_total": sum(p["cantidad"] for p in productos)
    }
