from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel, EmailStr

router = APIRouter()

#Base de datos en memoria (temporal!!!!)
fake_users_db = []
user_id_counter = 1

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str

class UserResponse(BaseModel):
    id: int
    email: EmailStr

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"

# ----------- Endpoints de registro de usuario -----------
@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def register_user(payload: RegisterRequest):
    global user_id_counter

    # comprobar si existe
    for user in fake_users_db:
        if user["email"] == payload.email:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )

    new_user = {
        "id": user_id_counter,
        "email": payload.email,
        "password": payload.password,  # temporal
    }

    fake_users_db.append(new_user)
    user_id_counter += 1

    return {"id": new_user["id"], "email": new_user["email"]}


@router.post("/login", response_model=LoginResponse)
def login(payload: LoginRequest):
    for user in fake_users_db:
        if user["email"] == payload.email:
            if user["password"] == payload.password:
                return LoginResponse(access_token=f"fake-token-{user['id']}")
            else:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect password"
                )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )


