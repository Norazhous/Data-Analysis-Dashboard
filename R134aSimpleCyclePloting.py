import CoolProp
from CoolProp.Plots import PropertyPlot
from CoolProp.Plots import SimpleCompressionCycle
import matplotlib.pyplot as plt


CP = CoolProp.CoolProp


pp = PropertyPlot('HEOS::R134a', 'PH', unit_system='EUR')
pp.calc_isolines()
cycle = SimpleCompressionCycle('HEOS::R134a', 'PH', unit_system='EUR')

# # This part Quality(0(liquid)-1(vapor)) and temperature are need for calculation. 
# T0 = 280
# pp.state.update(CoolProp.QT_INPUTS,0.1,T0-10) # Q means quality Quality (Q) is a dimensionless quantity that represents the ratio of the mass of vapor to the total mass (vapor + liquid) in a two-phase mixture. Its value ranges from 0 (saturated liquid) to 1 (saturated vapor).Temperature (T) is the thermodynamic temperature of the fluid. 
# p0 = pp.state.keyed_output(CoolProp.iP)
# T2 = 310
# pp.state.update(CoolProp.QT_INPUTS,1.0,T2+15)
# p2 = pp.state.keyed_output(CoolProp.iP)
# pp.calc_isolines(CoolProp.iT, [T0-273.15,T2-273.15], num=2)
# cycle.simple_solve(T0, p0, T2, p2, 0.7, SI=True)
# cycle.steps = 50
# sc = cycle.get_state_changes()
# pp.draw_process(sc)
# plt.close(cycle.figure)
# pp.show()

# T and P values. e- evaporator , c- condenser
T1 = 11+273.15   # compressor inlet
T2 = 62+273.15   # compressor outlet
T3 = 41.5+273.15   # condenser inlet
T4 = 2.2+273.15    # evaporator inlet
T5 = 1.4+273.15   # evaporator outlet

P1 = 3
P2 = 10.5

# plot the cycle
cycle.simple_solve_dt(T5, T3, P1, P2, 0.5, SI=True) #http://www.coolprop.org/apidoc/CoolProp.Plots.SimpleCyclesCompression.html
cycle.steps = 50
sc = cycle.get_state_changes()
plt.close(cycle.figure)
pp.draw_process(sc)

# plot the p-h diagram
pp.show()

# calculation for h and Q and COP
P1_pa = P1*101325
P2_pa = P2*101325

m = 0.00137361

working_fluid='R134a'

h1 = CP.PropsSI('H', 'T', T1, 'P', P1_pa, working_fluid) 
h2 = CP.PropsSI('H', 'T', T2, 'P', P2_pa, working_fluid)
h3 = CP.PropsSI('H', 'T', T3, 'P', P2_pa, working_fluid) 
h4 = CP.PropsSI('H', 'T', T4, 'P', P1_pa, working_fluid)
h5 = CP.PropsSI('H', 'T', T5, 'P', P1_pa, working_fluid) 

Q = m*(h1-h3)

print(" h1 =", h1, " h2 =",h2," h3 =", h3, " h4 =",h4," h5 =", h5, " Q =",Q)
