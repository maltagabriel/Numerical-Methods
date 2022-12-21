% Exibe a solução de um sistema linear já escalonado/triangulado

function SolSistTriang (T,d)

n=size(T,1)  
Td = [T d];
x(n) = Td(n,n+1)/Td(n,n);

for k = n-1:1
    s = 0;
    for j = k+1:n
	s = s + Td(k,j)*x(j);
    end

    x(k) = (Td(k,n+1)-s)/Td(k,k);
end

disp('Solução obtida: ')
disp(x)

endfunction
 
