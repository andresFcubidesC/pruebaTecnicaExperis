# Prueba tecnica

Este repositorio tiene la prueba tecnica de una creacion de una api rest utilizando:
-	FastAPI: Framework principal para el desarrollo de la API.
-	PostgreSQL: Base de datos relacional para almacenar la información de los libros.
-	ORM: SQLAlchemy para interactuar con la base de datos.
-	Swagger: Generación de documentación de la API.
-	Pytest: Framework de pruebas unitarias y de integración.
-	Docker: Para contenerizar la aplicación (opcional, pero recomendado).
-	GitHub: Para alojar el código fuente.

y permite realizar las siguientes operaciones dentro de la base de datos.

-	Agregar libros: Título, autor, año de publicación, ISBN.
-	Listar libros: Todos los libros o filtrados por autor o año.
-	Actualizar información de un libro.
-	Eliminar un libro.
-	Buscar libros por título o autor.

## Índice

1. [Requirements](#Requirements)
2. [Setup](#Setup)
3. [Preguntas_adicionales](#preguntas_adicionales)


## Requirements

Antes de comenzar es necesario que se tenga los siguientes programas instalados.

- [Docker](https://www.docker.com/get-started)
- [Git](https://git-scm.com/)
- [PostgreSQL](https://www.postgresql.org/download/) 
- Python 3.9
- PgAdmin o otro motro de base de datos

## Setup

### 1. Clone the Repository

Primero clona el repositorio en tu ambiente local:

```bash
git clone https://github.com/andresFcubidesC/pruebaTecnicaExperis.git
cd your-repository-name
```

### 2. created the postgres data base
Crea una base de datos postgres, solo se necesitara el esquema, la aplicacion al actualizar el esquema correra automaticamente el modelo de base de datos.

```bash
docker pull postgres
docker run -d \
  --name my_postgres_db \
  -e POSTGRES_USER=myuser \
  -e POSTGRES_PASSWORD=mypassword \
  -e POSTGRES_DB=mydatabase \
  -p 5432:5432 \
  postgres
```

### 3. check conection to data base

corre to motor de bases de dato (el que sea que estes utilizando) y conectate a la base de datos que acabas de crear si funciona ya estas un paso mas cerca de probar la aplicacion.

### 4. update .env to you conection setting on the data base

He dejado el archivo .env como guia, si bien no es una buena practica, para el contexto de esta prueba no generara problema.
ten en cuenta la ruta ip de tu base de datos, he dejado host.docker.internal para que se pueda comunicar entre contenedores pero si ese no es tu caso cambialo.


### 5. import shcema to data base

Para tener el modelo de base de datos es necesario que cree una migracion, aqui dejo unos pasos para poder realizar la migracion

```bash
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head
```

### 6. run the aplication

He dejado un docker file, al crear la imagen y crear el contenedor tu aplicacion estara funcional.

```bash
docker build -t fastapi-app .
docker run -p 8080:8080 fastapi-app 
```

## Preguntas_adiconales

•	¿Cómo manejarías la autenticación y autorización en la API?

Eso se puede hacer por medio de:
- Tokens JWS y tokens JWT, lo cual permitirá mantener la integridad y el control del acceso a nuestras APIs.
Gateway, el cual estará encargado de orquestar y validar los requisitos de comunicación.
Incluso, se podrían dejar los microservicios dentro de nodos no accesibles a toda la red y dejar solo el gateway expuesto a la red.
- Combinación de ambas cosas, lo cual maximizará la seguridad.

•	¿Qué estrategias utilizarías para escalar la aplicación?

Por la carateristicas de este microservicio lo mejor seria un escalado horizontal, esto para evitar problemas de concurrencia, podemos utilizar Kubernetes que nos permitiria balancear la carga y escalar utomaticamente dependiendo de la demanda.

•	¿Cómo implementarías la paginación en los endpoints que devuelven listas de libros?

La paginacion normalemente se manega por medio de parametros que limiten y controlen la busquda en la base de datos, para poderle agragar a la busqueda un limite de registros una pagina en especifico.

•	¿Cómo asegurarías la seguridad de la aplicación (protección contra inyecciones SQL, XSS, etc.)?

Para prevenir este tipo de ataques, es importante seguir buenas prácticas y utilizar tecnologías como frameworks que protejan contra estas vulnerabilidades. Lo más común y mínimo que se debe hacer es:

- Validar el tipo y formato de los datos de entrada a nuestras APIs.
- Utilizar ORMs (Object-Relational Mappers) que realicen consultas de manera segura.
- Mantener los permisos de la base de datos siguiendo el principio de "menor privilegio".




