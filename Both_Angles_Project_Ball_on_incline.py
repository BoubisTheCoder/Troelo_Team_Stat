import numpy as np                                     # Matlab like syntax for linear algebra and functions
import matplotlib.pyplot as plt                        # Plots and figures like you know them from Matlab
import seaborn as sns                                  # Make the plots nicer to look at
from iminuit import Minuit                             # The actual fitting tool, better than scipy's
import sys                                             # Module to see files and folders in directories
from scipy import stats

#Putting the angles in the arrays, in degrees
theta_norm = np.array([0.2688, 0.2758, 0.2775, 0.2749])
error_theta_norm = np.array([0.0021, 0.0037, 0.0038, 0.0031])
theta_rev = np.array([0.2601, 0.2602, 0.2583, 0.2548])
error_theta_rev = np.array([0.0017, 0.0017, 0.0031, 0.0037])
mean_theta = (theta_norm + theta_rev)/2
#Calculation of the Mean of angles from normal and reversed
print(mean_theta)
#Error on the Mean 
Err_mean_theta = np.sqrt(np.square(error_theta_norm) + np.square(error_theta_rev))
print(Err_mean_theta)
# Now we will take the averaged measurements and calculate the weighted mean, error of weighted mean and chi2
#dhook = theta_gonio, i just copied the script, used for Dball and Drail
dhook = mean_theta
err_dhook = Err_mean_theta

ErrSquared= np.square(err_dhook)
print(ErrSquared)
ErrTotal= np.sum(1/ErrSquared)
print(ErrTotal)
Weights= dhook/ErrSquared
print(Weights)
Weighted_Mean=np.sum(Weights)/ErrTotal
print(Weighted_Mean)

#Now lets evaluate the error

sigma_Weighted_Mean= np.sqrt(1/ErrTotal)
print(sigma_Weighted_Mean)

print("The weighted angle is ",  Weighted_Mean, "plus/minus", sigma_Weighted_Mean, "rad" )

#Now we will continue with the Chi2 value 
Chi2_value= np.sum(np.square((dhook-Weighted_Mean)/err_dhook))

print("the Chi2_Value is", Chi2_value)

#Lastly we will calculate the probability of Chi2Value


Ndof_fit=3
 
Prob_fit = stats.chi2.sf(Chi2_value, Ndof_fit)
print("this is the p-value of Chi2", Prob_fit)
#Lets proceed to the trigonometry method

theta_trig = np.arctan(0.27033)
print(" This is the angle from the trigonometric method", theta_trig) 
# Now the error from the error propagation formula 
S = 1/(1 + np.power(0.27033, 4))
print(S)
Err_theta_trig = np.sqrt(S*np.square(0.12)/(np.square(98.4)) + S* np.square(0.27033 * 0.1))
print(" The error, from error propagation, on the trigonometry is: ", Err_theta_trig)
print("The result from the trigonometry process is : ", theta_trig, "+-", Err_theta_trig, "rad" )
print("The result from the goniometer is : ", Weighted_Mean , "+-", sigma_Weighted_Mean, "rad")



