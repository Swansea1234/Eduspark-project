import os
import httpx
import json

class AIService:
    """
    A service class to interact with an AI model for generating educational content.
    """
    def __init__(self):
        # The API key is assumed to be available as an environment variable.
        # This is a placeholder for demonstration purposes.
        self.api_key = os.getenv("GEMINI_API_KEY", "")
        self.api_url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash-preview-05-20:generateContent"
        self.headers = {
            "Content-Type": "application/json",
        }

    async def generate_lesson_content(self, user_prompt: str, context: str = ""):
        """
        Generates lesson content using a large language model.

        Args:
            user_prompt: The user's query for generating content.
            context: Additional context to guide the generation.

        Returns:
            A dictionary with the generated content or an error message.
        """
        system_instruction = "Act as an expert lesson creator. Generate comprehensive and easy-to-understand lesson content."

        payload = {
            "contents": [{
                "parts": [{
                    "text": user_prompt
                }]
            }],
            "systemInstruction": {
                "parts": [{"text": system_instruction}]
            }
        }

        if context:
            payload["contents"][0]["parts"].insert(0, {"text": f"Context: {context}"})

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.api_url}?key={self.api_key}",
                    headers=self.headers,
                    data=json.dumps(payload),
                    timeout=30.0
                )
                response.raise_for_status()

                # Assuming the response format is a JSON object with 'candidates'
                response_data = response.json()
                generated_text = response_data['candidates'][0]['content']['parts'][0]['text']

                return {"status": "success", "content": generated_text}

        except httpx.HTTPStatusError as e:
            return {"status": "error", "message": f"HTTP error occurred: {e.response.status_code}"}
        except Exception as e:
            return {"status": "error", "message": f"An error occurred: {str(e)}"}

# You would instantiate and use this class in your FastAPI routes.
# Example:
# from eduspark.ai_services import AIService
# ai_service = AIService()
# @router.post("/generate")
# async def generate_content_from_prompt(prompt: LessonPrompt):
#     result = await ai_service.generate_lesson_content(user_prompt=prompt.user_query, context=prompt.context)
#     return result
