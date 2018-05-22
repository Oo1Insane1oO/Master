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

currentprojection=perspective(
camera=(84.7629923596942,-92.7374492936132,36.2280163371789),
up=(-0.0644074031752014,0.0502786661560219,0.0423516180682772),
target=(2.17766950816237,1.40494269901863,12.5166869511021),
zoom=0.822702474791882,
angle=47.287614411611);

triple simulatedS(pair ij){
    real i = ij.x;
    real j = ij.y;
    return (i, j, -20*exp(-0.2*sqrt(0.5*(i*i+j*j))) - exp(0.5*(cos(2*pi*i) +
                    cos(2*pi*j))) + 20+exp(1));
}

currentlight=Viewport;
surface graf = surface(simulatedS, (-40,-40), (40,40),nu=100,nv=100,Spline);
draw(graf, mean(palette(graf.map(zpart),cmyk(Wheel()))),black, light=currentlight);

axes3("$x$","$y$","$f(x,y)$",min=(-40,-40,0),max=(40,40,30),arrow=Arrow3(),fontsize(20));
