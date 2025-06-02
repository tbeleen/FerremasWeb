# 🛠️ FERREMAS - Plataforma Web de Comercio Electrónico
FERREMAS es una distribuidora chilena de productos de ferretería y construcción, con presencia nacional desde los años 80.
Este proyecto corresponde al desarrollo de una plataforma web de comercio electrónico, centrada en mejorar la experiencia del cliente y digitalizar
los procesos de venta y gestión interna de la empresa.
________________________________________
# 📌 Introducción
El crecimiento del rubro de la construcción en Chile ha exigido a las empresas adaptarse tecnológicamente.
FERREMAS detectó la necesidad de contar con un sitio web que facilite la venta en línea y permita mejorar los procesos 
logísticos, administrativos y contables, especialmente tras la pandemia del COVID-19.
________________________________________
# ❗ Problema Detectado
FERREMAS no contaba con una plataforma digital para realizar ventas en línea. Esto generaba:
* Menor alcance a clientes.
* Procesos manuales lentos y propensos a errores.
* Falta de trazabilidad en pedidos, pagos y entregas.
* Baja eficiencia en la gestión interna de sucursales y bodegas.
________________________________________
# ✅ Solución Propuesta
Se desarrolló una aplicación web con frontend en Django, conectada a APIs internas desarrolladas en FastAPI y Express. Esta solución permite:
* Autenticación de usuarios según su rol (cliente, vendedor, administrador, bodeguero, contador).
* Visualización de productos.
* Carrito de compras funcional.
* Selección de tipo de entrega: retiro en tienda o despacho.
* Diversos medios de pago, incluyendo integración con PayPal.
* Gestión administrativa y contable desde vistas privadas.
________________________________________
# 🧱 Arquitectura del Proyecto
* Frontend (Django): Interfaz principal para los usuarios.
* API de Usuarios (FastAPI): Manejo de autenticación, roles y seguridad.
* API de Productos (Express): Gestión y disponibilidad de productos.
________________________________________
# ⚙️ Tecnologías Utilizadas
* Frontend: Django, HTML, CSS, Bootstrap 5.3.6, JavaScript, Axios
* Reportes: ReportLab (PDF), OpenPyXL (Excel)
* APIs Internas: FastAPI (usuarios), Express (productos)
* APIs Externas: PayPal (pagos), Mindicador (valor del dólar)
________________________________________
# 📦 Instalación del Entorno
1. Clonar el repositorio

```bash
git clone https://github.com/tbeleen/ferremas.git
cd ferremas
```
2. Crear entorno virtual e instalar dependencias
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```
O bien, instalar una por una:
```bash
pip install requests
pip install django
pip install reportlab
pip install openpyxl
```
3. Instalar dependencias frontend (npm)
```bash
npm install bootstrap@5.3.6
npm install axios
```
________________________________________
# 🚀 ¿Cómo levantar el proyecto?
1.	Asegúrate de tener en funcionamiento las APIs internas:
o	Usuarios: Levantar el proyecto FastAPI con uvicorn
o	Productos: Iniciar el servidor Express
2.	Luego, desde el directorio del frontend:
```bash
python manage.py runserver
```
3.	Abre en tu navegador:
http://localhost:8000
________________________________________
# 🔗 Integración de APIs
## 📡 APIs Internas
*	FastAPI: Autenticación de usuarios, encriptación de contraseñas, gestión de roles.
*	Express: Manejo del catálogo de productos, stock y categorías.
## 🌐 APIs Externas
*	PayPal: Integración para pagos seguros en línea.
*	Mindicador: Consulta del tipo de cambio del dólar en tiempo real para mostrar precios referenciales.
________________________________________
# 📌 Conclusión
El desarrollo de este sistema de comercio electrónico permite a FERREMAS ampliar su alcance comercial, optimizar sus operaciones internas y ofrecer una experiencia de compra moderna y eficiente. Esta solución modular y escalable prepara a la empresa para competir en el mercado digital, integrar nuevas funcionalidades y crecer a nivel nacional.

Link dirve: 
* https://drive.google.com/drive/folders/1lkPvWTTVWj3MsBdtiUJetwczXnkziltn?usp=sharing
