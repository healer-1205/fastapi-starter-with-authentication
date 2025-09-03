# 🚀 FastAPI Starter with Email Authentication

A robust, production-ready FastAPI starter project featuring **user registration and login via email authentication**. Built with best practices for project structure, scalability, and maintainability—perfect for quickly launching new web apps or APIs with FastAPI.

---

## 🌟 Features

- **Email Authentication**: Secure registration and login with email/password.
- **Strong Project Structure**: Modular, extensible, and easy to maintain.
- **Ready for Production**: Includes best practices for security, environment management, and API development.
- **Easy to Customize**: Clean codebase with clear separation of concerns.
- **Environment Configs**: `.env` support for configuration and secrets.
- **Async-Ready**: Fully asynchronous FastAPI stack.
- **Modern Python Tooling**: Uses `uv` for fast dependency management and `pyproject.toml` for modern Python packaging.

---

## 📦 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — lightning-fast Python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) — flexible ORM for database management
- [Alembic](https://alembic.sqlalchemy.org/) — database migrations
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [JWT](https://jwt.io/) — secure token authentication
- [Passlib](https://passlib.readthedocs.io/) — password hashing
- [Email Sending] — email verification and password reset ready
- [uv](https://github.com/astral-sh/uv) — fast Python package installer and resolver

---

## 🔥 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/healer-1205/fastapi-starter-with-authentication.git
cd fastapi-starter-with-authentication
```

### 2. Install uv (if not already installed)

```bash
pip install uv
```

### 3. Activate venv

```bash
python -m venv .venv
# in command prompt
.venv\Scripts\activate
```


### 4. Install Dependencies from pyproject.toml

```bash
uv sync
```

### 5. Create & Configure `.env`

Copy `.env.example` to `.env` and fill in your environment variables:

```bash
cp .env.example .env
# Edit .env with your editor
```

### 6. Start the App

```bash
uv run uvicorn app.main:app --reload --port 8001
```

### 7. API Docs

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive documentation.

---

## 📦 Dependency Management

This project uses `uv` for fast dependency management with `pyproject.toml`:

### Adding Dependencies

```bash
# Add a new dependency
uv pip install <package-name>

# Add a development dependency
uv pip install <package-name> --dev
```

### Managing Dependencies

```bash
# Sync environment with pyproject.toml
uv pip sync

# Update dependencies
uv pip compile --upgrade

# Run commands in the virtual environment
uv run <command>
```

### Running Scripts

```bash
# Run the application
uv run uvicorn app.main:app --reload

# Run tests
uv run pytest

# Run any Python script
uv run python app/main.py
```

---

## ✉️ Authentication Endpoints

| Endpoint               | Method | Description                     |
| ---------------------- | ------ | ------------------------------- |
| `/api/users`           | POST   | Register with email             |
| `/api/users/login`     | POST   | Login with email/password       |
| `/api/users/{user_id}` | GET    | Get current user profile        |
| `/api/users`           | GET    | Get all users from the database |
| `/api/users/{user_id}` | PUT    | Update current user profile     |
| `/api/users/{user_id}` | DELETE | Delete current user profile     |

---

## 📁 Project Structure

```
app/
├── alembic/              # Database migrations
├── controllers/           # Business logic controllers
├── middleware/           # Middleware such as token verification
├── models/               # Database models
├── routers/              # API route handlers
├── schemas/              # Pydantic schemas
├── config.py             # Configuration settings
├── dependencies.py       # Dependency injection
└── main.py              # FastAPI application entry point
tests/                    # Test files
.env.example             # Example environment variables
pyproject.toml           # Project configuration and dependencies
uv.lock                  # Locked dependency versions
```

---

## 🛡️ Security Best Practices

- Passwords are hashed with strong algorithms.
- JWT tokens for authentication.
- Environment variables for sensitive data.
- CORS and HTTPS ready.

---

## 🎯 Why Use This Starter?

- **Save hours** of setup for new FastAPI projects.
- Built-in email authentication so you can focus on features.
- Easily extensible: add OAuth, new routes, more models, etc.
- Follows clean code & SOLID principles.
- **Modern Python tooling** with `uv` for faster dependency resolution.

---

## 📬 Get Started Now!

1. **Clone, configure, and run** your new FastAPI project.
2. **Customize** as needed—add endpoints, change authentication, etc.
3. **Deploy** to your favorite cloud or serverless platform!

---

## 📝 License

[MIT](LICENSE)

---

## 🤝 Contributing

Pull requests and issues are welcome! Feel free to open a discussion or submit a PR.

---

## 🔎 SEO Keywords (for Google Search)

- FastAPI starter
- FastAPI boilerplate
- Email authentication FastAPI
- FastAPI login register example
- Production-ready FastAPI template
- Python FastAPI project structure
- Secure FastAPI starter
- uv Python package manager
- pyproject.toml FastAPI

---

**Kickstart your next FastAPI project with robust email authentication and modern Python tooling!**



