import CoolProp
from CoolProp.Plots import PropertyPlot
from CoolProp.Plots import SimpleCompressionCycle
import matplotlib.pyplot as plt

# import sys
# import os

# # Add the parent directory of the current script to sys.path
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from modules import globalVariables


def systemCalculation():
    # introduce CoolProp
    CP = CoolProp.CoolProp

    # introduce Propertyplot for plotting p-h diagram and cycle
    pp = PropertyPlot("HEOS::R134a", "PH", unit_system="EUR")
    cycle = SimpleCompressionCycle("HEOS::R134a", "PH", unit_system="EUR")

    # T and P values. e- evaporator , c- condenser
    T1 = globalVariables.Parameters_MeasuredData["T1"] + 273.15  # compressor inlet
    T2 = globalVariables.Parameters_MeasuredData["T2"] + 273.15  # compressor outlet
    T3 = globalVariables.Parameters_MeasuredData["T3"] + 273.15  # condenser inlet
    T4 = globalVariables.Parameters_MeasuredData["T4"] + 273.15  # evaporator inlet
    T5 = globalVariables.Parameters_MeasuredData["T5"] + 273.1514  # evaporator outlet

    # T1 = 14.49+273.15   # compressor inlet
    # T2 = 68.02+273.15   # compressor outlet
    # T3 = 43.1+273.15   # condenser inlet
    # T4 = 3.65+273.15    # evaporator inlet
    # T5 = 2.82+273.15   # evaporator outlet

    P1 = globalVariables.Parameters_MeasuredData["P1"]
    P2 = globalVariables.Parameters_MeasuredData["P2"]
    # P1 = 2.41
    # P2 = 10.18
    ASP = globalVariables.Parameters_MeasuredData["ASP"]
    # ASP = 1011.6
    F = globalVariables.Parameters_MeasuredData["F"]
    # F= 4.43

    # plot the p-h diagram
    pp.calc_isolines()

    # plot the cycle, 0.7 is the Isentropic compressor efficiency, need calculate in our experiment
    cycle.simple_solve_dt(
        T5, T3, P1 + 1, P2 + 1, 0.7, SI=True
    )  # http://www.coolprop.org/apidoc/CoolProp.Plots.SimpleCyclesCompression.html
    cycle.steps = 50
    sc = cycle.get_state_changes()
    plt.close(cycle.figure)
    pp.draw_process(sc)
    # plt.close(cycle.figure)

    # plot the p-h diagram

    pp.title("R134a P-H Diagram")
    pp.savefig("server/uuid/test.png", dpi=100, bbox_inches="tight")
    # pp.show()

    # show the diagram by plt while it's doesn't work, need to use api from propertyPlot
    # plt.title("p-h diagram")
    # plt.show()
    # plt.savefig('p_h_diagram2.png')

    # calculation for h and Q and COP
    P1_pa = P1 * 100000 + ASP * 100000
    P2_pa = P2 * 100000 + ASP * 100000

    m_Sys = F * 1.15 / 3600  # Mass flowrate m(Kg/s)

    working_fluid = "R134a"

    h1_Sys = CP.PropsSI("H", "T", T1, "P", P1_pa, working_fluid)
    h2_Sys = CP.PropsSI("H", "T", T2, "P", P2_pa, working_fluid)
    h3_Sys = CP.PropsSI("H", "T", T3, "P", P2_pa, working_fluid)
    h4_Sys = CP.PropsSI("H", "T", T4, "P", P1_pa, working_fluid)
    h5_Sys = CP.PropsSI("H", "T", T5, "P", P1_pa, working_fluid)

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

    QL_Sys = m_Sys * (h1_Sys - h4_Sys)  # Refrigeration capacity QL(KW)
    W_Sys = m_Sys * (h2_Sys - h1_Sys)  # Compressor work W(KW)
    QH_Sys = m_Sys * (h2_Sys - h3_Sys)  # Condensation capacity QH(KW)

    COP_Sys = QL_Sys / W_Sys  # Coefficient of performance COP
    n_Sys = P2 / P1  # Compressor compression ratio η

    # print the value of calculation
    # print(" h1 =", h1, " h2 =",h2," h3 =", h3, " h4 =",h4," h5 =", h5, " Q =",Q, " Qcp =",Qcp)
    # print(" h11 =", h11, " h21 =",h21," h31 =", h31, " h41 =",h41," h51 =", h51, " Q =",Q)

    # This part Quality(0(liquid)-1(vapor)) and temperature are need for calculation.
    # Calculate saturation liquid pressure based on the temperature and quality
    T_l_input = T3
    pp.state.update(
        CoolProp.QT_INPUTS, 0.0, T_l_input
    )  # Q means quality Quality (Q) is a dimensionless quantity that represents the ratio of the mass of vapor to the total mass (vapor + liquid) in a two-phase mixture. Its value ranges from 0 (saturated liquid) to 1 (saturated vapor).Temperature (T) is the thermodynamic temperature of the fluid.
    p_l = pp.state.keyed_output(CoolProp.iP)
    # Calculate saturation vapor pressure based on the temperature and quality
    T_v_input = T5
    pp.state.update(CoolProp.QT_INPUTS, 1.0, T_v_input)
    p_v = pp.state.keyed_output(CoolProp.iP)
    # Calculate saturation vapor tempreature based on the pressure and quality
    p_v_input = P1_pa
    pp.state.update(CoolProp.PQ_INPUTS, p_v_input, 1)
    T_v = pp.state.keyed_output(CoolProp.iT) - 273.15
    # Calculate saturation liquid tempreature based on the pressure and quality
    p_l_input = P2_pa
    pp.state.update(CoolProp.PQ_INPUTS, p_l_input, 0)
    T_l = pp.state.keyed_output(CoolProp.iT) - 273.15

    # print the pressure and temperature under staturation phase
    print("p_l = ", p_l, "p_v = ", p_v, "T_v=", T_v, "T_l", T_l)

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

    # update system calculation values in the global val
    globalVariables.Parameters_SystemCaculation.update(
        {
            # system calcualtion data
            "H1_Sys": h1_Sys,
            "H2_Sys": h2_Sys,
            "H3_Sys": h3_Sys,
            "H4_Sys": h4_Sys,
            "H5_Sys": h5_Sys,
            "m_Sys": m_Sys,
            "QL_Sys": QL_Sys,
            "QH_Sys": QH_Sys,
            "W_Sys": W_Sys,
            "COP_Sys": COP_Sys,
            "n_Sys": n_Sys,
        }
    )

    # get students calculation data
    H1_Stu = globalVariables.Parameters_StudentCaculation["H1_Stu"]
    H2_Stu = globalVariables.Parameters_StudentCaculation["H2_Stu"]
    H3_Stu = globalVariables.Parameters_StudentCaculation["H3_Stu"]
    H4_Stu = globalVariables.Parameters_StudentCaculation["H4_Stu"]
    H5_Stu = globalVariables.Parameters_StudentCaculation["H5_Stu"]
    m_Stu = globalVariables.Parameters_StudentCaculation["m_Stu"]
    QL_Stu = globalVariables.Parameters_StudentCaculation["QL_Stu"]
    QH_Stu = globalVariables.Parameters_StudentCaculation["QH_Stu"]
    W_Stu = globalVariables.Parameters_StudentCaculation["W_Stu"]
    COP_Stu = globalVariables.Parameters_StudentCaculation["COP_Stu"]
    n_Stu = globalVariables.Parameters_StudentCaculation["n_Stu"]

    # calculate deviation between students calculation and system calculation
    H1_Dev = (h1_Sys - H1_Stu * 1000) / h1_Sys
    H2_Dev = (h2_Sys - H2_Stu * 1000) / h2_Sys
    H3_Dev = (h3_Sys - H3_Stu * 1000) / h3_Sys
    H4_Dev = (h4_Sys - H4_Stu * 1000) / h4_Sys
    H5_Dev = (h5_Sys - H5_Stu * 1000) / h5_Sys
    m_Dev = (m_Sys - m_Stu) / m_Sys
    QL_Dev = (QL_Sys - QL_Stu) / QL_Sys
    QH_Dev = (QH_Sys - QH_Stu) / QH_Sys
    W_Dev = (W_Sys - W_Stu) / W_Sys
    COP_Dev = (COP_Sys - COP_Stu) / COP_Sys
    n_Dev = (n_Sys - n_Stu) / n_Sys

    # updata deviation values in the global val
    globalVariables.Parameters_DeviationCaculation.update(
        {
            "H1_Dev": "{:.0%}".format(abs(H1_Dev)),
            "H2_Dev": "{:.0%}".format(abs(H2_Dev)),
            "H3_Dev": "{:.0%}".format(abs(H3_Dev)),
            "H4_Dev": "{:.0%}".format(abs(H4_Dev)),
            "H5_Dev": "{:.0%}".format(abs(H5_Dev)),
            "m_Dev": "{:.0%}".format(abs(m_Dev)),
            "QL_Dev": "{:.0%}".format(abs(QL_Dev)),
            "QH_Dev": "{:.0%}".format(abs(QH_Dev)),
            "W_Dev": "{:.0%}".format(abs(W_Dev)),
            "COP_Dev": "{:.0%}".format(abs(COP_Dev)),
            "n_Dev": "{:.0%}".format(abs(n_Dev)),
        }
    )

    # update saturation values in the global val
    globalVariables.Parameters_SaturatedValue.update(
        {
            "SaturT_P1": T_v,
            "SaturT_P2": T_l,
            "SaturP_T3": p_l,
            "SaturP_T5": p_v,
        }
    )

#     print(globalVariables.Parameters_SaturatedValue)
# systemCalculation()