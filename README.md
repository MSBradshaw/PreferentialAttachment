# PreferentialAttachment


The purpose of this repo was to explore power-law distributions in protein-protein-interaction (PPI) networks. Here I check if two PPI have PL, [STRING](https://string-db.org/) and [HuRI](http://www.interactome-atlas.org/). STRING is an agglomeration of many databased, studies and data types and contains an ennormous number of edges ~15 million. HuRI on the other hand is the results of a single massive all-by-all yeast 2 hybrid set of experiments where 10 thousand proteins were all equally used as bait and prey. I expected String to have a PL and HuRI to not, turns out they both do. But the hub nodes (very high degree nodes) in the two networks are different, in STRING they are things like Cancer genes and those related to well understood processes like ATP. In HuRI these are no longer the top connected nodes, top nodes in HuRI do not fall into an easily definable category or group.


## String
<p align="center"><img src="https://github.com/MSBradshaw/PreferentialAttachment/blob/main/work/Plots/string.all.degree_dists.png?raw=true" width="80%"/></p>

## HuRI
<p align="center"><img src="https://github.com/MSBradshaw/PreferentialAttachment/blob/main/work/Plots/HuRI.degree_dists.png?raw=true" width="80%"/></p>
