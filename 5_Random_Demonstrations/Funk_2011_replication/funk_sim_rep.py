import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
from scipy.stats.kde import gaussian_kde


n = 2000
sims = 2500

# Generating all the data
np.random.seed(20200513)

ids = []
for i in range(sims):
    ids.extend([i] * n)

df = pd.DataFrame()
df['sim_id'] = ids
z1 = np.random.normal(size=n*sims)
df['Z1'] = z1
z2 = np.random.normal(size=n*sims)
df['Z2'] = z2
z3 = np.random.binomial(n=1, p=0.3, size=n*sims)
df['Z3'] = z3
pr_x = (1+np.exp(-1*(1.5 + z1 - 2*z2 + z3)))**(-1)
x = np.where(pr_x < 0.91, 1, 0)
df['X'] = x
y = z1 + z3 + 2*np.random.normal(size=n*sims)
df['Y'] = y


def simulation_runner(ps_model, y_model):
    g_bias, i_bias, a_bias, a_cov = [[], [], [], []]
    f = sm.families.family.Binomial()

    # Looping through all sim IDs
    samples = list(df['sim_id'].unique())

    for i in samples:
        dfs = df.loc[df['sim_id'] == i].copy()

        # Propensity Score Model
        propensity_model = smf.glm(ps_model, dfs, family=f).fit()
        ps = propensity_model.predict(dfs)

        # Outcome Model
        outcome_model = smf.ols(y_model, dfs).fit()
        dfx = dfs.copy()
        dfx["X"] = 1
        y_x1 = outcome_model.predict(dfx)
        dfx["X"] = 0
        y_x0 = outcome_model.predict(dfx)

        y_obs = np.asarray(dfs['Y'])
        x_obs = np.asarray(dfs['X'])

        # G-formula estimate
        g_bias.append(np.mean(y_x1 - y_x0) - 0)

        # IPW estimate
        i_bias.append(np.mean((y_obs * x_obs) / ps - (y_obs * (1 - x_obs)) / (1 - ps)) - 0)

        # AIPW estimate
        y_x1_star = (y_obs * x_obs)/ps + (y_x1 * (ps - x_obs))/ps
        y_x0_star = (y_obs * (1 - x_obs))/(1 - ps) + (y_x0 * (x_obs - ps))/(1 - ps)
        pseudo_y = y_x1_star - y_x0_star
        ate = np.mean(pseudo_y)
        a_bias.append(ate - 0)
        var_ate = np.var(pseudo_y - ate, ddof=1) / dfs.shape[0]
        if (ate - 1.96*np.sqrt(var_ate) < 0) & (0 < ate + 1.96*np.sqrt(var_ate)):
            a_cov.append(1)
        else:
            a_cov.append(0)

    results = pd.DataFrame()
    results['g_bias'] = g_bias
    results['i_bias'] = i_bias
    results['a_bias'] = a_bias
    results['a_cov'] = a_cov
    return results


def print_sim_results(results):
    print("=================================")
    print("Bias")
    print("---------------------------------")
    print("G-comp:", np.mean(results['g_bias']))
    print("IPW:", np.mean(results['i_bias']))
    print("AIPW:", np.mean(results['a_bias']))
    print("---------------------------------")
    print("ESE")
    print("---------------------------------")
    print("G-comp:", np.std(results['g_bias'], ddof=1))
    print("IPW:", np.std(results['i_bias'], ddof=1))
    print("AIPW:", np.std(results['a_bias'], ddof=1))
    print("---------------------------------")
    print("Coverage")
    print("---------------------------------")
    print("AIPW:", np.mean(results['a_cov']))
    print("=================================")


def plot_sim_results(results, save=None):
    ax = plt.gca()
    bias = gaussian_kde(results['g_bias'])
    xvals = np.linspace(np.min(results['g_bias']), np.max(results['g_bias']), 100)
    ax.fill_between(xvals, bias(xvals), color='blue', alpha=0.2, label=None)
    ax.plot(xvals, bias(xvals), color='blue', alpha=1, label='G-comp')

    bias = gaussian_kde(results['i_bias'])
    xvals = np.linspace(np.min(results['i_bias']), np.max(results['i_bias']), 100)
    ax.fill_between(xvals, bias(xvals), color='red', alpha=0.2, label=None)
    ax.plot(xvals, bias(xvals), color='red', alpha=1, label='IPW')

    bias = gaussian_kde(results['a_bias'])
    xvals = np.linspace(np.min(results['a_bias']), np.max(results['a_bias']), 100)
    ax.fill_between(xvals, bias(xvals), color='purple', alpha=0.2, label=None)
    ax.plot(xvals, bias(xvals), color='purple', alpha=1, label='AIPW')

    ax.set_xlabel("Bias")
    ax.legend()
    plt.tight_layout()
    if save is not None:
        plt.savefig(save+".png", format='png', dpi=150)
    plt.close()


# Scenario 1
print("SCENARIO 1")
results = simulation_runner(ps_model="X ~ Z1 + Z3", y_model="Y ~ X + Z1 + Z3")
print_sim_results(results=results)
plot_sim_results(results=results, save='scenario_1')

# Scenarion 2
print("SCENARIO 2")
results = simulation_runner(ps_model="X ~ Z1", y_model="Y ~ X + Z1 + Z3")
print_sim_results(results=results)
plot_sim_results(results=results, save='scenario_2')

# Scenario 3
print("SCENARIO 3")
results = simulation_runner(ps_model="X ~ Z1 + Z3", y_model="Y ~ X + Z1")
print_sim_results(results=results)
plot_sim_results(results=results, save='scenario_3')

# Scenario 4
print("SCENARIO 4")
results = simulation_runner(ps_model="X ~ Z1", y_model="Y ~ X + Z1")
print_sim_results(results=results)
plot_sim_results(results=results, save='scenario_4')
