import numpy as np
from scipy.optimize import bisect

def find_critical_load(L, E, A, r, c, e, sigma_allow):
    
    def f(P):
        theta = (L / (2 * r)) * np.sqrt(P / (E * A))
        sigma_max = (P / A) * (1 + (e * c / r**2) * (1 / np.cos(theta)))
        return sigma_max - sigma_allow
        
    P_euler = (np.pi**2 * E * A) / ((L / r)**2)
    P_crit = bisect(f, 0, 0.999 * P_euler)
    
    return float(P_crit)
