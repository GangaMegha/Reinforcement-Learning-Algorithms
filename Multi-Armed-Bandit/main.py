################# Main function #################

import argparse
from constants import *
from alg import *
from plot import *

# Calls the algorithms and the plotting functions
def main_fun(arg_val):
    config = vars(arg_val)

    if config["compare"]==False:
        if config["alg"] == "ETC":
            if config["dist_val"] == "P1":
                op, op_upper, op_lower, regret, regret_upper, regret_lower = etc_alg(P1, config["m"], len(P1), max(P1), np.argmax(P1), bern)

            elif config["dist_val"] == "P2":
                op, op_upper, op_lower, regret, regret_upper, regret_lower = etc_alg(P2, config["m"], len(P2), max(P2), np.argmax(P2), bern)
            
            elif config["dist_val"] == "P3":
                op, op_upper, op_lower, regret, regret_upper, regret_lower = etc_alg(P3, config["m"], len(P3), max(P3), np.argmax(P3), bern)
            
            elif config["dist_val"] == "P4":
                op, op_upper, op_lower, regret, regret_upper, regret_lower = etc_alg(P4, config["m"], len(P4), max(P4), np.argmax(P4), uniform)
            
            else :
                print("Unknown Distribution!!")
                return

        elif config["alg"] == "UCB":
            if config["dist_val"] == "P1":
                op, op_upper, op_lower, regret, regret_upper, regret_lower = ucb_alg(P1, len(P1), max(P1), np.argmax(P1), bern)
            
            elif config["dist_val"] == "P2":
                op, op_upper, op_lower, regret, regret_upper, regret_lower = ucb_alg(P2, len(P2), max(P2), np.argmax(P2), bern)
            
            elif config["dist_val"] == "P3":
                op, op_upper, op_lower, regret, regret_upper, regret_lower = ucb_alg(P3, len(P3), max(P3), np.argmax(P3), bern)
            
            elif config["dist_val"] == "P4":
                op, op_upper, op_lower, regret, regret_upper, regret_lower = ucb_alg(P4, len(P4), max(P4), np.argmax(P4), uniform)
            
            else :
                print("Unknown Distribution!!")
                return     

        else :
            print("Unknown algorithm specified!!!")
            return
        plot_optimal_percent(op, op_upper, op_lower, config["alg"], config["dist_val"], config["m"], config["err"])
        plot_regret(regret, regret_upper, regret_lower, config["alg"], config["dist_val"], config["m"], config["err"])

    else :
        etc_op = [0]*len(m_val[config["dist_val"]])
        etc_regret = [0]*len(m_val[config["dist_val"]])

        i = 0
        dist_ = eval(config["dist_val"])

        for m in m_val[config["dist_val"]] :
            if config["dist_val"]!="P4":
                etc_op[i], _, __, etc_regret[i], ___, ____ = etc_alg(dist_, m, len(dist_), max(dist_), np.argmax(dist_), bern)
            else :
                etc_op[i], _, __, etc_regret[i], ___, ____ = etc_alg(dist_, m, len(dist_), max(dist_), np.argmax(dist_), uniform)

            i = i + 1

        if config["dist_val"]!="P4" : 
            ucb_op, _, __, ucb_regret, ___, ____ = ucb_alg(dist_, len(dist_), max(dist_), np.argmax(dist_), bern)
        else :
            ucb_op, _, __, ucb_regret, ___, ____ = ucb_alg(dist_, len(dist_), max(dist_), np.argmax(dist_), uniform)
        

        plot_optimal_percent_combined(ucb_op, etc_op, config["dist_val"])
        plot_regret_combined(ucb_regret, etc_regret, config["dist_val"])



# Function to parse hyperparameters from the commandline
def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument('--distribution', 
                        action="store", 
                        dest="dist_val", 
                        default="P1", 
                        type = str,
                        help='Choose from P1, P2, P3, P4')

    parser.add_argument('--algorithm', 
                        action="store", 
                        dest="alg", 
                        default="ETC", 
                        type = str,
                        help='Choose from ETC, UCB')

    parser.add_argument('--m', 
                        action="store", 
                        dest="m", 
                        default=300, 
                        type = int,
                        help='Int value : no. of times to explore each arm for ETC')

    parser.add_argument('--err', 
                        action="store", 
                        dest="err", 
                        default=1, 
                        type = int,
                        help='Int value : interval for error bar')

    parser.add_argument('--compare', 
                        action="store", 
                        dest="compare", 
                        default=False, 
                        type = bool,
                        help='Whether to compare different algorithms')


    arg_val = parser.parse_args()
  
    # Read the data and run the algorithm
    main_fun(arg_val)

parse()