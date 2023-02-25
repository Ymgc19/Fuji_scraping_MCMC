library(tidyverse)
library(rstan)

fit <- stan(file="Fuji.stan",
            data=standata, 
            iter=5000,
            warmup=1000,
            thin=1,
            chains=4,
            seed=8931)

#先手&七段以下　q0
#先手&八段以上　q1
#後手&七段以下　q2
#後手&八段以上　q3
print(fit)
#stan_trace(fit)

stan_plot(fit,point_est = "mean",ci_level = 0.95,outer_level = 1.00,
          show_density = T,fill_color = "pink") + theme_bw() +
  theme(legend.text=element_text(size=6),
        legend.title=element_text(size=8,face="bold"),  
        axis.text.x=element_text(size=6),
        axis.text.y=element_text(size=8,face="bold"),
        axis.title=element_text(size=8,face="bold"),
        strip.text.x = element_text(size=6,face="bold"),
        legend.position = "right") +
  theme(axis.title.x = element_blank(), axis.title.y = element_blank())
ggsave("..Fujii_first_stan.pdf",width=10,height=6,unit="cm")

