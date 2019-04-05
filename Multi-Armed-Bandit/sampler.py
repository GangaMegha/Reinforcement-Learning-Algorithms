################# Sampling from distributions ###############

import numpy as np

# Uniform distribution sampler
def uniform(up, length):
	return np.random.uniform(high=up, size=length)

# Bernouilli distribution sampler
def bern(p, length):
	return np.random.binomial(1, p, size=length)

'''
If we pass n=1 to the sampler for Binomial distribution : np.random.binomial(n, p, size=None), 
it is equivalent to the Bernoulli distribution. Size will then determine the number of times to 
flip the coin, ie., the number of samples to be generated.
'''