from genetic_algorithm import *
import matplotlib.pyplot as plt

# define the total iterations
n_iter = 1000
# bits
n_obj = 20
# define the population size
n_pop = 100
# crossover rate
r_cross = 0.9
# mutation rate
r_mut = 0.5 / float(n_obj)
# perform the genetic algorithm search

best_scores = []
best_populations = []
for obj in range(5, 50, 5):
    print("Objects in a Population: ", obj)
    best, score = genetic_algorithm(objective, obj, n_iter, n_pop, r_cross, r_mut)
    best_scores.append(score)
    best_populations.append(best)

print('Done!')
print("score: ", score)

x = list(range(5, 50, 5))

plt.plot(x, best_scores)
plt.title("Variation of KL-Divergence with Basket Size")
plt.xlabel("Basket Size")
plt.ylabel("KL-Divergence Score")
plt.show()