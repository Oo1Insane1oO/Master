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
camera=(31.6563712834458,18.1737139134171,355.333364889253),
up=(-0.0398044889396582,-0.0162787277441343,1.00853451614852),
target=(-1.4210854715202e-14,1.06581410364015e-14,5.6843418860808e-14),
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
draw(graf, mean(palette(graf.map(zpart),Wheel())),black, light=currentlight);

axes3("$x$","$y$","$f(x,y)$",min=(-10,-10,0),max=(10,10,100),arrow=Arrow3(),fontsize(20));

// triple simulatedR(pair ij){
//     real i = ij.x;
//     real j = ij.y;
//     return (i, j, i*i+j*j);
// }
