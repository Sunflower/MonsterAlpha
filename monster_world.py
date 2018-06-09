from monster_alpha import Monster
import random
import string
import atexit

class MonsterWorld:
    def __init__(self, num_mons):
        self.mons = []
        for i in range(num_mons):
            mon = Monster(0)
            self.mons.append(mon)

        self.update_world()

    def update_world(self):
        self.set_fitnesses()
        self.calc_pop_fitness()
        self.normalize_fitnesses()
        self.calc_probs()

    def breed(self, generation):
        parent1 = self.select()
        parent2 = self.select()

        genome1 = parent1.genome
        genome2 = parent2.genome

        i = len(genome1)//2

        new_genome1, new_genome2 = self.cross_over(genome1, genome2, i)
        parent1.successes += 1
        parent2.successes += 1

        child1 = Monster(generation, new_genome1)
        child2 = Monster(generation, new_genome2)

        self.mons.append(child1)
        self.mons.append(child2)

    def cross_over(self, genome1, genome2, i):
        new_genome1 = genome1[:i] + genome1[i:]
        new_genome2 = genome2[:i] + genome1[i:]

        return new_genome1, new_genome2

    def mating_season(self, fun, generation):
        for i in range(fun):
            self.breed(generation)
            self.update_world()

    def select(self):
        rand = random.random()

        for i in range(len(self.mons)):
            if rand < self.probs[i]:
                return self.mons[i]

    def set_fitnesses(self):
        # TODO
        for mon in self.mons:
            fitness = 0
            for bp in mon.genome:
                if bp == 'A':
                    fitness += 1
            mon.fitness = fitness

    def calc_pop_fitness(self):
        pop_fitness = 0
        for mon in self.mons:
            pop_fitness += mon.fitness
        self.pop_fitness = pop_fitness

    def normalize_fitnesses(self):
        self.norm_fitnesses = [mon.fitness/self.pop_fitness for mon in self.mons]

    def calc_probs(self):
        self.probs = [sum(self.norm_fitnesses[:i+1]) for i in range(len(self.norm_fitnesses))]

    def natural_selection(self, trim):
        sorted_mons = sorted(self.mons, key=(lambda mon: mon.fitness))
        self.mons = sorted_mons[trim:]
        #print([mon.genome for mon in self.mons])

        self.update_world()

    def mutate(self, genome):
        strlen = len(genome)
        bp = random.randint(0,strlen-1)
        snv = ''.join(random.choices(string.ascii_uppercase, k=1))
        genome_list = list(genome)
        genome_list[bp] = snv
        return "".join(genome_list)

    def new_gen(self, generation):
        num_mons = len(self.mons)
        nw.mating_season(num_mons, generation)
        nw.natural_selection(2*num_mons)
        for mon in self.mons:
            mon.genome = self.mutate(mon.genome)

nw = MonsterWorld(100)
def test_world():
    for i in range(10000):
        print(nw.select().fitness)
        # print(nw.probs)
        # print([mon.genome for mon in nw.mons])
        #print(i)
        nw.new_gen(i)
    print(nw.select().genome)

try:
    test_world()
except KeyboardInterrupt:
    print(nw.select().genome)
    print(Monster.base_phenotypes)
