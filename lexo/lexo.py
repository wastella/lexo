# Lexo class is the main class
# right now its for A1 learners to cover all of the content, then I'm going to expand it to more general stuff
# what it should do is
# 1. have a list of concepts that an A1 learner should cover, this includes vocabulary and grammar
# 2. It should have multiple practice modes, but the main thing is translating AI created spanish passages to english, and AI created english passages to spanish
# 3. Then it should give you a grade, with feedback on what you did wrong after every translation session, and chop up the AI created text into a list of words and flag ones that you didnt know.
# 4. It should then export them to like an Anki type program so that you can implement the new words the AI incorporated into your anki deck


# Here's the curriculumn for A1:
'''
1. Basic Vocabulary:
Greetings and Introductions:
Hola (Hello)

Buenos días (Good morning)

Buenas tardes (Good afternoon)

Buenas noches (Good night)

¿Cómo estás? (How are you?)

¿Qué tal? (What's up?)

Me llamo... (My name is...)

¿Cómo te llamas? (What's your name?)

Mucho gusto (Nice to meet you)

Numbers:
1-100

Basic numbers (uno, dos, tres, cuatro, etc.)

Decades (veinte, treinta, cuarenta...)

Ordinal numbers (primero, segundo, tercero...)

Days of the Week:
Lunes (Monday)

Martes (Tuesday)

Miércoles (Wednesday)

Jueves (Thursday)

Viernes (Friday)

Sábado (Saturday)

Domingo (Sunday)

Months:
Enero (January)

Febrero (February)

Marzo (March)

Abril (April)

Mayo (May)

Junio (June)

Julio (July)

Agosto (August)

Septiembre (September)

Octubre (October)

Noviembre (November)

Diciembre (December)

Common Phrases:
¿Qué hora es? (What time is it?)

¿Dónde está? (Where is it?)

¿Cuántos años tienes? (How old are you?)

¿Qué haces? (What are you doing?)

¡Hasta luego! (See you later!)

Common Verbs:
Ser (to be)

Estar (to be)

Tener (to have)

Hacer (to do/make)

Ir (to go)

Comer (to eat)

Beber (to drink)

Vivir (to live)

Hablar (to speak)

Estudiar (to study)

Basic Adjectives:
Grande (big)

Pequeño (small)

Bonito (beautiful)

Feo (ugly)

Bueno (good)

Malo (bad)

Nuevo (new)

Viejo (old)

Fácil (easy)

Difícil (difficult)

2. Basic Grammar Concepts:
Nouns and Articles:
Gender: Masculine (el) vs. Feminine (la)

Singular and plural (libro - libros, mesa - mesas)

Definite (el, la) vs. indefinite articles (un, una)

Pronouns:
Personal pronouns: yo (I), tú (you, informal), él/ella (he/she), nosotros/nosotras (we), vosotros/vosotras (you all, informal), ellos/ellas (they)

Possessive pronouns: mi (my), tu (your), su (his/her/its), nuestro/a (our), vuestro/a (your all's), su (their)

Present Tense of Regular Verbs:
-AR Verbs: Hablar (yo hablo, tú hablas, él habla, nosotros hablamos, ellos hablan)

-ER Verbs: Comer (yo como, tú comes, él come, nosotros comemos, ellos comen)

-IR Verbs: Vivir (yo vivo, tú vives, él vive, nosotros vivimos, ellos viven)

Irregular Verbs in the Present Tense:
Ser (yo soy, tú eres, él es, nosotros somos, ellos son)

Estar (yo estoy, tú estás, él está, nosotros estamos, ellos están)

Ir (yo voy, tú vas, él va, nosotros vamos, ellos van)

Tener (yo tengo, tú tienes, él tiene, nosotros tenemos, ellos tienen)

Adjectives and Agreement:
Adjectives agree in gender and number with nouns.

La casa blanca (The white house)

Los libros interesantes (The interesting books)

Simple Questions:
¿Qué? (What?)

¿Quién? (Who?)

¿Dónde? (Where?)

¿Cuándo? (When?)

¿Cómo? (How?)

¿Por qué? (Why?)

Prepositions:
En (in, on)

A (to, at)

Con (with)

Sin (without)

De (of, from)

Para (for, to)

Basic Negation:
No (no)

Nada (nothing)

Nadie (nobody)

Nunca (never)

Basic Sentence Structure:
Subject + verb + object (Yo estudio español).

Yes/no questions (¿Estudias español?)

Present Progressive (Present Continuous):
Formed with the verb "estar" + gerund (ando/iendo).

Estoy hablando (I am speaking)

Estás comiendo (You are eating)

3. Basic Vocabulary for Everyday Situations:
Family:
Madre (mother)

Padre (father)

Hermano/a (brother/sister)

Abuelos (grandparents)

Tío/a (uncle/aunt)

Food and Drinks:
Pan (bread)

Agua (water)

Fruta (fruit)

Carne (meat)

Vino (wine)

Jugo (juice)

Colors:
Rojo (red)

Azul (blue)

Verde (green)

Amarillo (yellow)

Blanco (white)

Negro (black)

Common Locations:
Casa (house)

Escuela (school)

Trabajo (work)

Tienda (store)

Restaurante (restaurant)

Calle (street)

Time-related Vocabulary:
Hoy (today)

Mañana (tomorrow)

Ayer (yesterday)

Ahora (now)

Siempre (always)

Nunca (never)
'''

from fsrs import Scheduler, Card, Rating, ReviewLog
from datetime import datetime, timezone
import random
from concept import Concept
from exercises.EngToSpanTranslationExercise import EngToSpanTranslationExercise

class Learner:
    def __init__(self, concept_list, api_key):
        self.scheduler = Scheduler()
        self.concepts = []
        self.concept_idx = 0
        self.concept_list = concept_list
        self._load_stored_concepts()  # Load any existing progress
        self.api_key = api_key

    def save(self):
        """Save the current state to disk"""
        self._store_concepts()

    def practice(self):
        # this is the main method, all this actually does is just pick what type of session it is, then invokes the internal method for it
        concept = self._pick_concepts()
        grade, description = concept.run_practice()
        print(f"Grade: {grade}, Description: {description}")
        self.save()  # Save progress after each practice session

    def _pick_concepts(self):
        # we need to have the scheduler tell me whats the most urgent thing to review, if theres nothing that is due then I introduce a new concept
        if len(self.concepts) == 0:
            due_list = []
        else:
            due_list = []
            for concept in self.concepts:
                if concept._is_due():
                    due_list.append(concept)

        if len(due_list) == 0: # then we need to introduce a new concept
            concept = self._pick_new_concept()
            return concept
        else:
            # Pick the most overdue concept and return it
            # Sort by due date and take the most overdue concept
            sorted_concepts = sorted(due_list, key=lambda x: x._get_card().due)
            return sorted_concepts[0]

    def _pick_new_concept(self): 
        # needs to pick a new concept and make a new card and an entry into the dictionary
        if self.concept_idx >= len(self.concept_list):
            return None
            
        # Get topic name and subtopics
        concept_name = self.concept_list[self.concept_idx]
        subtopics = self.concept_list[self.concept_idx + 1]
        
        # make the card
        new_card = Card()
        # add it to the lists
        new_concept = Concept(concept_name, subtopics, new_card, self.scheduler, [], EngToSpanTranslationExercise(concept_name, self.api_key))
        self.concepts.append(new_concept)
        self.concept_idx += 2   # move to the next concept (skip the subtopics list)

        return new_concept

    def _load_stored_concepts(self):
        import json
        try:
            with open("stored_concepts.json", "r") as f:
                stored_data = json.load(f)
                
                # Restore scheduler and cards
                self.scheduler = Scheduler.from_dict(stored_data["scheduler"])
                
                # Restore concepts
                for concept_data in stored_data["concepts"]:
                    card = Card.from_dict(concept_data["card"])
                    review_logs = [ReviewLog.from_dict(log) for log in concept_data["review_logs"]]
                    
                    concept = Concept(
                        concept_data["name"],
                        concept_data["subtopics"],
                        card,
                        self.scheduler,
                        review_logs,
                        EngToSpanTranslationExercise(concept_data["name"])
                    )
                    self.concepts.append(concept)
                
                self.concept_idx = stored_data["concept_idx"]
        except FileNotFoundError:
            pass
        
    def _store_concepts(self):
        import json
        stored_data = {
            "scheduler": self.scheduler.to_dict(),
            "concept_idx": self.concept_idx,
            "concepts": [{
                "name": c.name,
                "subtopics": c._get_subtopics(),
                "card": c._get_card().to_dict(),
                "review_logs": [log.to_dict() for log in c._get_review_log()]
            } for c in self.concepts]
        }
        
        with open("stored_concepts.json", "w") as f:
            json.dump(stored_data, f, indent=2)