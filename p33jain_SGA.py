import random
import math
import copy
from matplotlib import pyplot as plt


def parent_selection(parent_population,population_size):
    intial_parents_pool = copy.deepcopy(parent_population)
    
    i = 0
    fittest_parents = []
    fitness = 200000000
    K_for_tournament = 10
    # math.ceil(0.15*population_size)

    while(i < population_size):
        
        fitness = 200000000
        Tournament =random.sample(intial_parents_pool, K_for_tournament)
        # fittest_parent_among_sample = []

        for solution in Tournament:
            if solution[2] < fitness:
                fittest_parent_among_sample = solution
                fitness = solution[2]
        i = i +1
        fittest_parents.append(fittest_parent_among_sample)
    # print(fittest_parents)
    
    return fittest_parents



def generate_offsprings_mating(parents_pool,population_size):
    fittest_parents = copy.deepcopy(parents_pool)
    offsprings_mating = []

    for i in range(population_size):


        if i == (population_size-1):
            parent1 = fittest_parents[i]
            parent2 = fittest_parents[0]
        else:
            parent1 = fittest_parents[i]
            parent2 = fittest_parents[i+1]
        
        # print(parent2)
        temp = parent1[1]
        parent1[1] = parent2[1]
        parent2[1] = temp
        
        
        x = ((int(parent1[0],2)-1)/1000) - 5
        y = ((int(parent1[1],2)-1)/1000) - 5
        parent1[2] = ((4 - (2.1*pow(x,2)) + (pow(x,4)/3))*pow(x,2)) + (x*y) + ((-4 + (4*pow(y,2)))*pow(y,2))
        offsprings_mating.append(parent1)
        # # print(parent1)

        x1 = ((int(parent2[0],2)-1)/1000) - 5
        y1 = ((int(parent2[1],2)-1)/1000) - 5
        parent2[2] = ((4 - (2.1*pow(x1,2)) + (pow(x1,4)/3))*pow(x1,2)) + (x1*y1) + ((-4 + (4*pow(y1,2)))*pow(y1,2))
        offsprings_mating.append(parent2)


    offsprings_mating.sort(key=lambda x: x[2])
    offsprings_mating_updated = offsprings_mating[0:population_size]
    return offsprings_mating_updated

def generate_offsprings_mutating(offsprings_mate, population_size):
    offsprings_after_mating = copy.deepcopy(offsprings_mate)
    pm = 0.03
    offsprings_after_mutating = []
    length_offsprings = len(offsprings_after_mating)


    for i in range(length_offsprings):
        offspring = offsprings_after_mating[i]
        binary_xy = offspring[0]+offspring[1]
        length = len(binary_xy)

        for each_bit_index in range(28):
            check = random.uniform(0,1)
            list_of_bits = list(binary_xy)

            if check < pm:
                if list_of_bits[each_bit_index] =="0":
                    list_of_bits[each_bit_index] = "1"
                    # binary_xy = binary_xy[:each_bit_index+1] + "1" + binary_xy[each_bit_index+2:]
                else:
                    list_of_bits[each_bit_index] = "0"
                    # binary_xy = binary_xy[:each_bit_index+1] + "0" + binary_xy[each_bit_index+2:]
        

        offspring[0] = "".join(list_of_bits[:14])
        offspring[1] = "".join(list_of_bits[14:])


        x = ((int(offspring[0],2)-1)/1000)-5
        y = ((int(offspring[1],2)-1)/1000)-5
        offspring[2] = ((4 - (2.1*pow(x,2)) + (pow(x,4)/3))*pow(x,2)) + (x*y) + ((-4 + (4*pow(y,2)))*pow(y,2))
        offsprings_after_mutating.append(offspring)
    offsprings_after_mutating_final = offsprings_after_mutating
    
    return  offsprings_after_mutating_final
    

def main(population_size):
    lower_bound = -5
    upper_bound = 5
    intial_population = []

    for i in range(population_size):
        x = round(random.uniform(lower_bound,upper_bound),3)
        y = round(random.uniform(lower_bound,upper_bound),3)

        fitness = ((4 - (2.1*pow(x,2)) + (pow(x,4)/3))*pow(x,2)) + (x*y) + ((-4 + (4*pow(y,2)))*pow(y,2))

        x_binary = bin(int(((x-lower_bound)*1000 + 1))).replace("0b", "").zfill(14)
        y_binary = bin(int(((y-lower_bound)*1000 + 1))).replace("0b", "").zfill(14)
        

        intial_population.append([x_binary,y_binary,fitness])


    # best_solution = []
    list_average_fitness = []
    list_best_fitness = []
    best_fitness = 2000000
    i = 0
    generation_number = []
    while(i<50):
        average = 0
        if i == 0:
            fittest_parents = parent_selection(intial_population,population_size)
        else:
            fittest_parents = parent_selection(offsprings_mutating ,population_size)

        offsprings_mating = generate_offsprings_mating(fittest_parents,population_size)
        
       
        offsprings_mutating = generate_offsprings_mutating(offsprings_mating,population_size)
        # print(offsprings_mutating[0])
        # print(fittest_parents)
        # print("")
        # print(offsprings_mating)
        # print("")
        # print(offsprings_mutating)
        for m in range(population_size):
            average = average + offsprings_mutating[m][2]
        list_average_fitness.append(average)
        list_best_fitness.append(offsprings_mutating[0][2])
        generation_number.append(i+1)



        solution = offsprings_mutating[0]
        if (solution[2] < best_fitness):
            best_solution = solution
            best_fitness = solution[2]
            print(best_fitness)
            print(best_solution)


        i = i +1
        print(i)
    print(best_solution)
    x = ((int(best_solution[0],2)-1)/1000) - 5
    y = ((int(best_solution[1],2)-1)/1000) - 5
    print(x,y)

    
    fig, [ax1,ax2] = plt.subplots(2)
    ax1.plot( generation_number,list_average_fitness)
    ax1.set_title("average_fitness")
    ax2.plot(generation_number,list_best_fitness)
    ax2.set_title("best_fitness")

    plt.show()




if __name__ == "__main__":
    main(1000)