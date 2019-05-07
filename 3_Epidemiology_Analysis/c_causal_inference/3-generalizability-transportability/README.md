This section details generalizability and transportability

# Generalizability
Generalizability is the concept that our study sample is not a random sample from the population we want to make inferences about (target population). The concept of generalizability is often referred to as external validity. Generalizability estimators can be applied to both randomized trials and observational data. The randomized trial scenario is simpler, since we do not need to contend with confounding. However, generalizability does require us to make comparable assumptions *even for randomized trial data*. 

For demonstration, consider our simulated trial data to assess the effect of A on Y. While our trial results are internally valid (correct estimation for our study sample), we are concerned that they are no longer reflective of our target population. Specifically, we are concerned that the individuals who enrolled in our trial are not a random sample of our target population. For generalizability, we make the following assumptions

## Exchangeability
For generalizability, the exchangeability assumption refers to that the study sample is exchangeable with the target population. This is met when the study sample is a random sample of the target population. For the generalizability estimators, we will assume there is some set of variables under which conditional exchangeability between the study sample and the target population is met. 

The key feature of this assumption, is that it is not necessarily met for randomized trials. It is only met in expectation for randomized trials, in which the trial participants are a random sample of the target population. Often this is not true. Therefore, randomized trials need to make an (unverifiable) exchangeability assumption for generalizability. As a consequence, the following assumption is necessary.

## Positivity
All individuals in the target population by the set of variables for exchangeability have some non-zero probability of being part of the study sample.

## Treatment Variation Irrelevance
Lastly, we assume that the treatment mechanism or any of its variations are unimportant for the causal effect in the target population. 

# Transportability
Transportability is a related concept. Rather than our study sample not being a random sample from our target population, our study sample is not part of our target population. As an example, our study on the effect of drug X on death may have been conducted in the United States, but we want to estimate the effect of drug X on death in Canada. Since our study sample is not part of the target population, some authors draw a distinction between the two problems.

The key difference is what the estimators are marginalizing over. Under generalizability, the estimators marginalize over both the study sample and the target population sample. For transportability, the estimators marginalize over the target population sample only. Transportability makes comparable identifiability assumptions to generalizability.