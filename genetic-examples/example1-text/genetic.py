import random
from generation import GenerationSelection

class GeneticAlgorithm(object):

    def __init__(self, population_size, target, mutate, perfect_score, output):
        self.population_size = population_size
        self.target = target
        self.mutate = mutate
        self.mating_pool = []
        self.perfect_score = perfect_score
        self.fitness = []
        self.population = self._inital_population_setup(population_size, len(target))
        self.output = output
        self.counter = 0

    def natural_selection(self):
        self.mating_pool = []
        self.fitness_score()
        self.create_new_mating_pool()
        self.create_new_population()
        return self.target_match()

    def create_new_mating_pool(self):
        #normalized_fitness = [i/sum(self.fitness) for i in self.fitness]
        #print(normalized_fitness)
        for pindex, value in enumerate(self.population):
            fit_value = self.fitness[pindex] * 100
            for findex in range(int(fit_value)):
                self.mating_pool.append(value)

    def fitness_score(self):
        self.fitness = []
        for index, value in enumerate(self.population):
            score = 0
            for tindex, t_character in enumerate(self.target):
                if t_character == value[tindex]:
                    score = score + 1
            score = score / len(self.target)
            self.fitness.append(score)

    def _inital_population_setup(self, population_length, target_length):
        population = []
        for length_population in range(population_length):
            population.append(self.new_random_indiviual(target_length))
        return population

    def create_new_population(self):
        generation_selection = GenerationSelection(self.mating_pool)
        for pindex, value in enumerate(self.population):
            self.population[pindex] = generation_selection.next_generation(self.mutate)

    def target_match(self):
        self.counter += 1
        max_fitness = max(self.fitness)
        if int(max_fitness) == self.perfect_score:
            return True
        for index, fit_value in enumerate(self.fitness):
            if fit_value == max_fitness:
                self.output.set_average_fitness(max_fitness/len(self.fitness))
                self.output.set_best_near_target(self.population[index])
        self.output.set_iteration(self.counter)
        return False

    def new_char(self):
        char_val = random.randint(63, 122)
        if char_val == 63:
            char_val = 32
        elif char_val == 64:
            char_val = 46
        return chr(char_val)

    def new_random_indiviual(self, target_length):
        string_val = ""
        for t in range(target_length):
            random_character = self.new_char()
            string_val = string_val + random_character
        return string_val
