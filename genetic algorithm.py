import random

population_size = 100 #we have 100 solutions
genome_length = 200 #legnth of indivudual solutions = 20 (20 positions in array)
mutation_rate = 0.01 #probablility of mutation happening
crossover_rate = 0.7 #likehood of crossover happening instead of just returning the parents = 70%
generations = 200 #process is repeated 200 times

#returns a random genome as initilization
def random_geome(length):
    return [random.randint(0,1) for _ in range(length)] #random integer btwn 0 and 1  (generates bits)

def init_population(population_size, geonome_length):
    return [random_geome(genome_length) for _ in range(population_size)] #generates actual population


def fitness(genome):
    return sum(genome) #just all the 1s in the genome

def one_fourth(nums, size):
    avg = sum(nums) // size
    new_nums = []
    for i in nums:
        if i >= avg:
            new_nums.append(i)
    return new_nums
    

#this is basically a random selection- SPECIMIN
def select_parent(population, fitness_values):
    avg_fitness = sum(fitness_values)  // len(population)
    #print(avg_fitness)
    #print(sum(min(population)))
    pick = avg_fitness#(sum(fitness_values) * 2) // (3 * len(population)) + sum(min(population)) #min fitness is 2/3 of the population 
    print(f"pick",pick)
    current = 0
    #for each individual in the population and their fitness value
    for indivdual, fitness_value in zip(population, fitness_values): #zip basically pairs the population array w its fitness value
        current = fitness_value
        if current > pick: #if the current fit value is better than our threshold, return the indivudal as a new parent
            print(f"LOOK", fitness_value)
            return indivdual
        
def crossover(parent1, parent2):
    if random.random() < crossover_rate: #if a crossover isn't gonna happen, just return the parents
       crossover_point = random.randint(1, len(parent1) - 1) #gives random point
       return parent1[:crossover_point] + parent2[crossover_point:], parent2[:crossover_point] + parent1[crossover_point:]
        #returns parentx up to this point and parenty from this point to the end
    else:
        return parent1, parent2
    

def mutate(genome):
    for i in range(len(genome)): 
        if random.random() < mutation_rate: #for each bit there's a 1% chance we'll flip it
            genome[i] = abs(genome[i] - 1)  #if genomoe is a 1 its a 0 now, else its still 0
    return genome
    

def genetic_algorithm():
    population = init_population(population_size, genome_length)
    #going through generations of gen algorithm
    for generation in range(generations):
        fitness_values = [fitness(genome) for genome in population] #fitness_values is an array of the fitness (number of 1s) of the total population
        print(fitness_values)
        
        new_population = []
        for _ in range(population_size // 2): #population size flor divided by 2- bc we're taking two parents so don't need to look at eveyrone
            parent1 = select_parent(population, fitness_values)
            parent2 = select_parent(population, fitness_values)
            offspring1, offspring2 = crossover(parent1, parent2)
            new_population.extend([mutate(offspring1), mutate(offspring2)]) #add offspring to new population

        population = new_population

        fitness_values = [fitness(genome) for genome in population] #each genome in pop we're calculating the fitness for goes in this list
        #best_fitness = max(fitness_values)
        #print(f"generation {generation}: Best fitness = {best_fitness} ")
    
    best_index = fitness_values.index(max(fitness_values))
    best_solution = population[best_index]
    #print(f'Best Solution: {best_solution}')
    print(f'Best Fitness: {fitness(best_solution)}')



genetic_algorithm()

'''class Algorithm():
    population_size = 36 #we have 36 solutions
    genome_length = 5#legnth of indivudual solutions = 20 (20 positions in array)
    mutation_rate = 0.1 #probablility of mutation happening
    crossover_rate = 0.8 #likehood of crossover happening instead of just returning the parents = 70%
    generations = 200 #process is repeated 200 times
    population = [[0.0, 0, 0.1, 0, 0],[0.4, 0, 0.1, 0, 0],[0.8, 0, 0.1, 0, 0],
                  [0.0, 0, 0.5, 0, 0],[0.4, 0, 0.5, 0, 0],[0.8, 0, 0.5, 0, 0],
                  [0.0, 0, 1, 0, 0],[0.4, 0, 1, 0, 0],[0.8, 0, 1, 0, 0],

                  [0.0, 0, 0.1, 1, 0],[0.4, 0, 0.1, 1, 0],[0.8, 0, 0.1, 1, 0],
                  [0.0, 0, 0.5, 1, 0],[0.4, 0, 0.5, 1, 0],[0.8, 0, 0.5, 1, 0],
                  [0.0, 0, 1, 1, 0],[0.4, 0, 1, 1, 0],[0.8, 0, 1, 1, 0],
                  
                  [0.0, 1, 0.1, 0, 0],[0.4, 1, 0.1, 0, 0],[0.8, 1, 0.1, 0, 0],
                  [0.0, 1, 0.5, 0, 0],[0.4, 1, 0.5, 0, 0],[0.8, 1, 0.5, 0, 0],
                  [0.0, 1, 1, 0, 0],[0.4, 1, 1, 0, 0],[0.8, 1, 1, 0, 0],
                  
                  [0.0, 1, 0.1, 1, 0],[0.4, 1, 0.1, 1, 0],[0.8, 1, 0.1, 1, 0],
                  [0.0, 1, 0.5, 1, 0],[0.4, 1, 0.5, 1, 0],[0.8, 1, 0.5, 1, 0],
                  [0.0, 1, 1, 1, 0],[0.4, 1, 1, 1, 0],[0.8, 1, 1, 1, 0]] #[contrast threshold, inc/dec, margin,inc/dec,con]
    
    def select_parent(population, conf_values):
        avg_fitness = sum(conf_values)  // population_size
        pick = avg_fitness
        current = 0
        #for each individual in the population and their fitness value
        for indivdual, conf_value in zip(population, conf_values): #zip basically pairs the population array w its fitness value
            current = conf_value
            if current > pick: #if the current fit value is better than our threshold, return the indivudal as a new parent
                print(f"LOOK", conf_value)
                return indivdual
    
    def crossover(parent1, parent2):
        if random.random() < crossover_rate: #if a crossover isn't gonna happen, just return the parents
            crossover_point = random.randint(1, len(parent1) - 1) #gives random point
            return parent1[:crossover_point] + parent2[crossover_point:], parent2[:crossover_point] + parent1[crossover_point:]
            #returns parentx up to this point and parenty from this point to the end
        else:
            return parent1, parent2
        
    def mutate(genome):
        for i in range(len(genome)): 
            mut = random.random()
            if mut < mutation_rate: #for each bit there's a 1% chance we'll flip it
                if mut % 2 == 0:
                    genome[i][1] = abs(genome[i] - 1) #only changing if the value will increase or decrease
                if random.random() % 2 == 0:
                    genome[i][3] = abs(genome[i] - 1)
        return genome
    
    def fitness(population):
        for i in population:
            result = reader.readtext("cropped.jpg", contrast_ths=i[0], adjust_contrast=.9, width_ths= 1.5, add_margin= i[2], decoder= 'beamsearch')

    
    def genetic_algorithm():
        #going through generations of gen algorithm
        for generation in range(generations):
            fitness_values = [fitness(genome) for genome in population] #fitness_values is an array of the fitness (number of 1s) of the total population
            print(fitness_values)
            
            new_population = []
            for _ in range(population_size // 2): #population size flor divided by 2- bc we're taking two parents so don't need to look at eveyrone
                parent1 = select_parent(population, fitness_values)
                parent2 = select_parent(population, fitness_values)
                offspring1, offspring2 = crossover(parent1, parent2)
                new_population.extend([mutate(offspring1), mutate(offspring2)]) #add offspring to new population

            population = new_population

            fitness_values = [fitness(genome) for genome in population] #each genome in pop we're calculating the fitness for goes in this list
            #best_fitness = max(fitness_values)
            #print(f"generation {generation}: Best fitness = {best_fitness} ")
        
        best_index = fitness_values.index(max(fitness_values))
        best_solution = population[best_index]
        #print(f'Best Solution: {best_solution}')
        print(f'Best Fitness: {fitness(best_solution)}')'''