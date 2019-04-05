############ Plotting functions #############

import matplotlib.pyplot as plt
import numpy as np
from constants import *

def plot_optimal_percent(arr, upper, lower, algo, distr, m, err):

	plt.clf()
	upper = np.array(upper)
	lower = np.array(lower)

	upper = np.reshape(upper, (1,upper.shape[0]))
	lower = np.reshape(lower, (1,lower.shape[0]))

	val = np.vstack((np.array(arr) - lower, upper - np.array(arr)))

	plt.errorbar(range(len(arr)), arr, xerr=None, yerr=val, ecolor='y', errorevery=err)
	plt.title("{} {} : (%) of optimal arm pulled".format(algo, distr))
	plt.xlabel("t")
	plt.ylabel("Percentage (%)")
	plt.grid()

	if algo=="ETC":
		plt.savefig("Report/Figures/{}_{}_{}_op.png".format(algo, distr, m))
	else:
		plt.savefig("Report/Figures/{}_{}_op.png".format(algo, distr))
	# plt.show()

def plot_regret(arr, upper, lower, algo, distr, m, err):

	plt.clf()
	upper = np.reshape(upper, (1, len(arr)))
	lower = np.reshape(lower, (1, len(arr)))
	val = np.vstack((np.array(arr)-lower, upper-np.array(arr)))

	plt.errorbar(range(len(arr)), arr, xerr=None, yerr=val, ecolor='y', errorevery=err)
	plt.title("{} {} : Cumulative Regret".format(algo, distr))
	plt.xlabel("t")
	plt.ylabel("Cumulative Regret")
	plt.grid()

	if algo=="ETC":
		plt.savefig("Report/Figures/{}_{}_{}_ret.png".format(algo, distr, m))
	else:
		plt.savefig("Report/Figures/{}_{}_ret.png".format(algo, distr))
	# plt.show()

def plot_optimal_percent_combined(ucb_op, etc_op, distr) :
	plt.clf()

	for i in range(len(m_val[distr])) :
		plt.plot(range(len(etc_op[i])), etc_op[i], label='ETC: m={}'.format(m_val[distr][i]))

	plt.plot(range(len(ucb_op)), ucb_op, label='UCB'.format(m_val[distr][i]))
	plt.title("Comparison of (%) of optimal arm pulled")
	plt.xlabel("t")
	plt.ylabel("Percentage (%)")
	plt.legend()
	plt.grid()
	plt.savefig("Report/Figures/Combined_op_{}.png".format(distr))
	# plt.show()


def plot_regret_combined(ucb_regret, etc_regret, distr) :
	plt.clf()

	for i in range(len(m_val[distr])) :
		plt.plot(range(len(etc_regret[i])), etc_regret[i], label='ETC: m={}'.format(m_val[distr][i]))

	plt.plot(range(len(ucb_regret)), ucb_regret, label='UCB'.format(m_val[distr][i]))
	plt.title("Comparison of Cumulative Regret")
	plt.xlabel("t")
	plt.ylabel("Cumulative Regret")
	plt.legend()
	plt.grid()
	plt.savefig("Report/Figures/Combined_regret_{}.png".format(distr))
	# plt.show()