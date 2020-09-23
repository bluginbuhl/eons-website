# EONS Website Repository

### Local Development

Requires [Docker](https://www.docker.com/) to be installed.

Clone the repo, then move into the `eons_backend` directory and run `docker-compose`

```
$ git clone https://github.com/bluginbuhl/eons-website.git && cd eons-website
```

Create the appropriate `.env` file for `django-environ` to work with

```
touch eons_backend/config/.env
```

Add the appropriate environment variables to `.env`. (See `eons_backend/config/.env.example`; you may need to generate a new key with `secrets`, see below.)

Build the Docker containers in `eons_backend`.

```
$ cd eons_backend && docker-compose up --build
```

The containers will be build and the packages from `Pipfile` will be installed into the `web` container. The database is Postgresql.

Once the containers are finished building, you should be able to see the site at [http://localhost:8000/](http://localhost:8000/).

If you do not see the website, or otherwise get an error, try running `docker-compose logs` to debug.

#### Generating a SECRET_KEY

Copy the output of the following command and store it in `.env` as `DJANGO_SECRET_KEY`

```
$ python -c 'import secrets; print(secrets.token_urlsafe(38))'
```