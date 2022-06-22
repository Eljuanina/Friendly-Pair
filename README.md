## Friendly Pair

According to number theory, a friendly number is a natural number that shares a certain characteristic, called abundancy, with one or more other numbers. 
Abundancy is the ratio between the sum of divisors of the number and the number itself. Two different numbers with the same abundancy form a friendly pair.

The abundancy of n is the rational number σ(n) / n, in which σ denotes the sum of divisors function. A number n is a friendly number if there exists m ≠ n where σ(m) / m = σ(n) / n.

For example 6 is a friendly number because abundancy of 6 and 28 are same : 2. Thus 6 and 28 are friendly pair.

The implemented algorithm in the function isFriendlyPair checks whether two numbers are a friendly pair or not.