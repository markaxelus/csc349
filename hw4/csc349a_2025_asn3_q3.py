import numpy as np
import matplotlib.pyplot as plt

# x grid (ends at 5.98 by design)
x = np.arange(0.0, 6.0, 0.02)

# arrays the grader expects
fx = np.sqrt(x + 1)                                   # f(x)
px = 2 + (x - 3)/4 - ((x - 3)**2)/64                  # p(x)

# plot (red = f, blue = p) with legend
fig, ax = plt.subplots()
ax.plot(x, fx, color='red', label='f(x)')
ax.plot(x, px, color='blue', label='p(x)')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.legend()

# if your template asks for a file, keep this BEFORE show:
# plt.savefig('csc349a_2025_q3_plot.png', dpi=150, bbox_inches='tight')

plt.show()
