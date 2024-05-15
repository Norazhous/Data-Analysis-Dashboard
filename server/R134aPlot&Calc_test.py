# pip install CoolProp
import numpy as np
import matplotlib.pyplot as plt
import CoolProp
from CoolProp.Plots import PropertyPlot
from CoolProp.Plots import SimpleCompressionCycle
import CoolProp.CoolProp as CP

pp = PropertyPlot('HEOS::R134a', 'PH', unit_system='EUR')
pp.calc_isolines(CoolProp.iQ, num=11)
cycle = SimpleCompressionCycle('HEOS::R134a', 'PH', unit_system='EUR')
Te = 265
Tc = 300
pe = 10
pc = 15
cycle.simple_solve_dt(Te, Tc, pe, pc, 0.7, SI=True) #http://www.coolprop.org/apidoc/CoolProp.Plots.SimpleCyclesCompression.html
cycle.steps = 50
sc = cycle.get_state_changes()

plt.close(cycle.figure)
pp.draw_process(sc)


Pcritp=CP.PropsSI("Pcrit","R134a")
Pmin_p=CP.PropsSI("P_MIN","R134a")
j= np.linspace(Pmin_p,Pcritp,1)
hf=CP.PropsSI('H', 'P', j, 'Q', 0, "R134a")
hv=CP.PropsSI('H', 'P', j, 'Q', 1, "R134a")
plt.plot(hf/1000,j/1000,'--r',linewidth=.5)
plt.plot(hv/1000,j/1000,'--r',linewidth=.5)

plot = PropertyPlot('R134a', 'ph')
plot.calc_isolines()
plot.show()

# # The following example can be used to create a pressure-enthalpy (logp,h) plot for R-134a with a couple of isotherms and isentropic lines:
# plot = PropertyPlot('HEOS::R134a', 'PH', unit_system='EUR', tp_limits='ACHP')
# plot.calc_isolines(CoolProp.iQ, num=11)
# plot.calc_isolines(CoolProp.iT, num=25)
# plot.calc_isolines(CoolProp.iSmass, num=15)
# plot.show()

