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

---

## 📦 Tech Stack

- [FastAPI](https://fastapi.tiangolo.com/) — lightning-fast Python web framework
- [SQLAlchemy](https://www.sqlalchemy.org/) — flexible ORM for database management
- [Alembic](https://alembic.sqlalchemy.org/) — database migrations
- [Pydantic](https://docs.pydantic.dev/) — data validation
- [JWT](https://jwt.io/) — secure token authentication
- [Passlib](https://passlib.readthedocs.io/) — password hashing
- [Email Sending] — email verification and password reset ready

---

## 🔥 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/healer-1205/fastapi-starter-with-authentication.git
cd fastapi-starter-with-authentication
```

### 2. Create & Configure `.env`

Copy `.env.example` to `.env` and fill in your environment variables:

```bash
cp .env.example .env
# Edit .env with your editor
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the App

```bash
uvicorn app.main:app --reload
```

### 5. API Docs

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive documentation.

---

## ✉️ Authentication Endpoints

| Endpoint                 | Method | Description                |
|--------------------------|--------|---------------------------------|
| `/api/users`             | POST   | Register with email             |
| `/api/users/login`       | POST   | Login with email/password       |
| `/api/users/{user_id}`   | GET    | Get current user profile        |
| `/api/users`             | GET    | Get all users from the database |
| `/api/users/{user_id}`   | PUT    | Update current user profile     |
| `/api/users/{user_id}`   | DELETE | Delete current user profile     |

---

## 📁 Project Structure

```
app/
├── controllers/           
├── middleware/          # middleware such as token verification
├── models/            
├── routers/       
├── schemas/       
├── config.py      
├── dependencies.py
├── main.py        
tests/             
.env.example       # Example environment variables
requirements.txt
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

---

**Kickstart your next FastAPI project with robust email authentication and solid foundations!**
