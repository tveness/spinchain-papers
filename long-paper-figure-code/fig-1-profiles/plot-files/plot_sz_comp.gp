set terminal epslatex standalone color size 4.0in,3.0in background rgb "white"

set output "fig-1-profile-comparison.tex"



#set key width -2
#set key Left left top 

set multiplot layout 2,1

set xrange [-500:500]
#set xrange [-100:150]
set key width -1
set key Left left top 
#set key default
#set key at 0.0, 0.38

#set style arrow 1 nohead ls 0
#set for [i=0:1] arrow from (40*i), graph 0 to (40*i), graph 1 as 1
x1=0
x2=40
y1=-0.07
y2=0.25
#set style rect fill solid 0.25 noborder 
set style rect fc lt -1 fs solid 0.15 noborder
set object 1 rect from x1,y1 to x2,y2 
unset xlabel
set tmargin 3.3
set bmargin 0
set format x ''
set lmargin 6.5
#set yrange [-0.029:0.05]
set yrange [y1:y2]
#set label "$\\tau=0.5$" at 200,0.9
set label "$\\tau=0.5$" at 200,0.7
#set ylabel "$S^z_j$"
set label "$S_j^z$" rotate by 90 at graph 0 offset char -5, graph 0.5

plot "../profile-mc-fast/mc_profile.dat" u 1:(-$5) w l dt 3 lc 1 lw 2 title "Ensemble",\
"../profile-mc-fast/mc_profile.dat" u ($1-2000):(-$5) w l lc 1 lw 2 dt 3 title "",\
"../dyn-big-fast/dyn_profile-1000-tau.dat" u 1:5 w l lc 2 lw 2 title "$t=1000\\tau$",\
"../dyn-big-fast/dyn_profile-1000-tau.dat" u ($1-2000):5 w l lc 2 lw 2 title "",\
"../dyn-big-fast/dyn_profile-2000-tau.dat" u 1:5 w l lc 3 lw 2 title "$t=2000\\tau$",\
"../dyn-big-fast/dyn_profile-2000-tau.dat" u ($1-2000):5 w l lc 3 lw 2 title "",\
"../dyn-big-fast/dyn_profile-4000-tau.dat" u 1:5 w l lc 4 lw 2 title "$t=4000\\tau$",\
"../dyn-big-fast/dyn_profile-4000-tau.dat" u ($1-2000):5 w l lc 4 lw 2 title "",\

unset format x
set lmargin 6.5
set tmargin 0
set bmargin 3.3
set yrange [0:0.44]
set ytics 0.1
unset key
y1=0
y2=0.44
set object 1 rect from x1,y1 to x2,y2 
#set ylabel "$S^z_j$"
set xlabel "$j$"
set label "$\\tau=10$" at 200,0.3

#set for [i=0:1] arrow from (40*i), graph 0 to (40*i), graph 1 as 1

plot "../dyn-big-slow/dyn_profile-4000-tau.dat" u 1:5 w l lc 4 lw 2 title "$t=4000\\tau$",\
"../dyn-big-slow/dyn_profile-4000-tau.dat" u ($1-2000):5 w l lc 4 lw 2 title "",\
"../dyn-big-slow/dyn_profile-2000-tau.dat" u 1:5 w l lc 3 lw 2 title "$t=2000\\tau$",\
"../dyn-big-slow/dyn_profile-2000-tau.dat" u ($1-2000):5 w l lc 3 lw 2 title "",\
"../dyn-big-slow/dyn_profile-1000-tau.dat" u 1:5 w l lc 2 lw 2 title "$t=1000\\tau$",\
"../dyn-big-slow/dyn_profile-1000-tau.dat" u ($1-2000):5 w l lc 2 lw 2 title "",\
"../profile-mc-slow/mc_profile.dat" u 1:5 w l lc 1 lw 2 dt 3 title "Equilbrium ensemble $\\mathcal{P}_\\mathrm{rot}$", "../profile-mc-slow/mc_profile.dat" u ($1-1000):5 w l lw 2 dt 3 lc 1 title "",\
