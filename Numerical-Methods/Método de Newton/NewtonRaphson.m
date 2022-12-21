% Acha (com erro menor que E) o zero de uma função f sabendo sua derivada (fl) a partir de um chute inicial x0 

function x=NewtonRaphson(x0,E)

k=0;

output_precision(9);
er=1;
x=x0;
k
x
f(x)
  disp('--------------------------------');

while (E  <= er)
  xa=x;
  x = xa-f(xa)/fl(xa);
  er = norm(x-xa);
  k++;
  k
  x
  f(xa)
  er
  disp('-------------------------------');
endwhile

endfunction
