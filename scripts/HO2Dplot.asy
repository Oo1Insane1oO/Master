settings.outformat = "pdf";
settings.prc = false;
settings.render = 16;
size(17cm,9cm,IgnoreAspect);
import three;
import graph3;
import contour;
import palette;
import fontsize;
usepackage("mathdesign");

defaultpen(fontsize(12pt));

//currentlight=Headlamp;
//real myopacity=0.5;//0.801

currentprojection=orthographic(
camera=(28.4375097581347,23.0913041164081,288.569509302791),
up=(-0.0260191809381273,-0.0151050308523034,1.07458626845793),
target=(-7.105427357601e-15,1.06581410364015e-14,1.13686837721616e-13),
zoom=0.822702474791882);

triple simulatedS(pair ij){
    real i = ij.x;
    real j = ij.y;
    return (i, j, 0.5*(i*i + j*j));
}

currentlight=Viewport;
surface graf = surface(simulatedS, (-10,-10), (10,10),nu=100,nv=100,Spline);
draw(graf, mean(palette(graf.map(zpart),cmyk(Rainbow()))),black, light=currentlight);

axes3("$x$","$y$","$f(x,y)$",min=(-10,-10,0),max=(10,10,100),arrow=Arrow3(),fontsize(20));
