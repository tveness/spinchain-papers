set terminal epslatex standalone color size 4.0in,3.0in background rgb "white"
set output "fig-9-drift-tau-5.0.tex"

set xlabel "$\\mathfrak{e}$"
set ylabel "$e$"
set title "$\\tau = 5$"
y1000 = -.6326
y2000 = -0.61806
y5000 = -0.58952
y10000 = -0.55735

base=-0.8

h1000=-0.61
h2000=-0.55
h5000=-0.5
h10000=-0.47
set xrange [-.66:-.51]
set yrange [-1.1:-0.2]

set label "$1000$" at y1000-0.0075, base-0.04
set arrow from y1000,base to y1000,h1000

set label "$2000$" at y2000-0.0075, base+0.01
set arrow from y2000,base+0.04 to y2000,h2000

set label "$5000$" at y5000-0.0075, base-0.04
set arrow from y5000,base to y5000,h5000

set label "$10000$" at y10000-0.0075, base-0.04
set arrow from y10000,base to y10000,h10000

plot "avg.dat" u 2:3 w d title "Dynamics",\
"betat-rot.dat" u 2:4 w lp lw 2 title "Ensemble"

