set terminal epslatex standalone color size 8.0in,6.0in background rgb "white"
set output "fig.tex"


sumh = "`wc -l ../control-mc/mc_live.dat`"
sumdh = "`wc -l ../hf-dyn/dyn.dat`"
sumc = "`wc -l ../hf-mc/mc_live.dat`"

binwidth = 0.06
sumh = sumh*binwidth
sumc = sumc*binwidth
sumdh = sumdh*binwidth
set boxwidth binwidth



bin(x,width)=width*(floor(x/width) + 0.5)
set multiplot layout 2,3 margins 0.1,0.95,0.09,0.98 spacing 0.05,0.09



tau = 0.5
omega=2.0*pi/tau
c=cos(1.0/omega)
s=sin(1.0/omega)

# e low freq
set key Left reverse
set xrange [-1.8:0.2]
set yrange [0:2.5]
set xtics .4
set xlabel "$e$"
set ylabel "$P$"
#set style fill solid 0.06 noborder 
set style fill solid 0.25 noborder 

plot "../control-mc/mc_live.dat" u (bin($2+$3,binwidth)):(1.0/sumc) smooth freq w boxes lc 0 title "Monte Carlo $P_{0}$",\
"../hf-mc/mc_live.dat" u (bin($2+$3,binwidth)):(1.0/sumh) smooth freq w histeps lw 2 lc 1 title "Monte Carlo $P_{F}$",\
"../hf-dyn/dyn.dat" u (bin($3,binwidth)):(1.0/sumdh) smooth freq w lp lw 2 lc 2 title "Dynamics $\\tau=0.5$"

unset key
unset yrange
set xrange [-1:1]
set xtics auto
set xlabel "$m_z$"
unset ylabel 

plot "../control-mc/mc_live.dat" u (bin($5*c+$3*s,binwidth)):(1.0/sumc) smooth freq w boxes lc 0 title "Monte Carlo $P_{0}$",\
"../hf-mc/mc_live.dat" u (bin(($5*c+$3*s),binwidth)):(1.0/sumh) smooth freq w histeps lw 2 lc 1 title "Monte Carlo",\
"../hf-dyn/dyn.dat" u (bin($6,binwidth)):(1.0/sumdh) smooth freq w lp lw 2 lc 2 title "Dynamics"


unset key
set xrange [-1:1]
set xlabel "$S^z_{\\ell/4}$"
plot "../control-mc/mc_live.dat" u (bin(($8*c+$6*s),binwidth)):(1.0/sumc) smooth freq w boxes lc 0 title "Monte Carlo $P_{0}$",\
"../hf-mc/mc_live.dat" u (bin(($8*c+$6*s),binwidth)):(1.0/sumh) smooth freq w histeps lw 2 lc 1 title "Monte Carlo",\
"../hf-dyn/dyn.dat" u (bin($10,binwidth)):(1.0/sumdh) smooth freq w lp lw 2 lc 2 title "Dynamics",\



tau = 10
omega=2*pi/tau
# e low freq
binwidth = 0.05
set boxwidth binwidth

suml = "`wc -l ../lf-mc/mc_live.dat`"
sumdl = "`wc -l ../lf-dyn/dyn-samples.dat`"
sumdl = sumdl*binwidth
suml = suml*binwidth

set key Left reverse
set xrange [-1.8:0.2]
set yrange [0:3.5]
set xtics .4
set xlabel "$e$"
set ylabel "$P$"
plot "../control-mc/mc_live.dat" u (bin($2+omega*$5,binwidth)):(1.0/sumc) smooth freq w boxes lc 0 title "Monte Carlo $P_{0}$",\
"../lf-mc/mc_live.dat" u (bin($2+omega*$5,binwidth)):(1.0/suml) smooth freq w histeps lw 2 lc 1 title "Monte Carlo $P_{RF}$",\
"../lf-dyn/dyn-samples.dat" u (bin($3,binwidth)):(1.0/sumdl) smooth freq w lp lw 2 lc 2 title "Dynamics $\\tau=10$ "

unset key 
set xtics auto
set xrange [-1:1]
set yrange [0:5]
#unset yrange
set xlabel "$m_x$"
unset ylabel 

plot "../control-mc/mc_live.dat" u (bin($3,binwidth)):(1.0/sumc) smooth freq w boxes lc 0 title "Monte Carlo $P_{0}$",\
"../lf-mc/mc_live.dat" u (bin($3,binwidth)):(1.0/suml) smooth freq w histeps lw 2 lc 1 title "Monte Carlo",\
"../lf-dyn/dyn-samples.dat" u (bin($4,binwidth)):(1.0/sumdl) smooth freq w lp lw 2 lc 2 title "Dynamics"


unset key
set xrange [-1:1]
unset yrange
set xlabel "$S^x_{\\ell/4} S^x_{3\\ell/4}$"
plot "../control-mc/mc_live.dat" u (bin($6*$9,binwidth)):(1.0/sumc) smooth freq w boxes lc 0 title "Monte Carlo $P_{0}$",\
"../lf-mc/mc_live.dat" u (bin($6*$9,binwidth)):(1.0/suml) smooth freq w histeps lw 2 lc 1 title "Monte Carlo",\
"../lf-dyn/dyn-samples.dat" u (bin($8*$11,binwidth)):(1.0/sumdl) smooth freq w lp lw 2 lc 2 title "Dynamics"


