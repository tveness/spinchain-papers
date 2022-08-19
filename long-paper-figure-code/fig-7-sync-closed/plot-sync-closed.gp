set terminal epslatex standalone color size 8.0in,3.0in background rgb "white"
set output "fig-7-sync-closed.tex"

tau = 10
A = 0.496

unset xlabel
set ylabel "$m_x$"
set xrange [182:185]
set grid 
set samples 3000
g(x) = -C*cos(2*pi*x)

fit g(x) "closed-sync-avg.dat" u ($1/tau):4 via C
print C

set multiplot layout 2,2 


kx = 200
ky = 0.0055

set tmargin 3
set bmargin 0
set lmargin 9
set xrange [180:200]
set yrange [-0.0059:0.0059]
set format x ''
set xtics 5
set mxtics 5
set grid mxtics
set key top right maxrows 1
set key at kx, ky
plot "closed-sync-avg.dat" u ($1/tau):(-C*cos(2*pi*$1/tau)) w l lc 2 lw 3 title "$C\\cos\\left(\\omega t\\right)$",\
"closed-sync-avg.dat" u ($1/tau):($4) w l lc -1 lw 2 title "$m_x$",\

unset xlabel
set ylabel "$m_x - C\\cos \\left(\\omega t\\right)$"
set format x ''
set bmargin 0
set xtics 50
unset mxtics
set yrange [-0.0059:0.0059]
unset grid
unset key
set xrange [0:200]
set samples 2000
plot "closed-sync-avg.dat" u ($1/tau):($4+C*cos(2*pi*$1/tau)) w l lc 1 title ""


set tmargin 0
unset bmargin
unset yrange
set ylabel "$m_y$"
unset ylabel
set xlabel "$t/\\tau$"
set format x '%.0f'
set key at kx, ky
set xtics 5
set mxtics 5
set ylabel "$m_y$"
set grid xtics mxtics ytics
set lmargin 9

set xrange [180:200]
set yrange [-0.0059:0.0059]

plot "closed-sync-avg.dat" u ($1/tau):(-C*sin(2*pi*$1/tau)) w l lc 2 lw 3 title "$C\\sin\\left(\\omega t\\right)$",\
"closed-sync-avg.dat" u ($1/tau):($5) w l lc -1 lw 2 title "$m_y$",\


set tmargin 0
set lmargin 9
set bmargin 3
unset key
set ylabel "$m_y - C\\sin\\left( \\omega t\\right)$"
set xlabel "$t/\\tau$"
set xtics 50
unset mxtics
set yrange [-0.0059:0.0059]
unset grid
unset key 
set xrange [0:200]
set samples 2000
plot "closed-sync-avg.dat" u ($1/tau):($5+C*sin(2*pi*$1/tau)) w l lc 1 title ""
