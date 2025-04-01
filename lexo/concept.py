from fsrs import Scheduler, Card, Rating, ReviewLog
from datetime import datetime, timezone

class Concept:
    def __init__(self, name, subtopics, card, scheduler, review_log, exercise_type):
        self.name = name
        self.subtopics = subtopics
        self.card = card
        self.scheduler = scheduler
        self.review_log = review_log
        self.exercise = exercise_type
    
    def _get_name(self):
        return self.name
    
    def _get_subtopics(self):
        return self.subtopics
    
    def _get_card(self):
        return self.card
    
    def _get_exercise(self):
        return self.exercise
    
    def _get_scheduler(self):
        return self.scheduler
    
    def _get_review_log(self):
        return self.review_log
    
    def run_practice(self):
        grade, description = self.exercise.run_exercise(self.subtopics)
        rating = Rating(grade)
        self.card, review = self.scheduler.review_card(self.card, rating)

        self.review_log.append(review)
        return grade, description

    def _is_due(self):
        return self.card.due == datetime.now(timezone.utc)