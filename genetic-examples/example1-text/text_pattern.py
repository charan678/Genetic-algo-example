from genetic import GeneticAlgorithm
from output import Output


if __name__ == "__main__":
    print("Genetic Algorithms ..........")
    population_size = 150
    mutation_rate = 0.02
    perfect_score = 1
    target = "Fc Barcelona"
    output_object = Output(target, mutation_rate)
    genetic = GeneticAlgorithm(population_size, target, mutation_rate, perfect_score, output_object)

    while True:
        finished = genetic.natural_selection()
        if finished:
            break
        output_object.print_pretty_output()
    print(" -----------------------      ------------------------------------------")
    print(" -----------------------  SUCCESS    ------------------------------------------")
    print(" -----------------------      ------------------------------------------")
