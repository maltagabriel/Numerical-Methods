% Dado erro e chute inicial, o método de Gauss-Seidel calcula uma solução aproximada (com erro menor do que o dado) para o sistema linear
function y = GaussSeidel (M,e,x)

 for i=1:10
 Mt(i,:)=M(i,:)/M(i,i);
et(i)=e(i)/M(i,i);
endfor

et=transpose(et);
I=eye(10);
Lt=tril(Mt)-I;
Rt=triu(Mt)-I;

while (E>0.001)
  x1=x;
x=-Lt*x-Rt*x1+et;
E=norm(x-x1,inf);
  endwhile

endfucntion
