# install the package igraph from CRAN
# install.packages("igraph", repos="http://cran.r-project.org")
# install poweRlaw package from CRAN
# install.packages("poweRlaw", repos="http://cran.r-project.org")
library("igraph")
library("poweRlaw")

dd <- read.table("HuRI/HuRI.tsv", header=FALSE, sep="\t")
# dd <- read.table("work/string.experimental.txt", header=FALSE, sep="\t")
# dd <- read.table("HuRI/string.all.txt", header=FALSE, sep="\t")

gg <- graph.data.frame(dd, directed=FALSE)

ddist = degree(gg)
# print(ddist)
# print(c(ddist))
# ddist

#https://stats.stackexchange.com/questions/108843/how-to-test-whether-a-distribution-follows-a-power-law
data_pl <- displ$new(ddist)
est <- estimate_xmin(data_pl)
data_pl$xmin <- est$xmin
data_pl$pars <- est$pars

print(est$KS)

bs <- bootstrap_p(data_pl, threads=16, seed=42)
print(bs)
