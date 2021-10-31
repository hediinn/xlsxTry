import numpy as np
from matplotlib import pyplota as plt
import quaternion

q1 = np.quaternion(1,2,3,4)
q2 = np.quaternion(5,6,7,8)

print(q1 * q2)

plt.imshow(q1,interpolation='nearest')
plt.show()
