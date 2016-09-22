import inequations_cg;
unitsize(1cm);

pen p=bp+deepblue;

xlimits(-2.4,2.4);
xaxis(-2.4, 2.4, Ticks("%"),Arrow);
bracket("0",0,S,"]",p);
bracket("$-\infty$",-2.4,S,"]",p);

add("hachure",hatch(H=2mm,dir=NE,deepblue));
hatching(-2.4,0,"hachure");

shipout(bbox(1mm,invisible));
