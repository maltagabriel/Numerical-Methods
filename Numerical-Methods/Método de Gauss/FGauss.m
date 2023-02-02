
%Escalonamento de uma matriz, método básico para todos outros de resolução de sistema linear

function FGauss (A,d)

n=size(A,1);
I = eye(n);
Ad = [A d];

x = zeros(n,1);

for k = 1:n-1
    for i = k+1:n
    	m = Ad(i,k)/Ad(k,k);

    	Ad(i,k) = 0;
    	    
    	for j = k+1:n
    	    Ad(i,j) = Ad(i,j) - m*Ad(k,j);
    	end

   	    Ad(i,n+1) = Ad(i,n+1) - m*Ad(k,n+1);
        A = Ad(:,[1,n])
        disp('Matriz aumentada: ')
   	    disp(Ad)
    end
end

endfunction
