import inequations_cg;
unitsize(3mm);

pen p=bp+deepblue;
pen r=bp+red;

xlimits(-15,5);
xaxis(-15, 4, Ticks("%"),Arrow);

add("hachureG",hatch(H=2mm, dir=NE,deepblue));
hatching(-15,-2,"hachureG");
bracket("-2",-2,S,"]",p);
bracket("$-\infty$",-15,S,"]",p);

add("hachureD",hatch(H=2mm, dir=NW, red));
hatching(-10,0,"hachureD");
bracket("-10",-10,S,"[",r);
bracket("-0",-0,S,"]",r);

shipout(bbox(1mm,invisible));
