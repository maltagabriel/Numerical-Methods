%Método de Gaus-Jacobi para resolução de sistemas lineares com chute inicial
%Eu coloquei como entrada as matrizes superior, inferior e diagonal, mas você poderia calculá-las todas dentro da própria função que implementa o método

function x = GaussJacobi(D,L,R,d,x)
  
C=-inv(D)*(L+R);
be=inv(D)*d;

while (e>0.001)
x1=x;
x=C*x1+be;
e=norm(x-x1)/norm(x);
endwhile
  
endfunction

    
