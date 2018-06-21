settings.outformat = "pdf";
settings.prc = false;
settings.render = 16;
size(15cm,10cm,IgnoreAspect);
import three;
import graph3;
usepackage("mathpazo");

// currentprojection=orthographic((-0.15,-3.5,0.5),up=Z);
// currentlight=light(-0.15,-3.5,1.5);
real myopacity=1;//0.801

real[][] simulatedPs = input("test1dw").line();
int num_rhos = 400;
int num_Ts = 400;

triple simulatedP(pair ij){
    int i = (int) ij.x;
    int j = (int) ij.y;
    return (i, j, simulatedPs[i][j]);
}

surface graf = surface(simulatedP, (0,0), (num_rhos-1,num_Ts-1),nu=num_rhos,nv=num_Ts,Spline);
draw(graf,surfacepen=material(red+opacity(myopacity)));
