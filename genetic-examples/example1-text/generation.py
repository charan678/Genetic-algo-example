import random


class GenerationSelection(object):

    def __init__(self, mutation_pool):
        self.mutation_pool = mutation_pool

    def _crossover(self):
        child_string = ""
        mutation_size = len(self.mutation_pool)
        parent_male = list(self.mutation_pool[random.randint(0, mutation_size - 1)])
        parent_female = list(self.mutation_pool[random.randint(0, mutation_size - 1)])
        mid_point = random.randint(0, len(self.mutation_pool[0]))
        for index, character in enumerate(parent_male):
            if index > mid_point:
                child_string = child_string + str(parent_female[index])
            else:
                child_string = child_string + str(character)
        return child_string

    def _mutate(self, crossover_generation, mutation_rate):
        for i in range(len(crossover_generation)):
            if mutation_rate >= random.uniform(0, 1):
                random_character = self.new_char()
                crossover_generation = crossover_generation[:i] + str(random_character) + crossover_generation[
                                                                                          i + 1:]
        return crossover_generation

    def next_generation(self, mutation_rate):
        crossover_generation = self._crossover()
        mutated_generation = self._mutate(crossover_generation, mutation_rate)
        return mutated_generation

    def new_char(self):
        char_val = random.randint(63, 122)
        if char_val == 63:
            char_val = 32
        elif char_val == 64:
            char_val = 46
        return chr(char_val)