
import numpy as np
import matplotlib.pyplot as plt

from ThemeBrand import themebrand as tb


#######################################
# CREATE FAKE DATA

x = np.arange(0, 10, 0.1)

y1 = np.sin(2*x)
y2 = np.sin(x + 0.2)
y3 = 0.3*np.sin(x)
y4 = -np.sin(x) + 0.2

#######################################
# INITIALIZE THE THEME

theme = tb()

# SET THE THEME

theme.set_dark_theme()

#######################################
# PLOT THE DATA

plt.figure(figsize=(12,8),
           layout="tight")

plt.plot(x, y1, linewidth=2, c='C0')
plt.plot(x, y2, linewidth=2, c='C1')
plt.plot(x, y3, linewidth=2, c='C2')
plt.plot(x, y4, linewidth=2, c='red')

plt.ylabel("Y axis text")
plt.xlabel("Long x axis text for font type and size testing")
# plt.savefig(f"test.png",dpi=300)
plt.show()
