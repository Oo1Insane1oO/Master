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
camera=(48.810341055688,43.9661776199271,53.7180381411687),
up=(-0.00686758918190323,-0.0115083893675135,0.0937968070248958),
target=(-7.105427357601e-15,1.4210854715202e-14,4.2632564145606e-14),
zoom=0.822702474791882);

triple simulatedS(pair ij){
    real i = ij.x;
    real j = ij.y;
    return (i, j, 0.5*(i*i + j*j - 2*2*abs(i) + 2*2));
}

currentlight=Viewport;
int s = 5;
surface graf = surface(simulatedS, (-s,-s), (s,s),nu=100,nv=100,Spline);
draw(graf, mean(palette(graf.map(zpart),cmyk(Rainbow()))),black, light=currentlight);

axes3("$x$","$y$","$f(x,y)$",min=(-s,-s,0),max=(s,s,15),arrow=Arrow3(),fontsize(20));
