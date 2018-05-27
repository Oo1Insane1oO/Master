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
camera=(21.7324540905668,22.3692824738985,344.511658986183),
up=(-0.0276081370086271,-0.022891363838785,1.0134040851965),
target=(-7.105427357601e-15,3.5527136788005e-15,2.27373675443232e-13),
zoom=0.822702474791882);

//currentlight=Headlamp;
//real myopacity=0.5;//0.801

triple simulatedS(pair ij){
    real i = ij.x;
    real j = ij.y;
    return (i, j, i*i+j*j);
}

currentlight=Viewport;
surface graf = surface(simulatedS, (-10,-10), (10,10),nu=100,nv=100,Spline);
// draw(graf, mean(palette(graf.map(zpart),cmyk(Rainbow()))),black, light=currentlight);
draw(graf, mean(palette(graf.map(zpart),cmyk(Gradient(palecyan, heavycyan, orange, red)))),black, light=currentlight);

axes3("$x$","$y$","$f(x,y)$",min=(-10,-10,0),max=(10,10,100),arrow=Arrow3(),fontsize(20));
