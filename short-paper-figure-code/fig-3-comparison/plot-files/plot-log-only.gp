set terminal epslatex standalone color size 4.0in,3.0in background rgb "white"
set output "beta-comp.tex"

set xlabel "$\\tau$"
set ylabel "$e$"
set key bottom left Left reverse

set xrange [.1:14]
set yrange [-1.2:0]
set log x

# Dyn curve: tau vs e
# P_{RF} curve: tau vs e
# P_F curve: tau vs e + mx + mz/(2*omega)

plot "../dyn-curve/1000-cycles.dat" u ($1/1000):3 w lp lw 2 title "Dynamics",\
"../prf-curve/betat-rot.dat" u 1:4 w l lw 2 title "Monte Carlo $P_{RF}$",\
"../pf-curve/betat.dat" u 1:($4+$5+$7*$1/(4*pi)) smooth bezier lw 2 dt 2 title "Monte Carlo $P_{F}$"

