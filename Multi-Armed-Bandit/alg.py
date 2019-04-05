import numpy as np
from constants import * 
from sampler import *

def etc_alg(arr, m, k, max_val, max_idx_true, dist):
	mu = []
	X = []
	Optimal_percent = []

	for i in range(repeat):
		mu_cap = []
		x = []
		op = []

		for j in range(k):
			samples = dist(arr[j], m)
			x = x + list(samples)
			mu_cap.append(1/m * sum(samples))
			op = op + [j for p in range(m)]

		max_idx = np.argmax(mu_cap)

		for j in range(m*k, n):
			samples = dist(arr[max_idx], 1)
			x.append(samples)
			op.append(max_idx)
		
		X.append(x)
		Optimal_percent.append(op)

	Optimal_percent = np.array(Optimal_percent)
	X = np.array(X)

	regret = []
	op = []

	for i in range(repeat):
		regret_j = []
		op_j = []
		for j in range(n):
			regret_j.append((j+1)*max_val - np.sum(X[i, :j+1]))
			op_j.append(len(np.where(Optimal_percent[i, :j+1]==max_idx_true)[0])*100.0/(j+1))
		regret.append(regret_j)
		op.append(op_j)

	regret_upper = np.max(regret, axis=0)
	regret_lower = np.min(regret, axis=0)
	regret = np.mean(regret, axis=0)

	op_upper = np.max(op, axis=0)
	op_lower = np.min(op, axis=0)
	op = np.mean(op, axis=0)

	return(op, op_upper, op_lower, regret, regret_upper, regret_lower)

def ucb_alg(arr, k, max_val, max_idx_true, dist):
	mu = []
	X = []
	Optimal_percent = []

	for i in range(repeat):
		mu_cap = []
		x = []
		op = []
		num = np.zeros((k,1))
		add_on = np.zeros((k,1))
		T = 0

		for j in range(k):
			samples = dist(arr[j], 1)
			x.append(samples)
			T = T + 1
			mu_cap.append(samples)
			op.append(j)
			num[j] = num[j] + 1
			
		add_on = np.sqrt(8*np.log(T)/num)

		for j in range(k, n):
			max_idx = np.argmax(np.add(mu_cap, add_on))
			samples = dist(arr[max_idx], 1)

			x.append(samples)
			T = T + 1
			mu_cap[max_idx] = (mu_cap[max_idx]*num[max_idx] + samples)/(num[max_idx] + 1)
			op.append(max_idx)
			num[max_idx] = num[max_idx] + 1

			add_on = np.sqrt(8*np.log(T)/num)

		X.append(x)
		Optimal_percent.append(op)

	Optimal_percent = np.array(Optimal_percent)
	X = np.array(X)

	regret = []
	op = []

	for i in range(repeat):
		regret_j = []
		op_j = []
		for j in range(n):
			regret_j.append((j+1)*max_val - np.sum(X[i, :j+1]))
			op_j.append(len(np.where(Optimal_percent[i, :j+1]==max_idx_true)[0])*100.0/(j+1))
		regret.append(regret_j)
		op.append(op_j)

	regret_upper = np.max(regret, axis=0)
	regret_lower = np.min(regret, axis=0)
	regret = np.mean(regret, axis=0)

	op_std = np.std(op, axis=0)
	op = np.mean(op, axis=0)
	op_upper = op + op_std
	op_lower = op - op_std

	return(op, op_upper, op_lower, regret, regret_upper, regret_lower)
