#include<stdio.h>
#include<graphics.h>
#include<math.h>
int main()
{
	int gd,gm;
	int r,i,a,b,x,y;
	float PI=3.14;
	
	detectgraph(&gd,&gm);
	initgraph(&gd,&gm,"C:\TURBOC3\BGI");
	
	//draw the top rectangle and color it
	setcolor(RED);
	rectangle(100,100,450,150);
	setfillstyle(SOLID_FILL,RED);
	floodfill(101,101,RED);

	//draw the middle rectangle and color it
	setcolor(WHITE);
	rectangle(100,150,450,200);
	setfillstyle(SOLID_FILL,WHITE);
	floodfill(101,151,WHITE);

	//draw the bottom rectangle and color it
	setcolor(GREEN);
	rectangle(100,200,450,250);
	setfillstyle(SOLID_FILL,GREEN);
	floodfill(101,201,GREEN);

	//draw the circle
	a=275;	//center
	b=175;	//center
	r=25;	//radius
	setcolor(BLUE);
	circle(a,b,r);

	//spokes
	for(i=0;i<=360;i=i+15)
	{
		x=r*cos(i*PI/180);
		y=r*sin(i*PI/180);
		line(a,b,a+x,b-y);
	}

	getch();
	closegraph();
	return 0;
}