set terminal epslatex standalone color size 4.0in,3.0in background rgb "white"
set output "fig-1-heating.tex"
set xlabel "$\\tau = 2\\pi/\\omega$"
set label "$e$" rotate by 0 at graph 0 offset char -6, graph 0.5
set yrange [-1.1:0]
set xrange [:14]
set ytics 0.5
set mytics 5
set key Left reverse at graph 0.5, 0.3
set rmargin 1.0
set lmargin 7.0

plot "../closed-system/500-cycles.dat" u ($1/500):3 w l lw 2 dt 2 lc 1 title "",\
"../closed-system/1000-cycles.dat" u ($1/1000):3 w l lw 2 dt 2 lc 2 title "",\
"../closed-system/1500-cycles.dat" u ($1/1500):3 w l lw 2 dt 2 lc 3 title "",\
"../closed-system/2000-cycles.dat" u ($1/2000):3 w l lw 2 dt 2 lc 4 title "",\
"../open-system/2000-cycles.dat" u ($1/2000):3 w l lw 2 dt 1 lc 4 title "$t=2000\\tau$",\
"../open-system/1500-cycles.dat" u ($1/1500):3 w l lw 2 dt 1 lc 3 title "$t=1500\\tau$",\
"../open-system/1000-cycles.dat" u ($1/1000):3 w l lw 2 dt 1 lc 2 title "$t=1000\\tau$",\
"../open-system/500-cycles.dat" u ($1/500):3 w l lw 2 dt 1 lc 1 title "$t=500\\tau$",\
