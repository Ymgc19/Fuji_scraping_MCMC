
data {
  int N;
  int X[N];
  int Z[N];
  int Y[N];
}

parameters {
  real<lower=0,upper=1> q0;
  real<lower=0,upper=1> q1;
  real<lower=0,upper=1> q2;
  real<lower=0,upper=1> q3;
}

model {
  for (n in 1:N) {
    X[n] ~ bernoulli( (Z[n]*q0+(1-Z[n])*q2)*Y[n] + (Z[n]*q1+(1-Z[n])*q3)*(1-Y[n]) );
  }
}


