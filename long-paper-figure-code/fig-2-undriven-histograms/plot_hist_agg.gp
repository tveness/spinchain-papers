set terminal epslatex standalone color size 8.0in,6.0in background rgb "white"


set output "fig-2-undriven-histograms.tex"
set multiplot layout 2,2 
#margins 0.1,0.9,0.1,0.9 spacing 0.05,0.09
# spacing 0.5,2.5
#set bmargin 4.0


summ = "`wc -l hist_mc.dat`"
sumd = "`wc -l hist_dyn.dat`"
binwidth = 0.01
summ = summ*binwidth
sumd = sumd*binwidth
set boxwidth binwidth
bin(x,width)=width*(floor(x/width) + 0.5)

set lmargin 9
set rmargin 0.5
set tmargin 0.5
set bmargin 5

unset xrange
unset yrange
set xlabel "$e$"
set ylabel "$P(e)$"
set key spacing 1.5

set label 1 at graph 0.5,-0.258 offset char -1,0 "(a)"

set xrange [-.9:-.4]
plot "hist_mc.dat" u (bin($5,binwidth)):(1.0/summ) smooth freq w histeps title "$P_{\\mathrm can}(e)$",\
"hist_dyn.dat" u (bin($5,binwidth)):(1.0/sumd) smooth freq w lp lw 3 title "$P_T(e)$",\
"analytic-hist.dat" u 1:2 w l title "$P_\\ell(e)$" lc -1 dt 2 lw 1 

set lmargin 9
set rmargin 0.5
set tmargin 0.5
set bmargin 5

summ = "`wc -l hist_mc.dat`"
sumd = "`wc -l hist_dyn.dat`"
binwidth = 0.05
summ = summ*binwidth
sumd = sumd*binwidth
set boxwidth binwidth


set xrange [-1:1]
set xlabel "$m_x$"
set ylabel "$P(m_x)$"
set key spacing 1.5

set xrange [-1:1]
set yrange [0:2.5]
set label 1 at graph 0.5,-0.258 offset char -1,0 "(b)"

plot "hist_mc.dat" u (bin($2,binwidth)):(1.0/summ) smooth freq w histeps title "$P_{\\mathrm can}(m_x)$",\
"hist_dyn.dat" u (bin($2,binwidth)):(1.0/sumd) smooth freq w lp lw 3 title "$P_T(m_x)$",\

set label 1 at graph 0.5,-0.258 offset char -1,0 "(c)"

set lmargin 9
set rmargin 0.5
set tmargin 0.5
set bmargin 5

set xrange [-1:1]
set yrange [0:2.5]
set xlabel "$m_y$"
set ylabel "$P(m_y)$"
set key spacing 1.5

plot "hist_mc.dat" u (bin($3,binwidth)):(1.0/summ) smooth freq w histeps title "$P_{\\mathrm can}(m_y)$",\
"hist_dyn.dat" u (bin($3,binwidth)):(1.0/sumd) smooth freq w lp lw 3 title "$P_T(m_y)$"


set lmargin 9
set rmargin 0.5
set tmargin 0.5
set bmargin 5

set label 1 at graph 0.5,-0.258 offset char -1,0 "(d)"
set xrange [-1:1]
set yrange [0:2.5]
set xlabel "$m_z$"
set ylabel "$P(m_z)$"
set key spacing 1.5

plot "hist_mc.dat" u (bin($4,binwidth)):(1.0/summ) smooth freq w histeps title "$P_{\\mathrm can}(m_z)$",\
"hist_dyn.dat" u (bin($4,binwidth)):(1.0/sumd) smooth freq w lp lw 3 title "$P_T(m_z)$"

