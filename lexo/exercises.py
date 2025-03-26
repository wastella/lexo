from fsrs import Scheduler, Card, Rating, ReviewLog
from datetime import datetime, timezone

# parent class for all exercises
class Exercise:
    def __init__(self, concept_name, prompt):
        self.prompt = prompt
        self.concept_name = concept_name

    def _get_prompt(self):
        return self.prompt
    
    def _get_concept_name(self):
        return self.concept_name

class EngToSpanTranslationExercise(Exercise):
    def __init__(self, concept_name):
        super().__init__(concept_name, "Generate me a short story in english that a spanish learner could translate to spanish, that would test/help the learner learn about the following subject: ")

    def run_exercise(self):
        # needs to return one of these:
        # Rating.Again (==1) forgot the card
        # Rating.Hard (==2) remembered the card with serious difficulty
        # Rating.Good (==3) remembered the card after a hesitation
        # Rating.Easy (==4) remembered the card easily
        self._generate_story()
        self._display_story()
        self._get_translation()
        return self._grade_translation()


    def _generate_story(self):
        pass

    def _display_story(self):
        pass

    def _get_translation(self):
        pass

    def _grade_translation(self):
        # needs to return one of these:
        # Rating.Again (==1) forgot the card
        # Rating.Hard (==2) remembered the card with serious difficulty
        # Rating.Good (==3) remembered the card after a hesitation
        # Rating.Easy (==4) remembered the card easily
        pass

    

