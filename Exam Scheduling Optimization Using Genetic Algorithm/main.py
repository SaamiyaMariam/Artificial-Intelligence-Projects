
from typing import List, Tuple
import random
import numpy as np
import time


random.seed(int(time.time()))
max_hours = 6
pop_size = 100 #arbitrarily chosen
num_courses = 5
num_time_slots = 3
num_halls = 2
num_conflicts = 0
overtime_penalty = 10
confliction_penalty = 100
fitness_values = []
schedule_population = [] #consists of multiple schedules
num_gens = 100


# Initializing Population
course_id = list( range( 1, num_courses + 1 ) )
time_slot = list( range( 1, num_time_slots + 1 ) )
exam_hall = list( range( 1, num_halls + 1 ) )

exam_conflicts = {
    ('C1', 'C2'): 10,
    ('C1', 'C4'): 5,
    ('C2', 'C5'): 7,
    ('C3', 'C4'): 12,
    ('C4', 'C5'): 8,
    }


def make_schedule(course_id, time_slot, exam_hall):
    sched = []
    for course in course_id:
        exam = []
        exam = ( course, random.choice(time_slot), random.choice(exam_hall))
        sched.append(exam)

    return sched


def population_initializer():
    
    for i in range(pop_size):
        #generating schedules and appending them in schedule_population
        sched=[]
        sched = make_schedule(course_id, time_slot, exam_hall)
        schedule_population.append(sched)
        fit_val = fitness_function(exam_conflicts,sched)
       # print("fit_val: ", fit_val)
        fitness_values.append(fit_val)

def check_conflict(sched, exam_conflicts):
    # Calculate the total number of conflicts between exams
    num_conflicts = 0
    for i in range(len(sched)):
        for j in range(i + 1, len(sched)):
            exam1 = sched[i]
            exam2 = sched[j]
            if exam1[1] == exam2[1] or ((exam1[0], exam2[0]) in exam_conflicts or (exam2[0], exam1[0]) in exam_conflicts):
                key = ('C'+str(exam1[0]), 'C'+ str(exam2[0]))
                if key in exam_conflicts:
                    conflict_value = exam_conflicts[key]
                    num_conflicts += conflict_value
    return num_conflicts

def hall_time_validity(schedule, exam_hall):
    for hall in exam_hall: # for each exam hall, we check if there is an exam scheduled
        hours = 0
        for s in schedule:
            if s[2] == hall :
                hours+= random.randint(1,3)
        # checking if hours exceeds limit
        if hours > max_hours:
            return hours    
    #else return valid status
    return 0         

def fitness_function(exam_conflicts, sched):
    # fitness value will be dependent upon the number of exam conflicts in a schedule
    # as well as the number of hours an exam hall is occupied for a day
    overtime = 0
    fitness_val = 0
    conflict_count=0
    # checking if number of hours each exam hall is occupied is valid
    validity = hall_time_validity(sched,exam_hall)
    if validity != 0 :
        overtime = validity
    
    conflict_count = check_conflict(sched, exam_conflicts)
    # we want to minimize conflicts so a suitable fitness formula would be
    fitness_val -= (  (confliction_penalty * conflict_count ) + (overtime_penalty * (overtime - max_hours)) )
    #print("fitness value:", fitness_val)
    return fitness_val

def single_point_co(parentA, parentB):
    childA = []
    childB = []
    crossover_pt = random.randint(1, len(parentA) - 1) #random pt
    childA = parentA[crossover_pt:] + parentB[:crossover_pt]
    childB = parentB[crossover_pt:] + parentA[:crossover_pt]

    return childA, childB


def mutate_child(child):
    mu = random.randint(0,1) # if one, mutation will take place, otherwise unmutated child will be returned
    if(mu ==0):
        return child
    
    #a random exam is picked from the offspring/schedule and is mutated
    og_exam_index = random.randint(0, len(child) - 1)
    og_exam = child[og_exam_index]
    mutated_child = (og_exam[0], random.randint(1, num_time_slots), random.randint(1, num_halls)) # same course, random time and hall
    child[og_exam_index] = mutated_child
    return child

def genetic_algo():
    print("Running Genetic Algorithm...")

    for gen in range(num_gens):  
        # selecting 10 parents for crossover via tournament selection
        parents = []
    
        tourn_size = 5 #arbitrary value
        for i in range(10):
            tournament = random.sample(range(len(schedule_population)), tourn_size)
            tournament_fitness = [fitness_values[j] for j in tournament]
            best_fitness_index = tournament[np.argmax(tournament_fitness)] # index of max fitness value
            parents.append(schedule_population[best_fitness_index])

        # Creating 10 offspring for the next gen
        offspring = []
        for i in range(10):
            p1, p2 = random.sample(parents, 2)
            #applying single-point cross-over with a probability of 0.8
            prob = random.random()
            if(prob < 0.8 ):
                c1,c2 = single_point_co(p1,p2)
            else:
                c1,c2 = p1,p2
            #applying mutation with a probability of 0.1
            prob = random.random()
            if(prob < 0.1):
                c1 = mutate_child(c1)
            
            prob = random.random()
            if(prob < 0.1):
                c2 = mutate_child(c2)
            
            # appending children to offspring list
            offspring.append(c1)
            offspring.append(c2)

        # evaluating the fitness of the resulting offspring
        fit_val_offsp = []
        for schedule in offspring:
            fit_val_offsp.append(fitness_function(exam_conflicts, schedule))

        # out of the 10 offspring we have created, we will compare their fitness values with the lowest fit vals in our population

        for ch in range(10):
            lowest_fit_val = min(fitness_values)
            lowest_individual = fitness_values.index(lowest_fit_val)
            # if they perform better, we will replace them with offspring
            if (fit_val_offsp[i] > lowest_fit_val):
                schedule_population[lowest_individual] = offspring[i]
                fitness_values[lowest_individual] = fit_val_offsp[i]

    

if __name__ == "__main__":
     
    start_time = time.time()

    print("--------------------------------------------------------------------------")
    print("\nInitializing Population...")

    population_initializer()



    genetic_algo()
    print("..........................................................................")
    # Finding best solution after 100 Generations
    best_fitness = max(fitness_values)
    best_schedule = schedule_population[fitness_values.index(best_fitness)]
    print("After ", num_gens," Generations: \n->Best Fitness Value: {}".format(best_fitness))
    print("->Best Solution:", best_schedule,"\n")
    print("--------------------------------------------------------------------------")

    # run your function here
    final_time = time.time()
    total_time = 1000 * (final_time - start_time)
    print("Total running time:", total_time, " milliseconds")
