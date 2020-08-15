import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import animation
import statsmodels.api as sm
import statsmodels.formula.api as smf
from scipy.stats import logistic

np.random.seed(1986)


# Defining some functions to help out
def generate_stg_positions(data):
    for i, r in data.iterrows():
        data.loc[i, 'pos0'] = 0
        if r['L0'] == 1:
            data.loc[i, 'pos1'] = 1
            if r['A0'] == 1:
                data.loc[i, 'pos2'] = 1 + 0.5
                if r['L1'] == 1:
                    data.loc[i, 'pos3'] = 1 + 0.5 + 0.25
                    if r['A1'] == 1:
                        data.loc[i, 'pos4'] = 1 + 0.5 + 0.25 + 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = 1 + 0.5 + 0.25 + 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = 1 + 0.5 + 0.25 + 0.125 - 0.0625
                    else:
                        data.loc[i, 'pos4'] = 1 + 0.5 + 0.25 - 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = 1 + 0.5 + 0.25 - 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = 1 + 0.5 + 0.25 - 0.125 - 0.0625
                else:
                    data.loc[i, 'pos3'] = 1 + 0.5 - 0.25
                    if r['A1'] == 1:
                        data.loc[i, 'pos4'] = 1 + 0.5 - 0.25 + 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = 1 + 0.5 - 0.25 + 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = 1 + 0.5 - 0.25 + 0.125 - 0.0625
                    else:
                        data.loc[i, 'pos4'] = 1 + 0.5 - 0.25 - 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = 1 + 0.5 - 0.25 - 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = 1 + 0.5 - 0.25 - 0.125 - 0.0625
            else:
                data.loc[i, 'pos2'] = 1 - 0.5
                if r['L1'] == 1:
                    data.loc[i, 'pos3'] = 1 - 0.5 + 0.25
                    if r['A1'] == 1:
                        data.loc[i, 'pos4'] = 1 - 0.5 + 0.25 + 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = 1 - 0.5 + 0.25 + 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = 1 - 0.5 + 0.25 + 0.125 - 0.0625
                    else:
                        data.loc[i, 'pos4'] = 1 - 0.5 + 0.25 - 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = 1 - 0.5 + 0.25 - 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = 1 - 0.5 + 0.25 - 0.125 - 0.0625
                else:
                    data.loc[i, 'pos3'] = 1 - 0.5 - 0.25
                    if r['A1'] == 1:
                        data.loc[i, 'pos4'] = 1 - 0.5 - 0.25 + 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = 1 - 0.5 - 0.25 + 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = 1 - 0.5 - 0.25 + 0.125 - 0.0625
                    else:
                        data.loc[i, 'pos4'] = 1 - 0.5 - 0.25 - 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = 1 - 0.5 - 0.25 - 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = 1 - 0.5 - 0.25 - 0.125 - 0.0625
        else:
            data.loc[i, 'pos1'] = -1
            if r['A0'] == 1:
                data.loc[i, 'pos2'] = -1 + 0.5
                if r['L1'] == 1:
                    data.loc[i, 'pos3'] = -1 + 0.5 + 0.25
                    if r['A1'] == 1:
                        data.loc[i, 'pos4'] = -1 + 0.5 + 0.25 + 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = -1 + 0.5 + 0.25 + 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = -1 + 0.5 + 0.25 + 0.125 - 0.0625
                    else:
                        data.loc[i, 'pos4'] = -1 + 0.5 + 0.25 - 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = -1 + 0.5 + 0.25 - 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = -1 + 0.5 + 0.25 - 0.125 - 0.0625
                else:
                    data.loc[i, 'pos3'] = -1 + 0.5 - 0.25
                    if r['A1'] == 1:
                        data.loc[i, 'pos4'] = -1 + 0.5 - 0.25 + 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = -1 + 0.5 - 0.25 + 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = -1 + 0.5 - 0.25 + 0.125 - 0.0625
                    else:
                        data.loc[i, 'pos4'] = -1 + 0.5 - 0.25 - 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = -1 + 0.5 - 0.25 - 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = -1 + 0.5 - 0.25 - 0.125 - 0.0625
            else:
                data.loc[i, 'pos2'] = -1 - 0.5
                if r['L1'] == 1:
                    data.loc[i, 'pos3'] = -1 - 0.5 + 0.25
                    if r['A1'] == 1:
                        data.loc[i, 'pos4'] = -1 - 0.5 + 0.25 + 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = -1 - 0.5 + 0.25 + 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = -1 - 0.5 + 0.25 + 0.125 - 0.0625
                    else:
                        data.loc[i, 'pos4'] = -1 - 0.5 + 0.25 - 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = -1 - 0.5 + 0.25 - 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = -1 - 0.5 + 0.25 - 0.125 - 0.0625
                else:
                    data.loc[i, 'pos3'] = -1 - 0.5 - 0.25
                    if r['A1'] == 1:
                        data.loc[i, 'pos4'] = -1 - 0.5 - 0.25 + 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = -1 - 0.5 - 0.25 + 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = -1 - 0.5 - 0.25 + 0.125 - 0.0625
                    else:
                        data.loc[i, 'pos4'] = -1 - 0.5 - 0.25 - 0.125
                        if r['Y'] == 1:
                            data.loc[i, 'pos5'] = -1 - 0.5 - 0.25 - 0.125 + 0.0625
                        else:
                            data.loc[i, 'pos5'] = -1 - 0.5 - 0.25 - 0.125 - 0.0625

    return data


# Plot Structure Tree Graph
def plot_stg(ax, data, color='gray', alpha=0.1, with_annots=False):
    xcoords = [0, 1, 2, 3, 4, 5]
    yrow_pos = ['pos0', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5']
    for i, r in data.iterrows():
        ax.plot(xcoords, list(r[yrow_pos]), '-', color=color, alpha=alpha)

    if with_annots:
        plt.rcParams.update({'font.size': 10})
        ax.text(1.1, 0.95, r"$L_0 = 1$")
        ax.text(1.1, -1.05, r"$L_0 = 0$")
        for i in range(2):
            ax.text(2.1, 1.5 - i * 2 - 0.04, r"$A_0=1$")
            ax.text(2.1, 1.5 - i * 2 - 0.04 - 1, r"$A_0=0$")
        for i in range(4):
            ax.text(3.1, 1.75 - i * 1 - 0.04, r"$L_1=1$")
            ax.text(3.1, 1.75 - i * 1 - 0.04 - 0.5, r"$L_1=0$")
        for i in range(8):
            ax.text(4.1, 1.875 - i * 0.5 - 0.04, r"$A_1=1$")
            ax.text(4.1, 1.875 - i * 0.5 - 0.04 - 0.25, r"$A_1=0$")
        for i in range(16):
            ax.text(5.1, 1.9375 - i * 0.25 - 0.04, r"$Y=1$")
            ax.text(5.1, 1.9375 - i * 0.25 - 0.04 - 0.125, r"$Y=0$")
    else:
        plt.rcParams.update({'font.size': 12})
        ax.text(1, 2, r"$L_0$")
        ax.text(2, 2, r"$A_0$")
        ax.text(3, 2, r"$L_1$")
        ax.text(4, 2, r"$A_1$")
        ax.text(5, 2, r"$Y$")

    ax.axis('off')
    return ax


############################################
# Generate a data set
############################################
n = 200
data = pd.DataFrame()
data['L0'] = np.random.binomial(n=1, p=0.67, size=n)
data['A0'] = np.random.binomial(n=1, p=logistic.cdf(-0.1 - 0.4*data['L0']), size=n)
data['L1'] = np.random.binomial(n=1, p=logistic.cdf(0.6 + 0.4*data['L0'] - 0.35*data['A0']), size=n)
data['A1'] = np.random.binomial(n=1, p=logistic.cdf(0.1 - 0.4*data['L1'] + 0.25*data['A0']), size=n)
data['Y'] = np.random.binomial(n=1,
                               p=logistic.cdf(-1.5 + 0.4*data['L0'] - 0.3*data['A0'] + 0.4*data['L1'] - 0.2*data['A1']),
                               size=n)

############################################
# Plot STG
############################################

# Define Structured Tree Graph positions
data = generate_stg_positions(data)

fig, ax = plt.subplots()
plot_stg(ax, data, color='gray', alpha=0.1)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots()
plot_stg(ax, data, color='gray', alpha=0.1, with_annots=True)
plt.tight_layout()
plt.show()

# STG - Point Treatment
fig, ax = plt.subplots()
plot_stg(ax, data, color='lightgray', alpha=1)
plot_stg(ax, data.loc[data['A0'] == 1], color='navy', alpha=1)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots()
plot_stg(ax, data, color='lightgray', alpha=1)
plot_stg(ax, data.loc[data['A0'] == 0], color='darkred', alpha=1)
plt.tight_layout()
plt.show()

# STG - Time-varying treatment
fig, ax = plt.subplots()
plot_stg(ax, data, color='lightgray', alpha=1)
plot_stg(ax, data.loc[(data['A0'] == 1) & (data['A1'] == 1)], color='blue', alpha=1)
plt.tight_layout()
plt.show()

fig, ax = plt.subplots()
plot_stg(ax, data, color='lightgray', alpha=1)
plot_stg(ax, data.loc[(data['A0'] == 0) & (data['A1'] == 0)], color='red', alpha=1)
plt.tight_layout()
plt.show()

############################################
# Animated Individual Trajectories
############################################
fig, ax = plt.subplots()
ax.set_ylim([-2, 2])
ax.set_xlim([-0.1, 5.1])
# ax.set_ylabel(r"$E[Y(\alpha)]$")
# ax.set_xlabel(r"$\alpha$")

plot_stg(ax, data, color='lightgray', alpha=1, with_annots=False)
line, = ax.plot([0, 1, 2, 3, 4, 5], list(data.loc[0,
                                                  ['pos0', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5']]),
                '-', color='k', alpha=1)

def animate(i):
    ax.collections.clear()
    line.set_ydata(list(data.loc[i, ['pos0', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5']]))  # update the data
    return line, ax


ani = animation.FuncAnimation(fig, animate, range(0, 100),
                              interval=250, blit=False)
# ani.save("C:/Users/zivic/Desktop/data_gif.gif", writer='imagemagick', fps=10)
plt.show()

############################################
# Parametric g-formula
############################################

# 1: estimating models on observed data
f = sm.families.family.Binomial()
# m_a0 = smf.glm("A0 ~ L0", data, family=f).fit()
m_l1 = smf.glm("L1 ~ L0 + A0", data, family=f).fit()
# m_a1 = smf.glm("A1 ~ L1 + A0", data, family=f).fit()
m_y = smf.glm("Y ~ L0 + L1 + A0 + A1", data, family=f).fit()

# 2: re-sample with replacement
rata = data.sample(n=1000, replace=True).reset_index(drop=True)
rata = rata[['L0', 'A0']].copy()

# 3a: predict forward into future for A0=1, A1=1
rata['A0'] = 1
pL1 = m_l1.predict(rata)
rata['L1'] = np.random.binomial(n=1, p=pL1, size=rata.shape[0])
rata['A1'] = 1
pY = m_y.predict(rata)
rata['Y'] = np.random.binomial(n=1, p=pY, size=rata.shape[0])
rata = generate_stg_positions(rata)

fig, ax = plt.subplots()
ax.axis('off')
plt.rcParams.update({'font.size': 12})
ax.text(1, 2, r"$L_0$")
ax.text(2, 2, r"$A_0$")
ax.text(3, 2, r"$L_1$")
ax.text(4, 2, r"$A_1$")
ax.text(5, 2, r"$Y$")
line, = ax.plot([0, 1, 2, 3, 4, 5], list(rata.loc[0, ['pos0', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5']]),
                '-', color='blue', alpha=0.05)
ax.set_ylim([-2, 2])
ax.set_xlim([-0.1, 5.1])

def animate(i):
    line, = ax.plot([0, 1, 2, 3, 4, 5], list(rata.loc[i, ['pos0', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5']]),
                    '-', color='blue', alpha=0.05)
    return line, ax

ani = animation.FuncAnimation(fig, animate, range(0, 200),
                              interval=10, blit=False)
# ani.save("save_file.gif", writer='imagemagick', fps=60)
plt.show()

# 4a: predict forward into future for A0=0, A1=0
rata['A0'] = 0
pL1 = m_l1.predict(rata)
rata['L1'] = np.random.binomial(n=1, p=pL1, size=rata.shape[0])
rata['A1'] = 0
pY = m_y.predict(rata)
rata['Y'] = np.random.binomial(n=1, p=pY, size=rata.shape[0])
rata = generate_stg_positions(rata)

fig, ax = plt.subplots()
ax.axis('off')
plt.rcParams.update({'font.size': 12})
ax.text(1, 2, r"$L_0$")
ax.text(2, 2, r"$A_0$")
ax.text(3, 2, r"$L_1$")
ax.text(4, 2, r"$A_1$")
ax.text(5, 2, r"$Y$")
line, = ax.plot([0, 1, 2, 3, 4, 5], list(rata.loc[0, ['pos0', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5']]),
                '-', color='red', alpha=0.05)
ax.set_ylim([-2, 2])
ax.set_xlim([-0.1, 5.1])

def animate(i):
    line, = ax.plot([0, 1, 2, 3, 4, 5], list(rata.loc[i, ['pos0', 'pos1', 'pos2', 'pos3', 'pos4', 'pos5']]),
                    '-', color='red', alpha=0.05)
    return line, ax

ani = animation.FuncAnimation(fig, animate, range(0, 200),
                              interval=10, blit=False)
# ani.save("save_file.gif", writer='imagemagick', fps=60)
plt.show()
