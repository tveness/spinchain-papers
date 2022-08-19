set terminal epslatex standalone color size 8.0in,3.0in background rgb "white"
set output "fig-6-sync-open.tex"

tau = 10
A = 0.496

unset xlabel
set ylabel "$m_x$"
set xrange [100:200]
set grid 
set samples 3000
f(x) = -A*cos(2*pi*x)

fit f(x) "open-sync-avg.dat" u ($1/tau):4 via A
print A

set multiplot layout 2,2 

set tmargin 3
set bmargin 0
set lmargin 7
set xrange [180:200]
set yrange [-1.499:1.499]
set format x ''
set xtics 5
set mxtics 5
set grid mxtics
set key top right maxrows 1
plot "open-sync-avg.dat" u ($1/tau):(-A*cos(2*pi*$1/tau)) w l lc 2 lw 3 title "$A\\cos\\left(\\omega t\\right)$",\
"open-sync-avg.dat" u ($1/tau):($4) w l lc -1 lw 2 title "$m_x$",\

unset xlabel
set ylabel "$m_x - A\\cos \\left(\\omega t\\right)$"
set format x ''
set bmargin 0
set xtics 50
unset mxtics
set yrange [-0.5:0.5]
unset grid
unset key
set xrange [0:200]
set samples 2000
plot "open-sync-avg.dat" u ($1/tau):($4+A*cos(2*pi*$1/tau)) w l lc 1 title ""


set tmargin 0
unset bmargin
unset yrange
set ylabel "$m_y$"
unset ylabel
set xlabel "$t/\\tau$"
set format x '%.0f'
set key top right
set xtics 5
set ytics 0.5
set mxtics 5
set ylabel "$m_y$"
set grid xtics mxtics ytics
set lmargin 7

set xrange [180:200]
set yrange [-1.499:1.499]

plot "open-sync-avg.dat" u ($1/tau):(-A*sin(2*pi*$1/tau)) w l lc 2 lw 3 title "$A\\sin\\left(\\omega t\\right)$",\
"open-sync-avg.dat" u ($1/tau):($5) w l lc -1 lw 2 title "$m_y$",\


set tmargin 0
set lmargin 7
set bmargin 3
unset key
set ylabel "$m_y - A\\sin\\left( \\omega t\\right)$"
set xlabel "$t/\\tau$"
set xtics 50
unset mxtics
set yrange [-0.5:0.5]
set ytics 0.003
set ytics 0.2
unset grid
unset key 
set xrange [0:200]
set samples 2000
plot "open-sync-avg.dat" u ($1/tau):($5+A*sin(2*pi*$1/tau)) w l lc 1 title ""
