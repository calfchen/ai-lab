#
# CA-GrQc In Degree. G(5242, 14496). 1361 (0.2596) nodes with in-deg > avg deg (5.5), 579 (0.1105) with >2*avg.deg (Wed Aug 08 14:19:12 2018)
#

set title "CA-GrQc In Degree. G(5242, 14496). 1361 (0.2596) nodes with in-deg > avg deg (5.5), 579 (0.1105) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'inDeg.CA-GrQc.png'
plot 	"inDeg.CA-GrQc.tab" using 1:2 title "" with linespoints pt 6
