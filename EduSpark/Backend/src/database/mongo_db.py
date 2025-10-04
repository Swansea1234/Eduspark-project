from typing import List, Dict, Any
from motor.motor_asyncio import AsyncIOMotorClient
from bson import ObjectId
from pydantic import BaseModel, Field, BeforeValidator
from typing import Optional

# Custom validator to convert BSON ObjectId to a string
PyObjectId = BeforeValidator(str)

# A Pydantic model for a lesson, with a special ID field for MongoDB.
class Lesson(BaseModel):
    id: Optional[PyObjectId] = Field(alias="_id", default=None)
    title: str
    content: str
    owner_id: str
    is_public: bool = False

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class MongoDBService:
    """
    A service class to handle database operations using a MongoDB connection.
    This class uses the motor library for asynchronous operations.
    """
    def __init__(self, db_url: str = "mongodb://localhost:27017/", db_name: str = "eduspark"):
        self.client = AsyncIOMotorClient(db_url)
        self.db = self.client[db_name]
        self.lessons_collection = self.db.lessons

    async def get_lesson_by_id(self, lesson_id: str) -> Optional[Lesson]:
        """
        Retrieves a single lesson by its unique ID.
        """
        lesson_data = await self.lessons_collection.find_one({"_id": ObjectId(lesson_id)})
        if lesson_data:
            return Lesson(**lesson_data)
        return None

    async def get_lessons_by_owner(self, owner_id: str) -> List[Lesson]:
        """
        Retrieves all lessons belonging to a specific user.
        """
        lessons = []
        async for lesson_data in self.lessons_collection.find({"owner_id": owner_id}):
            lessons.append(Lesson(**lesson_data))
        return lessons

    async def create_lesson(self, lesson_data: Lesson) -> Lesson:
        """
        Creates a new lesson and inserts it into the database.
        """
        new_lesson = lesson_data.model_dump(by_name=True, exclude={"id"})
        result = await self.lessons_collection.insert_one(new_lesson)
        lesson_data.id = result.inserted_id
        return lesson_data

    async def update_lesson(self, lesson_id: str, updates: Dict[str, Any]) -> Optional[Lesson]:
        """
        Updates an existing lesson.
        """
        update_result = await self.lessons_collection.update_one(
            {"_id": ObjectId(lesson_id)},
            {"$set": updates}
        )
        if update_result.modified_count == 1:
            return await self.get_lesson_by_id(lesson_id)
        return None

    async def delete_lesson(self, lesson_id: str) -> bool:
        """
        Deletes a lesson by its unique ID.
        """
        result = await self.lessons_collection.delete_one({"_id": ObjectId(lesson_id)})
        return result.deleted_count == 1
