Title: Mixed effects modeling in R
Date: 2017-03-11
Category: Statistics
Tags: Statistics, code
Slug: mixed-effects
Authors: Kevin Potter

Hierarchical generalized linear models provide an extremely powerful set of tools for statistical analysis. Here I provide a very basic example of how to fit these models using the lme4 package in R. Numerous tutorials already exist on this topic, so the other purpose of this post is to expand my understanding of these models by re-fitting them to simulated data. One's understanding of a statistical model is greatly improved when you are able to determine how to go about simulating data and testing parameter recovery for the model.

For this example, I will focus on a very basic example, a linear model in which the i<sup>th</sup> observation follows a normal distribution.

First, we need to install and load the package.
```r
# install.packages( 'lme4' )
library( lme4 )
```

Next, we'll define the structure for the data to be simulated. We will focus on the design for a simple two-factor repeated measures ANOVA. In this design, every subject provides multiple observations for each level of each factor. In other words, this is a completely within-subjects design.
```r
Ns = 100 # Number of subjects
No = 8 # Number of observations per subject

# The standard ANOVA uses effects coding
A = rep( c( -1, 1 ), each = No/2 ) # Factor A
B = rep( c( -1, 1 ), No/2 ) # Factor B
AxB = A * B # Interaction

# Expand out based on subject number
A = rep( A, Ns )
B = rep( B, Ns )
AxB = rep( AxB, Ns )

# Design matrix
X = cbind( 1, A, B, AxB )

# Subject index
subjIndex = rep( 1:Ns, each = No )
```

Next, let us define a set of generating parameters. With hierarchical linear modeling, a repeated measures ANOVA is similar to a model with a random intercept for subjects and a set of fixed effects capturing the main effects and interactions:
```r
gp = list(
  beta = rbind( 1, .2, -.3, .2 ), # Fixed effects
  sigma_eta = 0.7, # Standard deviation for random intercept for subjects
  sigma_epsilon = 2 # Standard deviation for residual variability
)
```

We are finally ready to simulate a set of responses:
```r
# Subject effects
set.seed( 10 ) # For reproducibility
eta = rnorm( Ns, 0, gp$sigma_eta )

# Define population mean for each observation
mu = X %*% gp$beta + eta[ subjIndex ]

# Simulate data
set.seed( 20 ) # For reproducibility
Y = rnorm( Ns*No, mu, gp$sigma_epsilon )

# Create data frame
df = cbind( Y = Y, A = A, B = B, AxB = AxB, S = subjIndex )
df = as.data.frame( df )
```

We can now carry out parameter recovery to see if I've correctly specified the structure of a mixed effects model with a random intercept for subjects and a set of fixed effects representing the main effects and interaction between two factors, A and B:
```r
fit = lmer( Y ~ 1 + A + B + AxB + # Fixed effects (Intercept, main effect of A and B, 
            (1|S), # Random intercept per subject
			data = df )
```

We determine extract confidence intervals for the parameters:
```r
# Standard 95% confidence intervals
ui = confint( fit )

# print( round( ui, 2 ) )
#              2.5 % 97.5 %
# .sig01       0.37   0.81
# .sigma       1.97   2.18
# (Intercept)  0.70   1.07
# A            0.00   0.29
# B           -0.51  -0.23
# AxB          0.13   0.42
```
As can be seen, the estimates do a good job capturing the original generating parameters.

We can also use a semi-parametric bootstrap method (more robust but less powerful) to calculate confidence intervals:
```r
# Define function to extract test statistics of interest from 'lmer' fit object
f = function( fit ) {
  out = c( 
    # Extracting the standard deviation estimate for random effects can be complicated
    sig01 = sqrt( VarCorr(fit)$S[1] ),
    sigma = sigma(fit),
    # Extracting the fixed effects is much easier
    fixef( fit )
  )
  return( out )
}
R = 1000 # Number of bootstrap samples
sim = bootMer( fit, f, nsim = R )
ui_boot = t( apply( sim$t, 2, quantile, prob = c( .025, .975 ) ) )

# print( round( ui_boot, 2 ) )
#              2.5% 97.5%
# sig01        0.34  0.79
# sigma        1.96  2.18
# (Intercept)  0.70  1.07
# A           -0.01  0.29
# B           -0.50 -0.22
# AxB          0.13  0.42
```
