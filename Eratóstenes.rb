#!/usr/bin/ruby

primes=[2, 3]
i, j, k=5, 0, 0
while i<10000 do
    j=0
    k=i**(0,5)
    j+=1 while (primes[j]>k) and (i%primes[j])!=0
    primes+=[i] if primes[j]>k
    i+=((i%3==2)?2:4)
end

for i in primes do
    print i, " "
end

print "\n"