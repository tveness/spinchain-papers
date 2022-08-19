set terminal epslatex standalone color size 8.0in,3.0in background rgb "white"
set output "fig-3-high-frequency-histograms.tex"

binwidth = 0.06

sumh = "`wc -l mc/mc_live.dat`"
sumh = sumh*binwidth

sumhf = "`wc -l mc-full/mc_live.dat`"
sumhf = sumhf*binwidth

sumdh = "`wc -l dyn/dyn.dat`"
sumdh = sumdh*binwidth

sumc = "`wc -l mc-control/mc_live.dat`"
sumc = sumc*binwidth


set boxwidth binwidth


bin(x,width)=width*(floor(x/width) + 0.5)
set multiplot layout 1,3 margins 0.1,0.95,0.18,0.98 spacing 0.05,0.09


print sumh
print sumdh
print sumc

tau = 0.5
omega=2*pi/tau
c=cos(1.0/omega)
s=sin(1.0/omega)
print c,s


# e low freq
unset key
set xrange [-1.8:0.2]
set yrange [0:2.5]
set xtics .4
set xlabel "$e$"
set ylabel "$P$"
#set style fill solid 0.06 noborder 
set style fill solid 0.25 noborder 

plot "mc-control/mc_live.dat" u (bin($2+$3,binwidth)):(1.0/sumc) smooth freq w boxes lc 0 title "$P_F^{(0)}$",\
"mc/mc_live.dat" u (bin($2+$3,binwidth)):(1.0/sumh) smooth freq w histeps lw 2 lc 1 title "$P_{F}^{(1)}$",\
"mc-full/mc_live.dat" u (bin($2+$3,binwidth)):(1.0/sumhf) smooth freq w histeps lw 2 lc 3 title "$P_{F}^{(2)}$",\
"dyn/dyn.dat" u (bin($3,binwidth)):(1.0/sumdh) smooth freq w lp lw 2 lc 2 title "Dynamics $\\tau=0.5$",\

unset key
unset yrange
set xrange [-1:1]
set xtics auto
set xlabel "$m_z$"
unset ylabel 

plot "mc-control/mc_live.dat" u (bin($5*c+$3*s,binwidth)):(1.0/sumc) smooth freq w boxes lc 0 title "$P_F^{(0)}$",\
"mc/mc_live.dat" u (bin(($5*c+$3*s),binwidth)):(1.0/sumh) smooth freq w histeps lw 2 lc 1 title "$P_F^{(1)}$",\
"mc-full/mc_live.dat" u (bin($5,binwidth)):(1.0/sumhf) smooth freq w histeps lw 2 lc 3 title "$P_F^{(2)}$",\
"dyn/dyn.dat" u (bin($6,binwidth)):(1.0/sumdh) smooth freq w lp lw 2 lc 2 title "Dynamics",\


set key top left Left reverse spacing 1.5
set yrange [0:1.2]
set xrange [-1:1]
set xlabel "$S^z_{\\ell/4}$"
plot "mc-control/mc_live.dat" u (bin(($8*c+$6*s),binwidth)):(1.0/sumc) smooth freq w boxes lc 0 title "$P_F^{(0)}$",\
"mc/mc_live.dat" u (bin(($8*c+$6*s),binwidth)):(1.0/sumh) smooth freq w histeps lw 2 lc 1 title "$P_F^{(1)}$",\
"mc-full/mc_live.dat" u (bin($8,binwidth)):(1.0/sumhf) smooth freq w histeps lw 2 lc 3 title "$P_F^{(2)}$",\
"dyn/dyn.dat" u (bin($10,binwidth)):(1.0/sumdh) smooth freq w lp lw 2 lc 2 title "Dynamics",\


