function x = NewtonSis(x0,E)
  er = 1;
i=0
  x = x0;
while er>E
xa = x;
s = J(x)\(-f(x));
x = x + s;
er = norm(x-xa);
i=i+1
endwhile

endfunction
