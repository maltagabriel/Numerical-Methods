function A = trapezio (a,b,h)
  N = ceil((b-a)/h);
  I(1)=0;

for i=1:N
	xf = a + i*h;
        xi= a + (i-1)*h;
        x(i)=xi;
        fi = f(xi);
        func(i)=fi;
        ff = f(xf);
        fm = (ff-fi)/2;
        s=h*fm;
I(i+1)=s;
endfor

A=sum(I);

disp(A)
plot(x,func);
  endfunction
