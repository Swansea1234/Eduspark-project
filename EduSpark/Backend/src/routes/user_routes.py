from fastapi import APIRouter

# Create an APIRouter instance for user-related endpoints.
# The prefix ensures all routes in this file start with "/users".
router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get("/")
def get_users():
    """
    Retrieves a list of all users.
    
    In a real application, this would query a database.
    """
    # Placeholder for a database query
    users_list = [
        {"id": 1, "username": "alice"},
        {"id": 2, "username": "bob"},
    ]
    return {"users": users_list}


@router.get("/{user_id}")
def get_user_by_id(user_id: int):
    """
    Retrieves a single user by their ID.
    """
    # Placeholder logic to find a user
    if user_id == 1:
        return {"id": 1, "username": "alice"}
    elif user_id == 2:
        return {"id": 2, "username": "bob"}
    else:
        return {"error": "User not found"}


@router.post("/")
def create_user(username: str):
    """
    Creates a new user with the given username.
    """
    # Placeholder for creating a new user in a database
    new_user = {"id": 3, "username": username}
    return {"message": "User created successfully", "user": new_user}
