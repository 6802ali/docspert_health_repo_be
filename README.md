Running the Django Application with Docker
Prerequisites

Docker
 installed

Docker Compose
 installed

A .env folder with:

.django for Django environment variables (e.g., SECRET_KEY, API keys)

.postgres for PostgreSQL environment variables (e.g., POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD)


Steps to Run

Build and start containers

From the project root directory:

docker-compose up --build

This will:

Build the Docker images for the Django app (web)

Start the PostgreSQL database (db)

Expose Django on http://localhost:8000

Open a new terminal and run:
docker-compose run web python manage.py makemigrations
docker-compose run web python manage.py migrate

Create a superuser

Run the following command to create an admin user:
docker-compose run web python manage.py createsuperuser
