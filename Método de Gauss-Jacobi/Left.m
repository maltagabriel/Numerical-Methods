function L = Left (A)
  
for i= 1:10
	 for j=1:10
		 if (i>j)
		   L(i,j)=A(i,j);
		 else
		   L(i,j)=0;
endif
         endfor
endfor

endfunction
