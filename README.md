Running the Django Application with Docker
Prerequisites

1) Docker
  installed

2) Docker Compose
 installed

3) .env folder with:
a .django for Django environment variables (e.g., SECRET_KEY, API keys)
b .postgres for PostgreSQL environment variables (e.g., POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD)


Steps to Run, Build and start containers
From the project root directory:
1) run :- docker-compose up --build
   
   a) This will: Build the Docker images for the Django app (web)
   
   b) Start the PostgreSQL database (db) Expose Django on http://localhost:8000

Open a new terminal and run:
1) docker-compose run web python manage.py makemigrations
2) docker-compose run web python manage.py migrate

Create a superuser
docker-compose run web python manage.py createsuperuser

Access the swagger documentation 
http://localhost:8000/api/docs/#
