from fsrs import Scheduler, Card, Rating, ReviewLog
from datetime import datetime, timezone
from google import genai

# parent class for all exercises
class Exercise:
    def __init__(self, concept_name, prompt, api_key):
        self.prompt = prompt
        self.concept_name = concept_name
        self.api_key = api_key

    def _get_prompt(self):
        return self.prompt
    
    def _get_concept_name(self):
        return self.concept_name
    
    def _get_api_key(self):
        return self.api_key



