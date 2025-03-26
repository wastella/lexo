from fsrs import Scheduler, Card, Rating, ReviewLog
from datetime import datetime, timezone

class Concept:
    def __init__(self, name, card, scheduler, review_log, exercise_type):
        self.name = name
        self.card = card
        self.scheduler = scheduler
        self.review_log = review_log
        self.exercise = exercise_type
    
    def _get_name(self):
        return self.name
    
    def _get_card(self):
        return self.card
    
    def _get_exercise(self):
        return self.exercise
    
    def _get_scheduler(self):
        return self.scheduler
    
    def _get_review_log(self):
        return self.review_log
    
    def run_practice(self):
        self.card, review = self.scheduler.review_card(self.card, self.exercise.run_exercise())

        self.review_log.append(review)