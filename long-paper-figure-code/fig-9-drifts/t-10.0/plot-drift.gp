set terminal epslatex standalone color size 4.0in,3.0in background rgb "white"
set output "fig-9-drift-tau-10.0.tex"

set xlabel "$\\mathfrak{e}$"
set ylabel "$e$"
set title "$\\tau = 10$"
y1000 = -.634288
y2000 = -0.6189
y5000 = -0.587564
y10000 = -0.552031

base=-.60

h1000=-1.00148
h2000=-0.949021
h5000=-0.894463
h10000=-0.862987
set xrange [-.66:-.51]
set yrange [-1.1:-0.2]

set label "$1000$" at y1000-0.0075, base+0.02
set arrow from y1000,base to y1000,h1000

set label "$2000$" at y2000-0.0075, base-0.04
set arrow from y2000,base-.06 to y2000,h2000

set label "$5000$" at y5000-0.0075, base+0.02
set arrow from y5000,base to y5000,h5000

set label "$10000$" at y10000-0.0075, base+0.02
set arrow from y10000,base to y10000,h10000

plot "avg.dat" u 2:3 w d title "Dynamics",\
"betat-rot.dat" u 2:4 w lp lw 2 title "Ensemble"

