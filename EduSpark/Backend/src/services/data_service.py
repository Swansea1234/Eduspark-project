from typing import List, Dict, Any
from pydantic import BaseModel
import uuid

# A Pydantic model to define a basic lesson structure.
class Lesson(BaseModel):
    id: str = None
    title: str
    content: str
    owner_id: str
    is_public: bool = False

# This is a placeholder for a real database connection.
# For demonstration, we'll use an in-memory dictionary.
# In a real application, this would be a client for a database like MongoDB or Firestore.
class DataService:
    """
    A service class to handle all database operations for the application.
    """
    def __init__(self):
        # In-memory "database" for lessons.
        self._lessons_db: Dict[str, Lesson] = {}

    def get_lesson_by_id(self, lesson_id: str) -> Lesson | None:
        """
        Retrieves a single lesson by its unique ID.
        """
        return self._lessons_db.get(lesson_id)

    def get_lessons_by_owner(self, owner_id: str) -> List[Lesson]:
        """
        Retrieves all lessons belonging to a specific user.
        """
        return [lesson for lesson in self._lessons_db.values() if lesson.owner_id == owner_id]

    def create_lesson(self, lesson_data: Dict[str, Any]) -> Lesson:
        """
        Creates a new lesson and assigns it a unique ID.
        """
        lesson_id = str(uuid.uuid4())
        new_lesson = Lesson(id=lesson_id, **lesson_data)
        self._lessons_db[lesson_id] = new_lesson
        return new_lesson

    def update_lesson(self, lesson_id: str, updates: Dict[str, Any]) -> Lesson | None:
        """
        Updates an existing lesson.
        """
        lesson = self.get_lesson_by_id(lesson_id)
        if not lesson:
            return None

        for key, value in updates.items():
            setattr(lesson, key, value)
        
        return lesson

    def delete_lesson(self, lesson_id: str) -> bool:
        """
        Deletes a lesson by its unique ID.
        """
        if lesson_id in self._lessons_db:
            del self._lessons_db[lesson_id]
            return True
        return False
