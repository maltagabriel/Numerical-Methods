function S=soma(i_i,i_f,n)
h=(i_f-i_i)/n;
S=0;
for i=i_i:h:i_f-h
	S=S+h*g(i);
endfor
endfunction

