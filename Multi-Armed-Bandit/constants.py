############## Defining the constants ############

# Horizon
n = 10000

# No. of times to repeat the algorithms
repeat = 100

# p-values for 10 arms with individual bernoulli distributions
P1 = [0.6, 0.4, 0.4, 0.4, 0.4, 0.3, 0.3, 0.3, 0.3, 0.3]

# p-values for 10 arms with individual bernoulli distributions
P2 = [0.62, 0.6, 0.6, 0.6, 0.6, 0.58, 0.58, 0.58, 0.5, 0.5]

# p-values for 5 arms with individual bernoulli distributions
P3 = [0.8, 0.4, 0.3, 0.2, 0.1]

# upper-limit values for 3 arms with individual uniform distributions
P4 = [20, 16, 12]

# Dictionary for different values of m for comparison
m_val = dict({
			"P1" : [1, 10, 150, 334, 500, 750, 1000],
			"P2" : [1, 10, 100, 250, 500, 750, 1000],
			"P3" : [1, 10, 109, 300, 500, 1000],
			"P4" : [1, 8, 50, 250, 500, 1000]
		})