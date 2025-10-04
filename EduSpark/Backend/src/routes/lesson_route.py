from fastapi import APIRouter

# Create an APIRouter instance for lesson-related endpoints.
# The prefix ensures all routes in this file start with "/lessons".
router = APIRouter(
    prefix="/lessons",
    tags=["lessons"],
)


@router.get("/")
def get_lessons():
    """
    Retrieves a list of all lessons.
    
    In a real application, this would query a database.
    """
    # Placeholder for a database query
    lessons_list = [
        {"id": 101, "title": "Introduction to Python"},
        {"id": 102, "title": "Data Structures"},
    ]
    return {"lessons": lessons_list}


@router.get("/{lesson_id}")
def get_lesson_by_id(lesson_id: int):
    """
    Retrieves a single lesson by its ID.
    """
    # Placeholder logic to find a lesson
    if lesson_id == 101:
        return {"id": 101, "title": "Introduction to Python", "content": "This lesson covers the basics of Python."}
    elif lesson_id == 102:
        return {"id": 102, "title": "Data Structures", "content": "This lesson covers fundamental data structures."}
    else:
        return {"error": "Lesson not found"}


@router.post("/")
def create_lesson(title: str, content: str):
    """
    Creates a new lesson with the given title and content.
    """
    # Placeholder for creating a new lesson in a database
    new_lesson = {"id": 103, "title": title, "content": content}
    return {"message": "Lesson created successfully", "lesson": new_lesson}
