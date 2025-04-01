from exercises.exercise import Exercise
from google import genai

class EngToSpanTranslationExercise(Exercise):
    def __init__(self, concept_name, api_key):
        super().__init__(concept_name, "Generate a short story, 2-3 sentences long, that contains the following topics/words, all ENGLISH, no extra words, no extra punctuation other than normal english. The goal is to let me translate it into spanish, so please make sure its all in English:", api_key)

    def run_exercise(self, subtopics):
        # needs to return one of these:
        # Rating.Again (==1) forgot the card
        # Rating.Hard (==2) remembered the card with serious difficulty
        # Rating.Good (==3) remembered the card after a hesitation
        # Rating.Easy (==4) remembered the card easily
        story = self._generate_story(subtopics)
        self._display_story(story)
        correct_translation = self._get_translation(story)
        learner_translation = self._get_learner_translation()
        return self._grade_translation(correct_translation, learner_translation, story)


    def _generate_story(self, subtopics):
        client = genai.Client(api_key=self._get_api_key())
        prompt = f"""Create a very simple English sentence using these basic greetings/phrases.
Keep it extremely basic - just like speaking to a beginner.
No complex tenses, no complex structure.

Spanish words to include: {', '.join(subtopics)}

Example output:
"Hello, good morning. How are you? Nice to meet you."

Your turn (make it different from the example) AND NO MATTER WHAT DO NOT ADD ANYTHING IN SPANISH:"""
        
        story = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        return story

    def _display_story(self, story):
        print(story.text)

    def _get_translation(self, story):
        client = genai.Client(api_key=self._get_api_key())
        translation = client.models.generate_content(
            model="gemini-2.0-flash", contents="Translate the following story to spanish: " + story.text
        )
        return translation

    def _get_learner_translation(self):
        # needs to return the learner's translation of the story
        return input("Please translate the story to spanish: ")

    def _grade_translation(self, correct_translation, learner_translation, story):
        # needs to return one of these:
        # Rating.Again (==1) forgot the card
        # Rating.Hard (==2) remembered the card with serious difficulty
        # Rating.Good (==3) remembered the card after a hesitation
        # Rating.Easy (==4) remembered the card easily
        client = genai.Client(api_key=self._get_api_key())
        grade = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents="""Return ONLY a valid JSON object in this exact format (no markdown, no backticks):
{
    "grade": <number 1-4>,
    "explanation": "<brief explanation of grade>"
}

Where grade follows these rules:
1 = forgot/incorrect translation
2 = serious difficulty/major mistakes
3 = minor mistakes/hesitation
4 = perfect/near perfect

Original English: """ + story.text + """
Correct Spanish: """ + correct_translation.text + """
Learner's Spanish: """ + learner_translation
        )

        response_text = grade.text.strip()
        if response_text.startswith('```'):
            response_text = response_text.split('\n', 1)[1]  
        if response_text.endswith('```'):
            response_text = response_text.rsplit('\n', 1)[0] 
        if response_text.startswith('json'):
            response_text = response_text.split('\n', 1)[1] 
            
        # print(response_text)
        
        try:
            import json
            result = json.loads(response_text)
            return result["grade"], result["explanation"]
        except (json.JSONDecodeError, KeyError) as e:
            print(f"Error parsing JSON: {e}")
            return 1, "Error processing response. Please try again."
