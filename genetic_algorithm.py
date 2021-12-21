from numpy.random import randint
from numpy.random import rand, choice
from object import *
# from data_transform import *

np.random.seed(10)

'''
objective function is to minimise KL divergence 
of the probablity distribution of the set S
'''

def objective(S):
    return KL_Divergence(S)

'''
tournament selection returns a random selection
based on highest score of the different possible sets
'''


def selection(pop, scores, k=3):
    # first random selection
    selection_ix = randint(len(pop))
    for ix in randint(0, len(pop), k-1):
        # check if better (e.g. perform a tournament)
        if scores[ix] < scores[selection_ix]:
            selection_ix = ix
    return pop[selection_ix]

'''
crossover two parents to create two children
return children sets after crossover
'''


def crossover(p1, p2, r_cross):
    # children are copies of parents by default
    c1, c2 = p1.copy(), p2.copy()
    
    # check for recombination
    if rand() < r_cross:
        
        # select crossover point that is not on the end of the string
        pt = randint(1, len(p1)-2)
        # perform crossover
        c1 = p1[:pt] + p2[pt:]
        c2 = p2[:pt] + p1[pt:]
    return [c1, c2]

'''
mutation of a single parent
randomly removes some points in a population
and randomly add new points and return new population
'''


def mutation(indiv, r_mut, S):
    for i in range(len(indiv)):
        # check for a mutation
        if rand() < r_mut:
            indiv.remove(indiv[i])
            indiv.append(choice(S))

'''
genetic_algorithm returns best representative
population along with their scores
'''

def genetic_algorithm(objective, n_obj, n_iter, n_pop, r_cross, r_mut, S):
    # initial population of random bitstring
    pop = [choice(S, n_obj).tolist() for _ in range(n_pop)]
    
    # keep track of best solution
    best, best_eval = 0, objective(pop[0])
    check_convg=np.zeros((200,1))

    # enumerate generations
    for gen in range(n_iter):
        
        # evaluate all candidates in the population
        scores = [objective(c) for c in pop]
        # check for new best solution
        
        for i in range(n_pop):
            if scores[i] < best_eval:
                best, best_eval = pop[i], scores[i]
        
        check_convg[gen%200] = best_eval

        print(">%d, new best score = %.3f" % (gen, best_eval))
        res = all(ele == check_convg[0] for ele in check_convg)
        if res:
            print("Converged!")
            break

        # select parents
        selected = [selection(pop, scores) for _ in range(n_pop)]
        # create the next generation
        children = list()

        for i in range(0, n_pop, 2):
            # get selected parents in pairs
            p1, p2 = selected[i], selected[i+1]
            # crossover and mutation
            for c in crossover(p1, p2, r_cross):
                # mutation
                mutation(c, r_mut, S)
                # store for next generation
                children.append(c)
        
        # replace population
        pop = children
    
    return [best, best_eval]