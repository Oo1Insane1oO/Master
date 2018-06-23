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
up=(-0.0142952699962292,-0.0182296036348172,6452.49090907516),
target=(3.5527136788005e-15,0,-2.3283064365387e-10),
zoom=0.907029478458049);

//currentlight=Headlamp;
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
//draw(graf, mean(palette(graf.map(zpart),cmyk(Rainbow()))),black, light=currentlight);
draw(graf, mean(palette(graf.map(zpart),cmyk(Gradient(palecyan, heavycyan, orange, red)))),black, light=currentlight);

axes3("$x$","$y$","$f(x,y)$",min=(-10,-10,0),max=(12,10,900000),arrow=Arrow3(),fontsize(20));

// triple simulatedR(pair ij){
//     real i = ij.x;
//     real j = ij.y;
//     return (i, j, i*i+j*j);
// }
