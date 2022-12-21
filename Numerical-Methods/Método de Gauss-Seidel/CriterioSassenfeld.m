% O método de Gauss-Seidel é um método para solução de sistema linear que deve convergir mais rápido que o critério de Gauss-Jacobi
% mas tem uma condição para poder ser aplicado, que é o critério a seguir:

function c = CriterioSassenfeld(B)

  for i=1:size(B,2)
Bt(i,:)=B(i,:)/B(i,i);
endfor
b=zeros(1,size(B,2));

for i=1:size(B,2)
	  for j=i+1:size(B,2)
		  b(i)=abs(Bt(i,j))+b(i);
endfor
endfor
b
if (norm(b,inf)>1)
  c=0;
endif

if(norm(b,inf)<1)
  c=1;
endif
  endfunction
