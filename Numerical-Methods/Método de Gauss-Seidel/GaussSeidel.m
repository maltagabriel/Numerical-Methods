% Dado erro e chute inicial, o método de Gauss-Seidel calcula uma solução aproximada (com erro menor do que o dado) para o sistema linear
function y = GaussSeidel (M,b,x)
   E=1;
   
for i=1:size(M,2)
  Mt(i,:)=M(i,:)/M(i,i);
  bt(i)=b(i)/M(i,i);
endfor

bt=transpose(bt);
I=eye(size(M,2))
Lt=tril(Mt)-I
Rt=triu(Mt)-I

while (E>0.001)
  x1=x;
  x=-Lt*x-Rt*x1+bt;
  E=norm(x-x1,inf);
endwhile

endfunction
