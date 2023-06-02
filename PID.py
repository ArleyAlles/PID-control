from Curve_fit import CurveFit
from data import Data
import numpy as np
import control as clt
import matplotlib.pyplot as plt


class PID:

    def __init__(self, time, output, Kd, Kp, Ki):
        self.time = time
        self.output = output
        self.Kd = Kd
        self.Kp = Kp
        self.Ki = Ki

    def P_s(self):
        """
        Transfer function of plant
        :return: Ps: Transfer function of plant in s domain
        """
        param = CurveFit.fit_curve(self.output, self.time)
        numerator = [param[0]]
        denominator = [param[1], 1]
        Ps = clt.tf(numerator, denominator)
        print("================ TRANSFER FUNCTION OF PLANT ===================\n",Ps)
        return Ps

    def C_s(self):
        """
        Transfer function of controller
        :return: Cs: Transfer function of controller in s domain
        """
        numerator = [self.Kd, self.Kp, self.Ki]
        denominator = [1., 0.]
        Cs = clt.tf(numerator, denominator)
        print("================ TRANSFER FUNCTION OF CONTROLLER ===================\n", Cs)
        return Cs

    def F_s(self):
        """
        Transfer function of feedback
        :return: Hs: Transfer function of feedback in s domain
        """
        Fs = clt.tf([1.], [1.])
        print("================ TRANSFER FUNCTION OF FEEDBACK ===================\n", Fs)
        return Fs

    def G_s(self):
        """
        Transfer function of closed loop system
        :return: Gs: Transfer function of closed loop system in s domain
        """
        Gs = clt.feedback(clt.series(self.C_s(), self.P_s()), self.F_s(), sign=-1)
        print("================ TRANSFER FUNCTION OF CLOSED LOOP SYSTEM ===================\n",Gs)
        return Gs

    def simulation(self):
        """
        Plot generation
        """
        simulation_time = 20
        time_mf, p_mf = clt.step_response(self.G_s(), simulation_time)
        param = CurveFit.fit_curve(self.output, self.time)
        fig, (ax, ax1) = plt.subplots(1, 2)


        ax.plot(self.time, self.output, 'r', label='Experimental data')
        ax.plot(self.time, CurveFit.func(self.time, *param), label='Fitted curve')
        ax.set_title("Curve fitting of experimental data", fontsize=16)
        ax.set_xlabel("Time", fontsize=16)
        ax.set_ylabel("Output", fontsize=16)
        ax.legend(loc='best')


        ax1.plot(time_mf, p_mf, 'b', label ='PID control')
        ax1.plot(time_mf, np.ones(len(time_mf)), 'r--', label='Setpoint')
        ax1.set_xlabel("Time", fontsize=16)
        ax1.set_title("PID control", fontsize=16)
        ax1.set_ylabel("Output", fontsize=16)
        ax1.legend(loc='best')
        plt.show()

if __name__=='__main__':
    """
    PID parameters
    """
    Ki = 3.0 #Valor alterável
    Kp = 5.5 #Valor alterável
    Kd = 0.  #Valor alterável

    time = Data.time()
    output = Data.output(hasnoise=True)
    resp = PID(time, output, Kd, Kp, Ki).simulation()

