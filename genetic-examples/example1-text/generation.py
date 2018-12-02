import random


class GenerationSelection(object):

    def __init__(self, mutation_pool):
        self.mutation_pool = mutation_pool

    def _crossover(self):
        mutation_size = len(self.mutation_pool)
        parent_male = self.mutation_pool[random.randint(0, mutation_size -1 )]
        parent_female = self.mutation_pool[random.randint(0, mutation_size -1)]
        mid_point = len(self.mutation_pool) % 2
        crossover_genes_male = len(parent_male) // 2
        crossover_genes_female = len(parent_female) // 2 + mid_point
        crossover_generation = parent_male[:crossover_genes_male] + parent_female[:crossover_genes_female]
        return crossover_generation

    def _mutate(self, crossover_generation, mutation_rate):
        for i in range(len(crossover_generation)):
            if (mutation_rate*10) <= random.randint(0,10):
                random_character = self.new_char()
                mutated_generation = crossover_generation[:i] + str(random_character) + crossover_generation[
                                                                                              i + 1:]
        return mutated_generation

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