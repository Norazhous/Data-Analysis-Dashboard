import CoolProp
from CoolProp.Plots import PropertyPlot
from CoolProp.Plots import SimpleCompressionCycle
import matplotlib.pyplot as plt

# introduce CoolProp
CP = CoolProp.CoolProp

# introduce Propertyplot for plotting p-h diagram and cycle
pp = PropertyPlot('HEOS::R134a', 'PH', unit_system='EUR')
cycle = SimpleCompressionCycle('HEOS::R134a', 'PH', unit_system='EUR')

# T and P values. e- evaporator , c- condenser
T1 = 14.49+273.15   # compressor inlet
T2 = 68.02+273.15   # compressor outlet
T3 = 43.1+273.15   # condenser inlet
T4 = 3.65+273.15    # evaporator inlet
T5 = 2.82+273.15   # evaporator outlet

P1 = 2.41
P2 = 10.18

PSA = 1011.6

F= 4.43

# plot the p-h diagram
pp.calc_isolines()

# plot the cycle, 0.7 is the Isentropic compressor efficiency, need calculate in our experiment 
cycle.simple_solve_dt(T5, T3, P1+1, P2+1, 0.7, SI=True) #http://www.coolprop.org/apidoc/CoolProp.Plots.SimpleCyclesCompression.html
cycle.steps = 50
sc = cycle.get_state_changes()
plt.close(cycle.figure)
pp.draw_process(sc)
# plt.close(cycle.figure)

# plot the p-h diagram

pp.title("R134a P-H Diagram")
pp.savefig('./plotDiagram/R134_p_h_diagram_with_cycle.svg',dpi=300, bbox_inches='tight')
pp.show()

# show the diagram by plt while it's doesn't work, need to use api from propertyPlot
# plt.title("p-h diagram")
# plt.show()
# plt.savefig('p_h_diagram2.png')

# calculation for h and Q and COP
P1_pa = P1*100000 + PSA *100
P2_pa = P2*100000 + PSA *100

m = F*1.15/3600

working_fluid='R134a'

h1 = CP.PropsSI('H', 'T', T1, 'P', P1_pa, working_fluid) 
h2 = CP.PropsSI('H', 'T', T2, 'P', P2_pa, working_fluid)
h3 = CP.PropsSI('H', 'T', T3, 'P', P2_pa, working_fluid) 
h4 = CP.PropsSI('H', 'T', T4, 'P', P1_pa, working_fluid)
h5 = CP.PropsSI('H', 'T', T5, 'P', P1_pa, working_fluid) 

# pp.state.update(CoolProp.PT_INPUTS,P1_pa,T1)
# h11 = pp.state.keyed_output(CoolProp.iHmass) 

# pp.state.update(CoolProp.PT_INPUTS,P2_pa,T2)
# h21 = pp.state.keyed_output(CoolProp.iHmass) 

# pp.state.update(CoolProp.PT_INPUTS,P2_pa,T3)
# h31 = pp.state.keyed_output(CoolProp.iHmass) 

# pp.state.update(CoolProp.PT_INPUTS,P1_pa,T4)
# h41 = pp.state.keyed_output(CoolProp.iHmass) 

# pp.state.update(CoolProp.PT_INPUTS,P1_pa,T5)
# h51 = pp.state.keyed_output(CoolProp.iHmass) 

Q = m*(h1-h3)
Qcp = m*(h2-h1)

# print the value of calculation 
print(" h1 =", h1, " h2 =",h2," h3 =", h3, " h4 =",h4," h5 =", h5, " Q =",Q, " Qcp =",Qcp)
# print(" h11 =", h11, " h21 =",h21," h31 =", h31, " h41 =",h41," h51 =", h51, " Q =",Q)


# This part Quality(0(liquid)-1(vapor)) and temperature are need for calculation.
# Calculate saturation liquid pressure based on the temperature and quality
T_l_input = T3
pp.state.update(CoolProp.QT_INPUTS,0.0,T_l_input) # Q means quality Quality (Q) is a dimensionless quantity that represents the ratio of the mass of vapor to the total mass (vapor + liquid) in a two-phase mixture. Its value ranges from 0 (saturated liquid) to 1 (saturated vapor).Temperature (T) is the thermodynamic temperature of the fluid. 
p_l = pp.state.keyed_output(CoolProp.iP)
# Calculate saturation vapor pressure based on the temperature and quality
T_v_input = T5
pp.state.update(CoolProp.QT_INPUTS,1.0,T_v_input)
p_v = pp.state.keyed_output(CoolProp.iP)
# Calculate saturation vapor tempreature based on the pressure and quality
p_v_input = P1_pa
pp.state.update(CoolProp.PQ_INPUTS,p_v_input,1)
T_v = pp.state.keyed_output(CoolProp.iT) -273.15
# Calculate saturation liquid tempreature based on the pressure and quality
p_l_input = P2_pa
pp.state.update(CoolProp.PQ_INPUTS,p_l_input,0)
T_l = pp.state.keyed_output(CoolProp.iT) -273.15

# print the pressure and temperature under staturation phase
print ("p_l = ",p_l, "p_v = ", p_v, "T_v=", T_v, "T_l", T_l)

# plot the saturation cycle
# pp.calc_isolines(CoolProp.iT, [T0-273.15,T2-273.15], num=2)
# cycle.simple_solve(T2, p0, T0, p2, 0.7, SI=True)
# cycle.steps = 50
# sc = cycle.get_state_changes()
# # sc.set_color('blue')
# pp.draw_process(sc,line_opts={'color':'blue', 'lw':1.5})
# plt.close(cycle.figure)
# pp.show()
# print ("P0 = ",p0, "P2 = ", p2)
