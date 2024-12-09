# 🚀 **Role-Based Access Control (RBAC) System with FastAPI**

This project is a simple yet powerful **Role-Based Access Control (RBAC)** system built using **FastAPI** and **SQLite**. It allows for dynamic user, role, and permission management, along with access validation and optional audit logging.

---

## ⭐ **Features**

1. **User Management**  
   - Create users  
   - Assign predefined roles: `staff`, `supervisor`, `admin`  

2. **Role Management**  
   - Predefined roles: `staff`, `supervisor`, `admin`  
   - Assign permissions dynamically (only `admin` can assign permissions)  

3. **Permission Management**  
   - Dynamically define permissions and associate them with roles and actions  

4. **Access Validation**  
   - Validate if a user has permission to perform an action on a resource  
---

## 🛠️ **Tech Stack**

- **Backend:** FastAPI  
- **Database:** SQLite  
- **Containerization:** Docker, Docker Compose  
- **API Documentation:** Postman  

---

## 📂 **Directory Structure**

```
rbac_system/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   ├── roles.py
│   │   ├── permissions.py
│   │   └── access.py
│   └── utils/
│       └── auth.py
│
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## 🚀 **Setup Instructions**

### 1. **Clone the Repository**

```bash
git clone https://github.com/yourusername/fastapi-rbac-system.git
cd fastapi-rbac-system
```

### 2. **Install Dependencies**

Using a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

### 3. **Run the Application**

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

### 4. **Run with Docker**

1. **Build the Docker Image:**

   ```bash
   docker-compose build
   ```

2. **Run the Container:**

   ```bash
   docker-compose up
   ```

Access the app at `http://localhost:8000`.

---

## 📑 **API Documentation**

The API documentation is available via Swagger UI:

```
http://localhost:8000/docs
```
