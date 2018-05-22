settings.outformat = "pdf";
settings.prc = false;
settings.render = 16;
size(18cm,9cm,IgnoreAspect);
import three;
import graph3;
import contour;
import palette;
import fontsize;
usepackage("mathdesign");

defaultpen(fontsize(12pt));

currentprojection=orthographic(
camera=(26.0935158686183,33.2749714613687,1753961.89227429),
up=(-0.0240978954315237,-0.0282958474986643,3508.89213393995),
target=(0,0,-2.3283064365387e-10),
zoom=0.613913253540759);

currentlight=Headlamp;
//real myopacity=0.5;//0.801

triple simulatedS(pair ij){
    real i = ij.x;
    real j = ij.y;
    real jipr = 100.*j - i*i;
    real im = i-1;
    return (i, j, jipr*jipr + im*im);
}

currentlight=Viewport;
surface graf = surface(simulatedS, (-10,-10), (10,10),nu=100,nv=100,Spline);
draw(graf, mean(palette(graf.map(zpart),Wheel())),black, light=currentlight);

axes3("$x$","$y$","$f(x,y)$",min=(-10,-10,0),max=(12,10,1200000),arrow=Arrow3(),fontsize(20));

// triple simulatedR(pair ij){
//     real i = ij.x;
//     real j = ij.y;
//     return (i, j, i*i+j*j);
// }
