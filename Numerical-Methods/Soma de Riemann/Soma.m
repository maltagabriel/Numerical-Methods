function S=Soma(i_i,i_f,n)
h=(i_f-i_i)/n;
S=0;
for i=i_i+h:h:i_f
	S=S+h*g(i);
endfor
endfunction
