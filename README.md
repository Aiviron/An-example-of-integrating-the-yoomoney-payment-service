# Payment Service Integration

This project provides an integration with the YooKassa/YooMoney payment service for accepting and processing payments. It is extracted from a larger startup codebase and is designed for standalone use and further development.

## Project Structure

```
payment-service/
    app/
        app.py
        main.py
        core/
            payment_service.py
            yookassa.py
        database/
            database.py
            models/
                payment.py
                tariff.py
        schemas/
            payment.py
            yoomoney.py
    Dockerfile
    Pipfile
    Procfile
supabase/
    config.toml
    migrations/
        *.sql
```

## Quick Start

### 1. Clone the Repository

```powershell
git clone https://github.com/Aiviron/An-example-of-integrating-the-yoomoney-payment-service.git
cd An-example-of-integrating-the-yoomoney-payment-service

```

### 2. Install Dependencies

It is recommended to use [pipenv](https://pipenv.pypa.io/en/latest/):

```powershell
pip install pipenv
pipenv install
```

### 3. Environment Variables

Create a `.env` file in the payment-service directory and add the required variables (API keys, database connection, etc.):

Example:
```
YOOKASSA_SHOP_ID=your_shop_id
YOOKASSA_SECRET_KEY=your_secret_key
DATABASE_URL=your_database_url
```

### 4. Database Migrations

Apply the SQL migrations from migrations to your database:

```powershell
psql -U <user> -d <dbname> -f supabase/migrations/20250309130020_initial_schema.sql
# Repeat for other migration files
```

### 5. Run the Application

#### Locally

```powershell
pipenv run python payment-service/app/main.py
```

#### With Docker

The provided `Dockerfile` builds and runs the service:

```powershell
docker build -t payment-service payment-service/
docker run --env-file payment-service/.env -p 80:80 payment-service
```

#### With Procfile (Heroku/Render)

For deployment on Heroku/Render, use the `Procfile`:

```
web: pipenv run python app/main.py
```

## Main Files

- `app/main.py` — Application entry point.
- `core/payment_service.py` — Payment service logic.
- `core/yookassa.py` — YooKassa API integration.
- `database/models/` — Payment and tariff models.
- `schemas/` — Data serialization/validation schemas.


## Support

For questions, open an issue or contact in the GitHub profile.

