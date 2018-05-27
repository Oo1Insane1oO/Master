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

currentprojection=perspective(
camera=(13.7983962520023,9.58380802278321,142.696880890009),
up=(-0.0163374487138208,-0.0206870928463049,0.483118897039435),
target=(0.452147120704446,0.0567648127768035,54.7952671263372),
zoom=0.90702947845805,
angle=44.1726701566335);

//currentlight=Headlamp;
//real myopacity=0.5;//0.801

triple simulatedS(pair ij){
    real i = ij.x;
    real j = ij.y;
    return (i, j, 20 + i*i - 10*cos(2*pi*i) + j*j - 10*cos(2*pi*j));
}

currentlight=Viewport;
surface graf = surface(simulatedS, (-5,-5), (5,5),nu=100,nv=100,Spline);
//draw(graf, mean(palette(graf.map(zpart),cmyk(Wheel()))),black, light=currentlight);
draw(graf, mean(palette(graf.map(zpart),cmyk(Gradient(palecyan, heavycyan, orange, red)))),black, light=currentlight);

axes3("$x$","$y$","$f(x,y)$",min=(-5,-5,0),max=(5,5,100),arrow=Arrow3(),fontsize(20));
