# MyStore

A small e-commerce web app built with Flask. Products are stored in SQLite and managed through a simple admin form that supports image uploads.

## Features

- Home page and product listing
- Add products (name, price, description, stock, image) at `/admin/products/add`
- Product images uploaded to `app/static/uploads/`
- Database migrations with Flask-Migrate
- Cart and login pages are placeholders for now

## Tech stack

- Python 3.11+
- Flask
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- python-dotenv

## Getting started

1. Clone the repo and create a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create your local environment file:

   ```bash
   cp .env.example .env
   ```

   Then edit `.env` and set a real `SECRET_KEY`. You can generate one with:

   ```bash
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

4. Apply the database migrations:

   ```bash
   flask --app run db upgrade
   ```

5. Run the app:

   ```bash
   flask --app run run --debug
   ```

   Then open http://127.0.0.1:5000.

## Adding products

Visit `/admin/products/add` to add a product. Images are optional and must be JPG, JPEG, PNG, or WEBP.

## Project structure

```text
.
├── app/
│   ├── __init__.py        # app factory
│   ├── extensions.py      # db and migrate instances
│   ├── models.py          # Product model
│   ├── routes.py          # routes
│   ├── static/css/        # styles
│   └── templates/         # Jinja templates
├── migrations/            # Alembic migrations
├── config.py              # configuration (reads from .env)
├── requirements.txt
└── run.py
```

## Roadmap

- [ ] Shopping cart
- [ ] User login and registration
- [ ] Checkout
- [ ] Admin authentication
- [ ] Product editing and deletion
- [ ] Tests
