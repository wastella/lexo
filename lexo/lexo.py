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

class Learner:
    def __init__(concept_list):
        self.scheduler = Scheduler()
        self.cards_dict = {}
        self.concept_idx = 0
        self.concept_list = concept_list

    def start_prac(self):
        # this is the main method, all this actually does is just pick what type of session it is, then invokes the internal method for it

    def _pick_concepts(self):
        # we need to have the scheduler tell me whats the most urgent thing to review, if theres nothing that is due then I introduce a new concept
        if self.cards_dict.length() == 0:
            due_list = {}
        else:
            due_list = {}
            for concept, card in self.cards_dict.items():
                if card.due == datetime.now(timezone.utc):
                    due_list.append((concept, card))

        if due_list.length() == 0: # then we needa introduce a new concept
            concept = self._pick_new_concept()
            return [concept]
        else:
            # Pick 1-3 most overdue concepts and return them
            num_concepts = random.randint(1, 3)
            # Sort by due date and take the num_concepts most overdue concepts
            sorted_concepts = sorted(due_list.items(), key=lambda x: x[1].due)
            return [concept for concept, _ in sorted_concepts[:num_concepts]]

    def _pick_new_concept(self):
        # needs to pick a new concept and make a new card and an entry into the dictionary
        concept = self.concept_list[self.concept_idx]
        # make the card
        new_card = Card()
        # add it to the master dict
        entry = {concept: new_card}
        self.cards_dict.update(entry)

        return concept



            

   