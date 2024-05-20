import probability 

# Question 2 Bayesian
likelihood = {
    'insemester': {'spot': 0.6, 'nospot': 0.4},
    'betweensemesters': {'spot': 0.9, 'nospot': 0.1}
    }

prior = {
    'insemester':0.5,
    'betweensemesters':0.5
    }

for i in range(4):
    prior = probability.posterior(prior, likelihood, {'spot'})

print(' Probability of being in semester is', prior['insemester'])

# Question 3 Decision Theory
highyeild = {
    'drought': 2,
    'nodrought': 10
    }

draughttolarance = {
    'drought': 6,
    'nodrought': 8
    }

utilities = {
    'high-yield': highyeild,
    'drought-tolerance': draughttolarance
    }

droughtprob = {
    'drought': 0.3,
    'nodrought': 0.7
    }

print('utility for high-yeild variety:', probability.utility(droughtprob, highyeild))
print('utility for drought-tolerance variety:', probability.utility(droughtprob, draughttolarance))

print('Best decision:', probability.decide(droughtprob, utilities))