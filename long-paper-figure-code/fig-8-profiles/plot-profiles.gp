set terminal epslatex standalone color size 4.0in,3.0in background rgb "white"

set output "fig-8-sjs-profile.tex"
set key width -2
set key Left left top 

set xrange [-500:500]
set xlabel "$j$"
set ylabel "$e_0(j)$"

set style arrow 1 nohead ls 0
set for [i=0:1] arrow from (40*i), graph 0 to (40*i), graph 1 as 1

plot "mc_profile.dat" u 1:2 w l dt 3 title "$\\mathcal{P}_\\mathrm{rot}$", "mc_profile.dat" u ($1-1000):2 w l dt 3 lc 1 title "",\
"dyn_profile-1000-tau.dat" u 1:2 w l title "$t=1000\\tau$" lc 2,\
"dyn_profile-1000-tau.dat" u ($1-2000):2 w l lc 2 title "",\
"dyn_profile-2000-tau.dat" u 1:2 w l title "$t=2000\\tau$" lc 3,\
"dyn_profile-2000-tau.dat" u ($1-2000):2 w l lc 3 title "",\
"dyn_profile-4000-tau.dat" u 1:2 w l title "$t=4000\\tau$" lc 4,\
"dyn_profile-4000-tau.dat" u ($1-2000):2 w l lc 4 title "",\

set output "fig-8-sx-profile.tex"

set xrange [-500:500]
set xlabel "$j$"
set ylabel "$S^x_j$"
set key default
set key at 0.3,-0.05

set for [i=0:1] arrow from (40*i), graph 0 to (40*i), graph 1 as 1

plot "mc_profile.dat" u 1:3 w l dt 3 title "$\\mathcal{P}_\\mathrm{rot}$", "mc_profile.dat" u ($1-1000):3 w l dt 3 lc 1 title "",\
"dyn_profile-4000-tau.dat" u 1:3 w l title "$t=4000\\tau$" lc 4,\
"dyn_profile-4000-tau.dat" u ($1-2000):3 w l lc 4 title "",\
"dyn_profile-2000-tau.dat" u 1:3 w l title "$t=2000\\tau$" lc 3,\
"dyn_profile-2000-tau.dat" u ($1-2000):3 w l lc 3 title "",\
"dyn_profile-1000-tau.dat" u 1:3 w l title "$t=1000\\tau$" lc 2,\
"dyn_profile-1000-tau.dat" u ($1-2000):3 w l lc 2 title "",\



set output "fig-8-sy-profile.tex"

set xrange [-500:500]
set xlabel "$j$"
set ylabel "$S^y_j$"

set for [i=0:1] arrow from (40*i), graph 0 to (40*i), graph 1 as 1

plot "mc_profile.dat" u 1:4 w l dt 3 title "$\\mathcal{P}_\\mathrm{rot}$", "mc_profile.dat" u ($1-1000):4 w l dt 3 lc 1 title "",\
"dyn_profile-1000-tau.dat" u 1:4 w l title "$t=1000\\tau$" lc 2,\
"dyn_profile-1000-tau.dat" u ($1-2000):4 w l lc 2 title "",\
"dyn_profile-2000-tau.dat" u 1:4 w l title "$t=2000\\tau$" lc 3,\
"dyn_profile-2000-tau.dat" u ($1-2000):4 w l lc 3 title "",\
"dyn_profile-4000-tau.dat" u 1:4 w l title "$t=4000\\tau$" lc 4,\
"dyn_profile-4000-tau.dat" u ($1-2000):4 w l lc 4 title "",\

set output "fig-8-sz-profile.tex"

set xrange [-500:500]
set xlabel "$j$"
set ylabel "$S^z_j$"
set key width -2
set key Left left top 
set key default
set key at -50, 0.38

set for [i=0:1] arrow from (40*i), graph 0 to (40*i), graph 1 as 1

plot "mc_profile.dat" u 1:5 w l dt 3 title "$\\mathcal{P}_\\mathrm{rot}$", "mc_profile.dat" u ($1-1000):5 w l dt 3 lc 1 title "",\
"dyn_profile-4000-tau.dat" u 1:5 w l title "$t=4000\\tau$" lc 4,\
"dyn_profile-4000-tau.dat" u ($1-2000):5 w l lc 4 title "",\
"dyn_profile-2000-tau.dat" u 1:5 w l title "$t=2000\\tau$" lc 3,\
"dyn_profile-2000-tau.dat" u ($1-2000):5 w l lc 3 title "",\
"dyn_profile-1000-tau.dat" u 1:5 w l title "$t=1000\\tau$" lc 2,\
"dyn_profile-1000-tau.dat" u ($1-2000):5 w l lc 2 title "",\
