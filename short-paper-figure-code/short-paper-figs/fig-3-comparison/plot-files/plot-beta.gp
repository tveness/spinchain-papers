set terminal epslatex standalone color size 4.0in,3.0in background rgb "white"
set output "beta-comp.tex"

set xlabel "$\\tau$"
set ylabel "$e$"
set key bottom left Left reverse


#"/home/tom/nott/spin_chain/sc/hpc/circular_l_20_L_4000/avg1000.dat" u 1:($3) w p title "Dynamical results for 1000 cycles, $\\ell=20$, $L=4000$",\


set xrange [.1:14]
#set log x
set multiplot
set size 1.0,1.0
set origin 0.0,0.0

plot "../sc/8k-long-run-dj-0.01/1000-cycles.dat" u ($1/1000):3 w lp title "Dynamics",\
"../hpc-2/1000-cycles.dat" u ($1/1000):3 w lp title "Dynamics old",\
"../hpc-2/betat-e-bare.dat" u 1:4 w l title "Rotating frame ensemble",\
"betat-high-freq.dat" u 1:($4+$5+$7*$1/(4*pi)) smooth bezier title "Magnus ensemble"

#plot "../hpc-2/1000-cycles.dat" u ($1/1000):3 w lp title "Dynamics",\

set size 0.6,0.6
set origin 0.4,0.4

set log x
set xlabel ""
set ylabel ""
plot "../hpc-2/1000-cycles.dat" u ($1/1000):3 w lp title "",\
"../hpc-2/betat-e-bare.dat" u 1:4 w l title "",\
"betat-high-freq.dat" u 1:($4+$5+$7*$1/(4*pi)) smooth bezier title ""

