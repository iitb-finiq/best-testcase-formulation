import numpy as np
import math

'''
Object class contains the features that define prob.
distribution of a particular dataset
'''


class Object:

    def __init__(self, input):
        [solve_for, placement, strike_shift, issue_date, ac_type, ac_freq,
            ac_from, ac_coupon_type, payoff_type] = input.split(',')

        self.solve_for = solve_for
        self.placement = placement
        self.strike_shift = strike_shift
        self.issue_date = issue_date
        self.ac_type = ac_type
        self.ac_freq = ac_freq
        self.ac_from = ac_from
        self.ac_coupon_type = ac_coupon_type
        self.payoff_type = payoff_type
        self.str = input

    # defines the true distribution of the dataset
    # needs to be hardcoded for diff. dataset
    def q(self):
        prob = 1
        if self.strike_shift == "Fwd":
            prob *= 0.2
        else:
            prob *= 0.8

        if self.issue_date == "T+5" or self.issue_date == "T+10":
            prob *= 0.25
        else:
            prob *= 0.5

        if self.ac_freq == "Daily" or self.ac_freq == "Monthly":
            prob *= 0.5
        else:
            prob *= 0

        if self.ac_from[-1] == '1':
            prob *= 0.8
        else:
            prob *= 0.2

        if self.ac_coupon_type == "Flat":
            prob *= 0.8
        else:
            prob *= 0.2

        if self.payoff_type == "European":
            prob *= 0.8
        else:
            prob *= (0.2/3)
        return prob+1e-12


'''
S: list of Objects
empirical probability distribution of S
returns a dict prob
'''


def p(S):
    prob = {}
    for s in S:
        if s.str not in prob.keys():
            prob[s.str] = 1
        else:
            prob[s.str] += 1

    for s in prob.keys():
        prob[s] /= len(S)

    return prob


# calculates KL Divergence of a set of objects S
def KL_Divergence(S):
    prob = p(S)
    div = 0

    for s in prob.keys():
        div += prob[s] * np.log(prob[s] / Object(s).q())

    return div