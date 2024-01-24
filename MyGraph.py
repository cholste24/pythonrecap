import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)
plt.plot(x, np.sin(x))

plt.show()

print("Hello World!")

# Creating a Virtual Environment
# 1. Create a VE - mac: python3 -m venv myvenv
#                - pc: py -3 -m venv _____
# 2. Activate the VE - mac: source myvenv/bin/activate
#                    - pc: myvenv/scripts/activate
# 3. Install 3rd party library/module: pip3 install _______