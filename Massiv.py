aa = [5,6,8,'Hello',[7,9,'LU'],0.999]

print(aa) # izvadit visu sarakstu

print (len(aa)) # saraksta garums, vertibu skaits

print(aa[1]) #izvadit 1 indeksa vertibu - 6

print(aa[4]) #izvadit 4 indeksa vertibu  - 7,9,'LU'

print(aa[4][2]) #izvadit 4 indeksa saraksta vertibas 7,9,'LU' 2 indeksa vertibu - LU

aa[2] = 11 # mainit 2 indeksa vertibu no 8 uz 11

print(aa) # izvadit jaunu sarakstu

aa.append(17) # sarakstam pievienot vertibu

print(aa) # izvadit jaunu sarakstu

aa.pop(0) # dzest 0 indeksa vertibu - 5

print(aa) # izvadit jaunu sarakstu