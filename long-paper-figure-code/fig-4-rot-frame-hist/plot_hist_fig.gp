set terminal epslatex standalone color size 8.0in,3.0in background rgb "white"
set output "fig-4-low-frequency-histograms.tex"



binwidth = 0.05


bin(x,width)=width*(floor(x/width) + 0.5)
set multiplot layout 1,3 margins 0.1,0.95,0.20,0.98 spacing 0.05,0.09


tau = 4
omega=2*pi/tau
# e low freq

sumc = "`wc -l mc-control/mc_live.dat`"
suml = "`wc -l mc/mc_live.dat`"
sumlb = "`wc -l mc/mc_live-big-e-0.115.dat`"
sumdl = "`wc -l dyn/dyn-samples.dat`"
sumc = sumc*binwidth
suml = suml*binwidth
sumlb = sumlb*binwidth
sumdl = sumdl*binwidth

set boxwidth binwidth

#set style fill solid 0.06 noborder 
set style fill solid 0.25 noborder 
set key Left reverse at graph 1.2,0.98 spacing 1.3
set yrange [0:4]
set xrange [-1.6:0.2]
#unset xrange
#unset yrange
set xtics .4
set xlabel "$e$"
set ylabel "$P$"
plot "mc-control/mc_live.dat" u (bin($2+omega*$5,binwidth)):(1.0/sumc) smooth freq w boxes lc 0 title "$P_{0}$",\
"mc/mc_live-big-e-0.115.dat" u (bin($2+omega*$5,binwidth)):(1.0/sumlb) smooth freq w histeps lw 2 lc 1 title "$P_\\mathrm{rot}(\\beta_\\mathrm{rot}^*)$",\
"mc/mc_live.dat" u (bin($2+omega*$5,binwidth)):(1.0/suml) smooth freq w histeps lw 2 lc 3 title "$P_\\mathrm{rot}(\\beta_\\mathrm{rot}^\\mathrm{stat})$",\
"dyn/dyn-samples.dat" u (bin($3,binwidth)):(1.0/sumdl) smooth freq w lp lw 2 lc 2 title "Dynamics $\\tau=4$ ",\

unset key 
set xtics auto
set xrange [-1:1]
set yrange [0:4.5]
set xlabel "$m_x$"
unset ylabel 

plot "mc-control/mc_live.dat" u (bin($3,binwidth)):(1.0/sumc) smooth freq w boxes lc 0 title "MC $P_{0}$",\
"mc/mc_live-big-e-0.115.dat" u (bin($3,binwidth)):(1.0/sumlb) smooth freq w histeps lw 2 lc 1 title "MC $P_\\mathrm{rot}$ best",\
"mc/mc_live.dat" u (bin($3,binwidth)):(1.0/suml) smooth freq w histeps lw 2 lc 3 title "MC $P_\\mathrm{rot}$",\
"dyn/dyn-samples.dat" u (bin($4,binwidth)):(1.0/sumdl) smooth freq w lp lw 2 lc 2 title "Dynamics"


unset key
set xrange [-1:1]
set yrange [0:2.5]
set xlabel "$S^x_{\\ell/4} S^x_{3\\ell/4}$"
plot "mc-control/mc_live.dat" u (bin($6*$9,binwidth)):(1.0/sumc) smooth freq w boxes lc 0 title "MC $P_{0}$",\
"mc/mc_live-big-e-0.115.dat" u (bin($6*$9,binwidth)):(1.0/sumlb) smooth freq w histeps lw 2 lc 1 title "MC $P_\\mathrm{rot}$ best",\
"mc/mc_live.dat" u (bin($6*$9,binwidth)):(1.0/suml) smooth freq w histeps lw 2 lc 3 title "MC $P_\\mathrm{rot}$",\
"dyn/dyn-samples.dat" u (bin($8*$11,binwidth)):(1.0/sumdl) smooth freq w lp lw 2 lc 2 title "Dynamics"
