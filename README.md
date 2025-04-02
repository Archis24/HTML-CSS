# El Diario del Programador

¡Bienvenido a El Diario del Programador! Este es un proyecto donde puedes crear, ver y gestionar tus notas. También puedes registrarte e iniciar sesión para mantener tus notas seguras.

## ¿Qué puedes hacer con este proyecto?

- **Crear una cuenta:** Puedes registrarte con tu correo electrónico y una contraseña.
- **Iniciar sesión:** Una vez registrado, puedes iniciar sesión con tu correo y contraseña.
- **Crear notas:** Puedes crear nuevas notas con un título, un subtítulo y el contenido de la nota.
- **Ver notas:** Puedes ver todas las notas que has creado.
- **Ver una nota específica:** Puedes hacer clic en una nota para verla en detalle.

## ¿Cómo usar este proyecto?

### Paso 1: Registrarse

1. Abre la página de registro.
2. Introduce tu correo electrónico y una contraseña.
3. Haz clic en "Crear una cuenta".

### Paso 2: Iniciar sesión

1. Abre la página de inicio de sesión.
2. Introduce tu correo electrónico y contraseña.
3. Haz clic en "Iniciar sesión".

### Paso 3: Crear una nota

1. Una vez que hayas iniciado sesión, ve a la página de creación de notas.
2. Introduce un título, un subtítulo y el contenido de tu nota.
3. Haz clic en "Crear".

### Paso 4: Ver tus notas

1. Ve a la página principal.
2. Aquí verás una lista de todas tus notas.
3. Haz clic en una nota para verla en detalle.

## Estructura del Proyecto

- **main.py:** Este archivo contiene el código principal de la aplicación.
- **templates/:** Esta carpeta contiene las plantillas HTML para las páginas web.
  - **login.html:** Página de inicio de sesión.
  - **registration.html:** Página de registro.
  - **index.html:** Página principal donde se muestran todas las notas.
  - **create_card.html:** Página para crear una nueva nota.
  - **card.html:** Página para ver una nota específica.
- **static/css/style.css:** Este archivo contiene los estilos CSS para que las páginas se vean bonitas.

## ¿Cómo funciona el código?

### main.py

- **Rutas:** Las rutas son las diferentes páginas de la aplicación.
  - `/`: Página de inicio de sesión.
  - `/reg`: Página de registro.
  - `/index`: Página principal donde se muestran todas las notas.
  - `/card/<int:id>`: Página para ver una nota específica.
  - `/create`: Página para crear una nueva nota.
  - `/form_create`: Ruta para manejar el formulario de creación de notas.

### templates/

- **login.html:** Contiene el formulario de inicio de sesión.
- **registration.html:** Contiene el formulario de registro.
- **index.html:** Muestra todas las notas.
- **create_card.html:** Contiene el formulario para crear una nueva nota.
- **card.html:** Muestra una nota específica.

### static/css/style.css

- Contiene los estilos para que las páginas se vean bonitas y organizadas.

¡Esperamos que disfrutes usando El Diario del Programador!