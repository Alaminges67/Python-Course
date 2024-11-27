import numpy as np
import matplotlib.pyplot as plt
labels=np.array(['A', 'B', 'C', 'D', 'E'])
values=np.array([4, 3, 2, 5, 4])
angles=np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
values=np.concatenate((values,[values[0]]))
angles=np.concatenate((angles,[angles[0]]))
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
ax.fill(angles, values, color='blue', alpha=0.25)
ax.plot(angles, values, color='blue', linewidth=2)
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
plt.show()