from __future__ import division, print_function
import matplotlib
matplotlib.use('Agg') #Force mpl to use a non-GUI backend

import matplotlib.pyplot as plt
from CoolProp.Plots.ConsistencyPlots import ConsistencyFigure

ff = ConsistencyFigure('R134a')
ff.savefig('R134a.png', dpi = 30)
ff.savefig('R134a.pdf')
plt.close()
del ff
