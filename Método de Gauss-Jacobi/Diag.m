%o Octave tem a função diag que faz a mesma coisa que essa que eu construí aqui, possivelmente de forma mais efetiva
function D = Diag (A)
  
for i= 1:10
	 for j=1:10
		 if (i=j)
		   D(i,j)=A(i,j);
		 else
		   R(i,j)=0;
endif
         endfor
endfor

endfunction
