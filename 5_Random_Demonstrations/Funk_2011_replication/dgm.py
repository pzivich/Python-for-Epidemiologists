import numpy as np
import pandas as pd

n = 5000

# Generating covariates
z1 = np.random.normal(size=n)
z2 = np.random.normal(size=n)
z3 = np.random.binomial(n=1, p=0.3, size=n)

# Generating exposure data
pr_x = (1+np.exp(-1*(1.5 + z1 - 2*z2 + z3)))**(-1)
x = np.where(pr_x < 0.91, 1, 0)

# Generating outcome data
y = z1 + z3 + 2*np.random.normal(size=n)

# Stacking in pandas DataFrame for export
df = pd.DataFrame()
df['Z1'] = z1
df['Z2'] = z2
df['Z3'] = z3
df['X'] = x
df['Y'] = y
df.to_csv("dr_data.csv", index=False)
