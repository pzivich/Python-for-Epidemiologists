# zepid walkthrough
This is a walkthrough of the zepid package and its content functions

## First we will import some other packages and zepid
```python
#Import other packages
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.genmod.families import family
from statsmodels.genmod.families import links
#Import zepid
import zepid as ze
```
Now, let's import the example dataset for the analysis
```python
#Load sample dataframe
df = ze.datex()
df.info()
```
## Basic Measures of Association
Let's calculate the Odds Ratio and its corresponding 95% Confidence Interval
```python
ze.OddsRatio(df['exposure'],df['outcome'])
```
This function will produce the following output
```
outcome    0.0  1.0
exposure           
0.0       1822  533
1.0        513  293 

----------------------------------------------------------------------
Odds in exposed:  0.571
Odds in unexposed:  0.293
----------------------------------------------------------------------
Odds Ratio:  1.952
95.0% two-sided CI: ( 1.642 ,  2.321 )
Confidence Limit Ratio:  1.413
----------------------------------------------------------------------
```
We can also calculate other measures of association by using the following functions:
```python
ze.RelRisk(df['exposure'],df['outcome']) #calculates the Risk Ratio / Relative Risk
ze.RiskDiff(df['exposure'],df['outcome']) #calculates the Risk Difference
ze.NNT(df['exposure'],df['outcome']) #calculates the Number Needed to Treat/Harm
```
## Assess Collinearity
### Binary - Continuous
To assess collinearity between a continuous variable and binary variables, we can use Standardized Mean Differences. To calculate Standard Mean Differences, we can use the following function:
```python
ze.StandMeanDiff(df,'exposure','continuous')
```
Which produces the following output
```
----------------------------------------------------------------------
Standardized Mean Difference: 0.068
----------------------------------------------------------------------
```
### Categorical - Continuous
For variables with more than two categories, piecewise Standard Mean Differences need to be calculate. To do this, we will obtain the estimates and store them as variables. We will then use zepid.calc to calculate the Standard Mean Differences from the summary information
```python
df.category.value_counts() #getting n for each category
c0mean = np.mean(df.loc[df.category==0]['continuous']) #extracting the mean
c0std = np.std(df.loc[df.category==0]['continuous']) #extracting the standard deviation
c1mean = np.mean(df.loc[df.category==1]['continuous']) #extracting the mean
c1std = np.std(df.loc[df.category==1]['continuous']) #extracting the standard deviation
c2mean = np.mean(df.loc[df.category==2]['continuous']) #extracting the mean
c2std = np.std(df.loc[df.category==2]['continuous']) #extracting the standard deviation

ze.calc.stand_mean_diff(1900,859,c2mean,c0mean,c2std,c0std,decimal=5)
ze.calc.stand_mean_diff(1900,668,c2mean,c1mean,c2std,c1std,decimal=5)
```
Which will produce the following output
```
----------------------------------------------------------------------
Standardized Mean Difference: 0.0104
----------------------------------------------------------------------
----------------------------------------------------------------------
Standardized Mean Difference: 0.01776
----------------------------------------------------------------------
```
### Binary - Binary
To see whether there is collinearity between two binary variables, we use the odds ratio
```python
ze.OddsRatio(df['exposure'],df['binary'])
```
Which produces the following output
```
binary     0.0   1.0
exposure            
0.0       1036  1534
1.0        837    20 

----------------------------------------------------------------------
Odds in exposed:  0.024
Odds in unexposed:  1.481
----------------------------------------------------------------------
Odds Ratio:  0.016
95.0% two-sided CI: ( 0.01 ,  0.025 )
Confidence Limit Ratio:  2.462
----------------------------------------------------------------------
```
Note that there is evidence of collinearity, but we will ignore this issue through the rest of our example

### Categorical - Binary
For a categorical variables, we must again use the summary calculations contained in zepid.calc
```python
pd.crosstab(df['exposure'],df['category'])
ze.calc.oddr(a=80,b=588,c=747,d=1153)
ze.calc.oddr(30,829,747,1153)
```
Which produces the following output
```
----------------------------------------------------------------------
Odds exposed: 0.136
Odds unexposed: 0.648
----------------------------------------------------------------------
Odds Ratio: 0.21
95.0% two-sided CI: ( 0.163 ,  0.27 )
----------------------------------------------------------------------
----------------------------------------------------------------------
Odds exposed: 0.036
Odds unexposed: 0.648
----------------------------------------------------------------------
Odds Ratio: 0.056
95.0% two-sided CI: ( 0.038 ,  0.081 )
----------------------------------------------------------------------
```
Again, we have evidence of collinearity but we will ignore the methodological ramifications of this in our example
## Functional form of continuous variable
To do a functional form assessment, we first have to decide on some possible functional forms and code new variables. We will assess; linear, quadratic, categorical, and restricted quadratic spline. First, creating a quadratic and categorical variable
```python
df['cont_sq'] = df['continuous']**2
df.loc[df.continuous<20,'ccat'] = 0
df.loc[((df.continuous<40)&(df.continuous>=20)),'ccat'] = 1
df.loc[((df.continuous<60)&(df.continuous>=40)),'ccat'] = 2
df.loc[((df.continuous<80)&(df.continuous>=60)),'ccat'] = 3
df.loc[((df.continuous<=100)&(df.continuous>=80)),'ccat'] = 4
```
### Spline 
To generate a spline, we can use the zepid function spline. spline is used to generate any order term spline model with either user-specified spline knots or automatically generated spline knot locations. Additionally, whether a restricted spline model is used can be chosen. For our example, we will create a restricted (restricted=True) quadratic spline (term=2) spline with five knots (n_knots=5). We will let the function determine where the knots will be located.
```python
df[['rs1','rs2','rs3','rs4']] = ze.spline(df,'continuous',n_knots=5,term=2,restricted=True)
```
### Functional form plots
Now that our potential forms are coded, we can create some function form plots. 
#### Linear
First we will look at our linear functional form
```python
ze.graphics.func_form_plot(df,'outcome','continuous',ylims=[0.15,0.5]) #linear
```
Which produces the following output
```
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:                outcome   No. Observations:                 3161
Model:                            GLM   Df Residuals:                     3159
Model Family:                Binomial   Df Model:                            1
Link Function:                  logit   Scale:                             1.0
Method:                          IRLS   Log-Likelihood:                -1798.8
Date:                Mon, 18 Dec 2017   Deviance:                       3597.6
Time:                        08:02:01   Pearson chi2:                 3.17e+03
No. Iterations:                     4                                         
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     -1.4498      0.084    -17.305      0.000      -1.614      -1.286
continuous     0.0081      0.001      5.788      0.000       0.005       0.011
==============================================================================
```
and image

![alt text](https://github.com/pzivich/zepid/blob/master/images/linear_funcform.png "Linear Functional Form")

For our other functional form assessments, we obtain the following plots
#### Quadratic
```python 
ze.graphics.func_form_plot(df,'outcome','continuous','continuous + cont_sq',ylims=[0.15,0.5])
```

![alt text](https://github.com/pzivich/zepid/blob/master/images/quad_funcform.png "Quadratic Functional Form")
#### Categorical
```python 
ze.graphics.func_form_plot(df,'outcome','continuous','C(ccat)',ylims=[0.15,0.5])
```

![alt text](https://github.com/pzivich/zepid/blob/master/images/cat_funcform.png "Categorical Functional Form")
#### Restricted Quadratic Spline
```python 
ze.graphics.func_form_plot(df,'outcome','continuous','continuous + rs1 + rs2 + rs3 + rs4',ylims=[0.15,0.5])
```

![alt text](https://github.com/pzivich/zepid/blob/master/images/rqs_funcform.png "Restricted Quadratic Spline Functional Form")

Based on these results, we will use a quadratic functional form for our continuous variable

## Inverse Probability Weights
Currently, both IPW for missingness and IPW for treatment are supported. Let's look at each of these
### Inverse Probability of Missingness Weights
We can see that our outcome variable is missing some data. Therefore, let's weight our data by missingness due to the categorical variables
```python
m,df['ipmw_weight'] = ze.ipw.ipmw(df,'outcome','C(category)')
```
The above function with produce the weights as a new column, which we have labelled as 'ipmw_weight'. Since we do not care about the probabilities, we just set them equal to 'm'. The following model fit output will be printed
```
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:                    obs   No. Observations:                 3427
Model:                            GLM   Df Residuals:                     3424
Model Family:                Binomial   Df Model:                            2
Link Function:                  logit   Scale:                             1.0
Method:                          IRLS   Log-Likelihood:                -816.08
Date:                Mon, 18 Dec 2017   Deviance:                       1632.2
Time:                        08:20:15   Pearson chi2:                 3.43e+03
No. Iterations:                     6                                         
======================================================================================
                         coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------------
Intercept              3.0192      0.162     18.645      0.000       2.702       3.337
C(category)[T.1.0]    -1.8639      0.186    -10.044      0.000      -2.228      -1.500
C(category)[T.2.0]     0.3054      0.205      1.492      0.136      -0.096       0.707
======================================================================================
```
###### Note that we use the default to calculate the stabilized weights, but we could also obtain the unstablilized weights by using stabilized=False
Now that we have our weights, we can fit a IPMW model using the ipw_fit() function. This function uses GEE with an independent covariance structure to obtain the point estimate and the corresponding confidence intervals. This function is used to fit both IPMW and IPTW models
```python
df['id'] = df.index
ipmmodel = ze.ipw.ipw_fit(df,model='outcome ~ exposure + C(category) + binary + continuous + cont_sq',match='id',weight='ipmw_weight')
print(ipmmodel.summary())
```
Which produces the following output
```
                               GEE Regression Results                              
===================================================================================
Dep. Variable:                     outcome   No. Observations:                 3161
Model:                                 GEE   No. clusters:                     3161
Method:                        Generalized   Min. cluster size:                   1
                      Estimating Equations   Max. cluster size:                   1
Family:                           Binomial   Mean cluster size:                 1.0
Dependence structure:         Independence   Num. iterations:                     6
Date:                     Mon, 18 Dec 2017   Scale:                           1.000
Covariance type:                    robust   Time:                         08:23:23
======================================================================================
                         coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------------
Intercept             -0.4643      0.145     -3.198      0.001      -0.749      -0.180
C(category)[T.1.0]    -0.4836      0.125     -3.871      0.000      -0.728      -0.239
C(category)[T.2.0]    -1.2174      0.113    -10.808      0.000      -1.438      -0.997
exposure               0.9300      0.121      7.691      0.000       0.693       1.167
binary                -0.5200      0.102     -5.115      0.000      -0.719      -0.321
continuous            -0.0105      0.006     -1.810      0.070      -0.022       0.001
cont_sq                0.0002    5.6e-05      3.333      0.001    7.68e-05       0.000
==============================================================================
Skew:                          0.9645   Kurtosis:                      -0.6150
Centered skew:                 0.0000   Centered kurtosis:             -3.0000
==============================================================================
```

### Inverse Probability of Treatment Weights
To create an IPTW model, we use the following code to generate both the probabilities and the stabilized weights
```python
df['exp_prob'],df['iptw_weight'] = ze.ipw.iptw(df,'exposure','continuous + binary + C(category)')
```
Which produces the following output
```
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:               exposure   No. Observations:                 3427
Model:                            GLM   Df Residuals:                     3422
Model Family:                Binomial   Df Model:                            4
Link Function:                  logit   Scale:                             1.0
Method:                          IRLS   Log-Likelihood:                -1045.8
Date:                Mon, 18 Dec 2017   Deviance:                       2091.6
Time:                        08:27:23   Pearson chi2:                 2.69e+03
No. Iterations:                     7                                         
======================================================================================
                         coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------------
Intercept             -3.0628      0.215    -14.245      0.000      -3.484      -2.641
C(category)[T.1.0]     1.4697      0.228      6.449      0.000       1.023       1.916
C(category)[T.2.0]     3.5098      0.201     17.488      0.000       3.116       3.903
continuous             0.0073      0.002      3.858      0.000       0.004       0.011
binary                -4.6120      0.235    -19.595      0.000      -5.073      -4.151
======================================================================================
```
###### Note we can again request unstabilized weights if we set stabilized=False
#### Diagnostics
Now that we have weights, we can run some diagnostics on the IPTW model
##### Positivity
```python
ze.ipw.diagnostic.positivity(df,'iptw_weight')
```
Which produces the following output
```
----------------------------------------------------------------------
IPW Diagnostic for positivity
NOTE: This method is only valid for stabilized IPTW weights

If the mean of the weights is far from either the min or max, this may
 indicate the model is mispecified or positivity is violated
Standard deviation can help in IPTW model selection
----------------------------------------------------------------------
Mean Stabilized weight:		 0.947
Standard Deviation:		 0.942
Minimum weight:			 0.328
Maximum weight:			 12.997
----------------------------------------------------------------------
```
We can see that we may have some issues since our Maximum is quite far from the mean stabilized weight. However, we will ignore this issue in our example
##### Standarized Differences
Standardized differences can be calculated for both binary and continuous variables. To calculate, we use the following code
**Binary**:
```python
ze.ipw.diagnostic.standardized_diff(df,'exposure','binary','iptw_weight')
```
Output:
```
	Binary variable: binary
----------------------------------------------------------------------
Weighted SMD: 	 -32.711
----------------------------------------------------------------------
```
**Continuous**:
```python
ze.ipw.diagnostic.standardized_diff(df,'exposure','continuous','iptw_weight',var_type='continuous')
```
Output:
```
	Continuous variable: continuous
----------------------------------------------------------------------
Weighted SMD: 	 14.318
----------------------------------------------------------------------
```
Again, we see issues with our IPTW model. We will ignore these issues through our example
##### Graphical Assessments
We can generate two different graphical figures to assess how well the IPTW model is fitting. We can generate a histogram of the weights, stratified by treatment
```python
ze.ipw.diagnostic.p_hist(df,'exposure','exp_prob')
```
![alt text](https://github.com/pzivich/zepid/blob/master/images/hist_iptw.png "IPTW Histogram")

Alternatively, we can generate a boxplot stratified by the treatment
```python
ze.ipw.diagnostic.p_boxplot(df,'exposure','exp_prob')
```
![alt text](https://github.com/pzivich/zepid/blob/master/images/box_iptw.png "IPTW Boxplot")

From our graphics, we can see that there are issues with our model. We will ignore these for the purpose of our example. In an actual analysis, we would consider different options or coding schemes
#### Fitting an IPTW Model 
We can use the same ipw_fit() function described in the IPMW section to fit a IPTW model
```python
iptmodel = ze.ipw.ipw_fit(df,'outcome ~ exposure','id','iptw_weight')
print(iptmodel.summary())
```
Which outputs
```
                               GEE Regression Results                              
===================================================================================
Dep. Variable:                     outcome   No. Observations:                 3161
Model:                                 GEE   No. clusters:                     3161
Method:                        Generalized   Min. cluster size:                   1
                      Estimating Equations   Max. cluster size:                   1
Family:                           Binomial   Mean cluster size:                 1.0
Dependence structure:         Independence   Num. iterations:                     5
Date:                     Mon, 18 Dec 2017   Scale:                           1.000
Covariance type:                    robust   Time:                         09:39:27
==============================================================================
                 coef    std err          z      P>|z|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     -1.2998      0.056    -23.122      0.000      -1.410      -1.190
exposure       0.7922      0.165      4.801      0.000       0.469       1.116
==============================================================================
Skew:                          1.0508   Kurtosis:                      -0.7536
Centered skew:                 0.0000   Centered kurtosis:             -3.0000
==============================================================================
```
*Note*: Due to the model fitting issues, these results are NOT valid estimates
## Sensitivity Analyses
Now that we have completed our main analysis, we can conduct some sensitivity analyses
### E-values
E-values are a recently proposed item to assess the amount of bias required to shift the estimate to a null value (or some other value). For more information regarding e-values, we direct readers to Vanderweele & Ding 2017
We will calculate the e-value for our crude Odds Ratio from previous
```python
ze.sens_analysis.e_value(effect_measure=1.95,lcl=1.64,ucl=2.32,measure='OR')
```
Which returns
```
WARNING: if the outcome is common, OR/HR need to use the approximation method
for the E-value. The approximation method is implemented by default. If the
outcome is relatively rare (<15%) then the approximation is not required
----------------------------------------------------------------------
Effect Measure: OR	(Reference = 1)

E-values
	Point Estimate = 	2.14
	Confidence Limit = 	1.88
----------------------------------------------------------------------
```
Since our outcome is considered common in our data, we use the approximation method (default for OR in the calculation)
### Delta-Beta Analysis
Now we can use a delta-beta analysis to determine if any single observation was disproportionately driving the observed association. This functions fits a regression model dropping each observation at a time. This means the function may take awhile when large data sets are used, since it fits *n* regression models, where *n* is the number of observations in the data set.
To use this function and store the results, we use the following function. Since are only measure of interest is the exposure, we will only keep track of the changes in beta of this variable
```python
df['delta_b'] = ze.sens_analysis.delta_beta(df,model='outcome ~ exposure + C(category) + binary + continuous + cont_sq',beta=['exposure'])
```
###### Note: This may take a minute or two to run since it fits over 3000 glm models
We can now make a histogram of the delta-beta results to see if there was any outliers driving our association
```python
plt.hist(df.delta_b)
plt.show()
```
![alt text](https://github.com/pzivich/zepid/blob/master/images/hist_deltabeta.png "Delta-Beta Histogram")

From this, we can see there is not any single observation really driving the observed association. As a result, we have some reassurance that our estimate is not due to the covariate structure of a single observation
## Summary image for our effect measures
Now to summary our results (and our results from a normal GLM model not shown here), we will use a specific effect measure plot. This plot produces something similar to a forest plot, but does not provide a summary measure. 
First, we need to prepare our data. We create four lists containing the labels we want, the point estimates, the lower CI, and the upper CI. We convert these lists to a compatible object for our plotting function using the effectmeasure_plot_data() function
```python
labs = ['Crude','Logit','IPTW','IPMW']
resu = [1.95,2.45,1.12,2.53]
rlcl = [1.64,1.93,0.76,'2.00']
rucl = [2.32,'3.10',1.66,3.21]
pf = ze.graphics.effectmeasure_plotdata(labs,resu,rlcl,rucl)
```
Now that our data is all prepared for our plot, we generate our plot using the following code
```python
ze.graphics.effectmeasure_plot(pf,decimal=3,title='Odds Ratio Plot of Results',em='OR',ci='95% CI',scale='log',t_adjuster=0.09,size=3)
```
Producing the following plot

![alt text](https://github.com/pzivich/zepid/blob/master/images/result_plot.png "Effect Measure Summary Plot")

As we can see, our IPTW results are far off. We noticed there were issues in our IPTW diagnostics so we would either create a better IPTW model or not report these results. 

This completes the general walkthrough. In this example, we did not discuss any of the sensitivity or specificity analysis tools. Those will be discussed in a upcoming walkthrough
