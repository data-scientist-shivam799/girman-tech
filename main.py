from fastapi import FastAPI, status
from utils.database import engine, Base
from routes import users, roles, permissions, access_validation
from fastapi.responses import JSONResponse

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

# Include routes
app.include_router(users.router)
app.include_router(roles.router)
app.include_router(permissions.router)
app.include_router(access_validation.router)

@app.get("/")
async def root():
    return JSONResponse(content={
        "message": "Welcome, the application is working!!!"
    }, status_code=status.HTTP_200_OK)