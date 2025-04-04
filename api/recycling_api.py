import os
from dotenv import load_dotenv
import google.generativeai as genai

class RecyclingAPI:
    def __init__(self, api_key=None):
        load_dotenv()  # Load from .env file
        self.api_key = api_key or os.getenv("api_key")  # Pull from environment

        if not self.api_key:
            raise ValueError("API key not found. Please set 'api_key' in your .env file.")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel("gemini-2.0-flash")

    def get_recycling_info(self, item):
        try:
            prompt = (
                f"Provide clear and concise recycling instructions for '{item}'. "
                "Focus on how to dispose of it properly, including whether it can go in a recycling bin or requires special handling."
            )
            response = self.model.generate_content(prompt)
            raw_response = response.text.strip()
            modified_response = self._modify_response(raw_response)
            return modified_response
        except Exception as e:
            return f"Error fetching info: {str(e)}. Default: Check local guidelines for '{item}'."

    def _modify_response(self, response):
        return response
