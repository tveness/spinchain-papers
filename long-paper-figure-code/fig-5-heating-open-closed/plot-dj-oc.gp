set terminal epslatex standalone color size 8.0in,4.0in background rgb "white"
set output "fig-5-heating-open-closed.tex"
set multiplot layout 1, 2

set lmargin 8
set rmargin 1

set xlabel "$\\tau$"
set ylabel "$e$"
set samples 3000
set xrange[0:20.0001]
set yrange [-1.3:0.05]
set key bottom right

set label "\\textsc{Closed}" at 3,-1
plot "closed/1000-cycles-dj-0.2.dat" u ($1/1000):2 w lp lc 9 lt 9 title "$\\delta J = 0.2$",\
"closed/1000-cycles-dj-0.1.dat" u ($1/1000):2 w lp lc 8 lt 8 title "$\\delta J = 0.1$",\
"closed/1000-cycles-dj-0.05.dat" u ($1/1000):2 w lp lc 7 lt 7 title "$\\delta J = 0.05$",\
"closed/1000-cycles-dj-0.04.dat" u ($1/1000):2 w lp lc 6 lt 6 title "$\\delta J = 0.04$",\
"closed/1000-cycles-dj-0.03.dat" u ($1/1000):2 w lp lc 5 lt 5 title "$\\delta J = 0.03$",\
"closed/1000-cycles-dj-0.02.dat" u ($1/1000):2 w lp lc 4 lt 4 title "$\\delta J = 0.02$",\
"closed/1000-cycles-dj-0.01.dat" u ($1/1000):2 w lp lc 3 lt 3 title "$\\delta J = 0.01$",\

set lmargin 1
set rmargin 5

unset label
unset ylabel
set format y ""

set label "\\textsc{Open}" at 3,-1
plot "open/1000-cycles-dj-0.2.dat" u ($1/1000):3 w lp lc 9 lt 9 dt 2 title "",\
"open/1000-cycles-dj-0.1.dat" u ($1/1000):3 w lp lc 8 lt 8 dt 2 title "",\
"open/1000-cycles-dj-0.05.dat" u ($1/1000):3 w lp lc 7 lt 7 dt 2 title "",\
"open/1000-cycles-dj-0.04.dat" u ($1/1000):3 w lp lc 6 lt 6 dt 2 title "",\
"open/1000-cycles-dj-0.03.dat" u ($1/1000):3 w lp lc 5 lt 5 dt 2 title "",\
"open/1000-cycles-dj-0.02.dat" u ($1/1000):3 w lp lc 4 lt 4 dt 2 title "",\
"open/1000-cycles-dj-0.01.dat" u ($1/1000):3 w lp lc 3 lt 3 dt 2 title "",\
