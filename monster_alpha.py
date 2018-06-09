import secrets
import random
import string

class Monster:



    def __init__(self, generation, genome=None):
        self.successes = 0

        if genome is None:
            #self.genome = secrets.token_hex(8)
            self.genome = ''.join(random.choices(string.ascii_uppercase, k=100))
        else:
            self.genome = genome

        self.generation = generation

        self.fitness = 0

        self.body = {
            'heads': 0,
            'arms': 0,
            'legs': 0,
            'height': 0,
            'eyes': 0,
            'hair': 0,
            'colour': 0
        }
        self.build_body()

    def build_body(self):
        #print(self.base_phenotypes)
        self.base_phenotypes['eyes'] = self.genome[0]
