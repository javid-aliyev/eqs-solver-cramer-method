https://github.com/javid-aliyev/
28.06.2022 00:35, Baku GMT+4

Cramer's rule - https://en.wikipedia.org/wiki/Cramer%27s_rule

Systems of two linear equations with two unknowns (the number of unknowns is equal to the number of equations). Solution by Cramer's method. The algorithm and the parser are still raw and cannot automatically determine the coefficient of the same unknowns. Therefore, it all depends on how the equations are written. The program itself will determine if the system has no solutions. Equations are taken from the equations.txt file. Unknowns should always be called x and y. Coefficients != 0

====
a1x + b1y = s1
a2x + b2y = s2
====

==Use this input pattern==
a1x+b1y=s1
a2x+b2y=s2
====

==Examples==
2x+3y=5
3x+2y=10

4x+5y=10
9x+4y=15
====

WARNING:
if coefficient equals 1 then it doesn't matter, you must write it
1x+1y=5
2x+2y=10

AND THE PROGRAM CAN'T WORK WITH NEGATIVE NUMBERS
IT TAKES THEM AS POSITIVE NUMBERS
BECAUSE OF REGEXP...
AND IT ALSO CAN NOT HANDLE FRACTIONS