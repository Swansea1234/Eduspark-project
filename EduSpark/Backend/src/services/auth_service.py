from fastapi import HTTPException, status
from pydantic import BaseModel

# A Pydantic model to define the data structure for user credentials.
class UserCredentials(BaseModel):
    username: str
    password: str

# This is a simple placeholder service. In a real application,
# you would connect to a database and use proper password hashing.
class AuthService:
    """
    A service class to handle user authentication logic.
    """
    def __init__(self):
        # A simple in-memory "database" for demonstration purposes.
        self.users_db = {}

    def signup(self, credentials: UserCredentials):
        """
        Registers a new user.
        """
        if credentials.username in self.users_db:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Username already exists"
            )
        
        # In a real app, hash the password before storing it.
        self.users_db[credentials.username] = credentials.password
        return {"message": "User registered successfully"}

    def login(self, credentials: UserCredentials):
        """
        Authenticates a user and returns a token.
        """
        stored_password = self.users_db.get(credentials.username)
        if not stored_password or stored_password != credentials.password:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid credentials"
            )
        
        # Placeholder for a generated JWT or session token.
        mock_token = f"fake_token_for_{credentials.username}"
        return {"access_token": mock_token, "token_type": "bearer"}

    def verify_token(self, token: str):
        """
        Verifies a user's token.
        """
        # This is a very simple verification. A real token would be decoded.
        if token.startswith("fake_token_for_"):
            username = token.replace("fake_token_for_", "")
            return {"username": username, "is_valid": True}
        
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
