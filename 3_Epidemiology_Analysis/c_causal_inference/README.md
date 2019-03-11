Throughout the following tutorials in this branch, we will make the following identifiability assumptions. 
We additionally will assume no measurement error, no selection bias, and no interference.

# Assumptions

## Conditional Exchangeability
Conditional exchangeability is the assumption that potential outcomes are independent of the treatment received 
conditional on some set of covariates. Using causal diagrams, this amounts to no open backdoor paths between the 
treatment and outcome. See the further reading list for publications on the assumption of conditional exchangeability
and introductions to two different approaches to causal diagrams (directed acyclic graphs (DAG) and single-world 
intervention graphs (SWIG))

### Further Reading
Hernán MA, Robins JM. (2006). Estimating causal effects from epidemiological data. *Journal of Epidemiology 
& Community Health*, 60(7), 578-586.

Greenland S, Pearl J, Robins JM. (1999). Causal diagrams for epidemiologic research. *Epidemiology*, 10, 37-48.

Richardson TS, Robins JM. (2013). Single world intervention graphs: a primer. *In Second UAI workshop on 
causal structure learning*, Bellevue, Washington.

Breskin A, Cole SR, Hudgens MG. (2018). A practical example demonstrating the utility of single-world 
intervention graphs. *Epidemiology*, 29(3), e20-e21.

## Positivity
The positivity assumption is that there are treated and untreated individuals at every combination of covariates. There
are two potential positivity violations; deterministic or random. Deterministic positivity violations can never occur
despite additional data collection. For an example of a deterministic positivity violation, consider the risk of death 
by hysterectomy. Since men lack a uterus, they are unable to receive a hysterectomy. Random positivity violations 
occur as a result of finite samples. In a small sample, it may just occur that we didn't observe anyone treated between
ages 32-35. It isn't that no one could have been treated in that age group, we just didn't observe it in our sample. 
For these scenarios, we will assume that our statistical model correctly interpolates over these areas (often a 
strong assumption in small data sets)

### Further Reading
Westreich D, Cole SR. (2010). Invited commentary: positivity in practice. *American Journal of Epidemiology*, 
171(6), 674-677.

Cole SR, Hernán MA. (2008). Constructing inverse probability weights for marginal structural models. 
*American Journal of Epidemiology*, 168(6), 656-664.

## Causal Consistency
Causal consistency is also referred to as treatment variation irrelevance. Under this assumption we assume that there 
is only one version of treatment (consistency) or that any differences remaining between treatments is irrelevant
(treatment variation irrelevance). For example, consider a study on 200mg daily aspirin and all-cause mortality. In our
study, we may be willing to assume that taking aspirin in the morning versus at night is irrelevant to all-cause 
mortality. This is an example of assuming treatment variation irrelevance. Generally, defining the treatment more
precisely can get you out of this as an issue. There are also some additional approaches. I recommend reviewing the 
below readings for further discussions

### Further Reading
Cole SR, Frangakis CE. (2009). The consistency statement in causal inference: a definition or an assumption?. 
*Epidemiology*, 20(1), 3-5.

VanderWeele TJ. (2009). Concerning the consistency assumption in causal inference. *Epidemiology*, 20(6), 880-883.

VanderWeele TJ. (2018). On well-defined hypothetical interventions in the potential outcomes framework. 
*Epidemiology*, 29(4), e24-e25.

## Correctly specified model
Since we will be working with continuous and high-dimensional data, we will be using parametric regression models. 
We assume that these models are correctly specified. To make less restrictive assumptions regarding the functional
forms of continuous variables, we will use splines throughout. Please refer to the Data Basics for an intro to 
using splines with *zEpid*

Additionally, we will sometime uses machine learning approaches to relax this assumption further (see TMLE tutorials
for some examples)
