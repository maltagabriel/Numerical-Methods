function R = Right (A)
  
for i= 1:10
	 for j=1:10
		 if (i<j)
		   R(i,j)=A(i,j);
		 else
		   R(i,j)=0;
endif
         endfor
endfor

endfunction
