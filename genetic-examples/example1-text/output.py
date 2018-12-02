class Output(object):
    class Meta:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'

    def __init__(self, target_match, mutation_rate):
        self.target_match = target_match
        self.mutation_rate = mutation_rate
        self.iterations = 0
        self.average_fitness = 0
        self.best_near_target = ""

    def set_iteration(self, iteration):
        self.iterations = iteration

    def set_average_fitness(self, average_fitness):
        self.average_fitness = average_fitness

    def set_best_near_target(self, near_target):
        self.best_near_target = near_target

    def print_pretty_output(self):
        #print(self.Meta.OKGREEN + "------------------------------------------------------------")
        # print(self.Meta.BOLD + "Number of Iteration/generations = " + self.Meta.OKBLUE + self.iterations)
        # print(self.Meta.BOLD + "Number of target string = " + self.Meta.OKBLUE + self.target_match)
        # print(self.Meta.BOLD + "Number of average fitness = " + self.Meta.OKBLUE + self.average_fitness)
        # print(self.Meta.BOLD + "Number of mutation rate = " + self.Meta.OKBLUE + self.mutation_rate)
        # print(self.Meta.OKGREEN + "--------------------        END         -----------------------")

        print("Number of Iteration/generations = " + str(self.iterations))
        print("Number of target string = "  + str(self.target_match))
        print("Number of average fitness = "  + str(self.average_fitness))
        print("Number of mutation rate = " + str(self.mutation_rate))
        print("Number of mutation rate = " + self.best_near_target)
        print("--------------------        END         -----------------------")
