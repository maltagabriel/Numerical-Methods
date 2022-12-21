function w = RK4 (ti,tf,h,w0)
  N=ceil((tf-ti)/h);
  w(1)=w0;

for i=2:N
	k1 = h*f(i*h,w(i-1));
        k2 = h*f(i*h+h/2,w(i-1)+k1/2);
        k3 = h*f(i*h+h/2,w(i-1)+k2/2);
        k4 = h*f((i+1)*h,w(i-1)+k3);
	k = k1+2*k2+2*k3+k4;
        w(i) = w(i-1)+1/6*k;
endfor

endfunction
