settings.outformat = "pdf";
settings.prc = false;
settings.render = 16;
size(15cm,9cm,IgnoreAspect);
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
camera=(29.9188827918847,40.8061785268848,122.692819387471),
up=(-0.00985489907315786,-0.0229469731319799,0.54291491651671),
target=(-1.06581410364015e-14,7.105427357601e-15,5.6843418860808e-14),
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
