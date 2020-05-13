####################################################################
# Demonstration of AIPW with a single sample
#   Data generating mechanism comes from Funk et al. AJE (2011). See
#   online supplementary information for details (or the dgm.py file)
#
# Paul Zivich
####################################################################

# Loading the data
dat <- read.csv("dr_data.csv")
summary(dat)

# Estimating Propensity Scores (IPW)
propensity_model <- glm(X ~ Z1 + Z3, data=dat, family='binomial')
summary(propensity_model)

odds <- exp(predict(propensity_model, dat))
ps = odds / (1 + odds)

# Estimating Outcome Model (g-formula)
outcome_model <- lm(Y ~ X + Z1 + Z3, data=dat)
summary(outcome_model)

datx <- data.frame(dat)
datx$X <- 1
y_x1 <- predict(outcome_model, datx)
datx$X <- 0
y_x0 <- predict(outcome_model, datx)

# Generating Pseudo-Outcomes
y_obs <- dat$Y
x_obs <- dat$X

y_x1_star <- (y_obs*x_obs)/ps + (y_x1*(ps-x_obs))/ps
y_x0_star <- (y_obs*(1-x_obs))/(1-ps) + (y_x0*(x_obs-ps))/(1-ps)

# AIPW Estimates
pseudo_y <- y_x1_star - y_x0_star
ate <- mean(pseudo_y)  # Point estimate
var_ate <- var(pseudo_y - ate) / nrow(dat)  # Variance
ci_ate <- c(ate - 1.96*sqrt(var_ate),  # Confidence interval
            ate + 1.96*sqrt(var_ate))

ate
ci_ate

# G-computation
mean(y_x1 - y_x0)

# IPW
mean((y_obs*x_obs)/ps - (y_obs*(1-x_obs))/(1-ps))
