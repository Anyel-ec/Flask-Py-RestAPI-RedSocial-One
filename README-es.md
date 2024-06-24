# **Select Language:** 🌍
- [Español (Spanish)](README-es.md)
- [English](README.md)

# Gestión de Usuarios, Publicaciones y Categorías en Flask

Este proyecto Flask proporciona una API para gestionar usuarios, publicaciones y categorías, siguiendo un enfoque de arquitectura en capas.

## RESULTS
## REST CONSUMER
### Insomia Flask
![Alt text](api_docs/docs.PNG)
![Alt text](api_docs/insomia_flask.PNG)

## Características

- **Usuarios**: Crear, recuperar, actualizar y eliminar perfiles de usuario.
- **Publicaciones**: Crear, recuperar, actualizar y eliminar publicaciones.
- **Categorías**: Crear, recuperar, actualizar y eliminar categorías.

## Requisitos

- Python 3.8+
- Flask
- Flask-CORS

## Instalación

1. Clonar el repositorio:
    ```sh
    git clone https://github.com/Anyel-ec/Flask-Py-RestAPI-RedSocial-One
    cd Flask-Py-RestAPI-RedSocial-One
    ```

2. Crear y activar un entorno virtual:
    ```sh
    python -m venv env
    source env/bin/activate  # En Windows utiliza `env\Scripts\activate`
    ```

3. Instalar dependencias:
    ```sh
    pip install -r requirements.txt
    ```

4. Configurar e inicializar la base de datos:
    ```sh
    # Agregar instrucciones para la inicialización de la base de datos si es aplicable
    ```

5. Ejecutar el servidor de desarrollo:
    ```sh
    python app.py
    ```

## Arquitectura

Este proyecto sigue una arquitectura en capas:

1. **Controladores**: Manejan las solicitudes y respuestas HTTP.
2. **Servicios**: Implementan la lógica empresarial y las reglas de la aplicación.
3. **Repositorios**: Gestionan el acceso a datos y la persistencia.

## Principales Endpoints

### Usuarios

- `POST /api/users/`: Crear un nuevo usuario.
- `GET /api/users/<user_id>`: Recuperar un usuario específico.
- `GET /api/users/`: Recuperar todos los usuarios.
- `PUT /api/users/<user_id>`: Actualizar un usuario específico.
- `DELETE /api/users/<user_id>`: Eliminar un usuario específico.
- `POST /api/users/<user_id>/verify`: Verificar contraseña de usuario.
- `POST /api/users/verify`: Verificar credenciales de inicio de sesión.

### Publicaciones

- `POST /api/posts/`: Crear una nueva publicación.
- `GET /api/posts/<post_id>`: Recuperar una publicación específica.
- `GET /api/posts/`: Recuperar todas las publicaciones.
- `PUT /api/posts/<post_id>`: Actualizar una publicación específica.
- `DELETE /api/posts/<post_id>`: Eliminar una publicación específica.
- `GET /api/posts/by_user/<user_id>`: Recuperar publicaciones por usuario.
- `GET /api/posts/by_email/<email>`: Recuperar publicaciones por correo electrónico de usuario.

### Categorías

- `POST /api/categories/`: Crear una nueva categoría.
- `GET /api/categories/<category_id>`: Recuperar una categoría específica.
- `GET /api/categories/`: Recuperar todas las categorías.
- `PUT /api/categories/<category_id>`: Actualizar una categoría específica.
- `DELETE /api/categories/<category_id>`: Eliminar una categoría específica.

## Uso

Para probar la API, utiliza herramientas como Postman o `curl` para realizar solicitudes HTTP a los endpoints mencionados anteriormente.

## Insomnia JSON

Para facilitar las pruebas, importa el archivo JSON de Insomnia proporcionado `insomnia_export.json` en Insomnia. Este archivo contiene solicitudes preconfiguradas para todos los endpoints mencionados anteriormente.

## Contribuciones

¡Las contribuciones son bienvenidas! Sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agregar nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un nuevo Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
