# PID-control
This code treats about control simulation of first-order transfer function **without dead time** for experimental dataset.
Such code is divided into three parts:
* 1-) **data.py**  -----------> Where dataset is remains. In this code, was implemented an addition of noise to the data (opitional)
* 2-) **Curve_fit.py** -------> Here the parameters of first-order transfer function is obtained, usind curve_fit method from scipy
* 3-) **PID.py** -------------> Code responsible for generating transfer function of closed loop system (by control library) and plot output of PID control system for a given pertubation of system. 

OBS: 
* For observation of PID control system, the user needs to set, manually, values for **Ki**, **Kp** and **Kd** 
* If user wants to add noise in the dataset, the option **hasnoise** should be equals to **True**. The default is **False**
