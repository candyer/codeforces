[Complete problemset](https://codeforces.com/contest/1102/problems)


# Codeforces Round #531 (Div. 3)   
##A. Integer Sequence Dividing
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given an integer sequence 1,2,…,𝑛. You have to divide it into two sets 𝐴 and 𝐵 in such a way that each element belongs to exactly one set and |𝑠𝑢𝑚(𝐴)−𝑠𝑢𝑚(𝐵)| is minimum possible.

The value |𝑥| is the absolute value of 𝑥 and 𝑠𝑢𝑚(𝑆) is the sum of elements of the set 𝑆.

Input
The first line of the input contains one integer 𝑛 (1≤𝑛≤2⋅109).

Output
Print one integer — the minimum possible value of |𝑠𝑢𝑚(𝐴)−𝑠𝑢𝑚(𝐵)| if you divide the initial sequence 1,2,…,𝑛 into two sets 𝐴 and 𝐵.  

Examples  
```
inputCopy     
3   
outputCopy  
0  
inputCopy   
5  
outputCopy  
1  
inputCopy  
6  
outputCopy  
1  
```
Note
Some (not all) possible answers to examples:

In the first example you can divide the initial sequence into sets 𝐴={1,2} and 𝐵={3} so the answer is 0.

In the second example you can divide the initial sequence into sets 𝐴={1,3,4} and 𝐵={2,5} so the answer is 1.

In the third example you can divide the initial sequence into sets 𝐴={1,4,5} and 𝐵={2,3,6} so the answer is 1.

## B. Array K-Coloring  
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given an array 𝑎 consisting of 𝑛 integer numbers.

You have to color this array in 𝑘 colors in such a way that:

Each element of the array should be colored in some color;
For each 𝑖 from 1 to 𝑘 there should be at least one element colored in the 𝑖-th color in the array;
For each 𝑖 from 1 to 𝑘 all elements colored in the 𝑖-th color should be distinct.
Obviously, such coloring might be impossible. In this case, print "NO". Otherwise print "YES" and any coloring (i.e. numbers 𝑐1,𝑐2,…𝑐𝑛, where 1≤𝑐𝑖≤𝑘 and 𝑐𝑖 is the color of the 𝑖-th element of the given array) satisfying the conditions above. If there are multiple answers, you can print any.

Input
The first line of the input contains two integers 𝑛 and 𝑘 (1≤𝑘≤𝑛≤5000) — the length of the array 𝑎 and the number of colors, respectively.

The second line of the input contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤5000) — elements of the array 𝑎.

Output
If there is no answer, print "NO". Otherwise print "YES" and any coloring (i.e. numbers 𝑐1,𝑐2,…𝑐𝑛, where 1≤𝑐𝑖≤𝑘 and 𝑐𝑖 is the color of the 𝑖-th element of the given array) satisfying the conditions described in the problem statement. If there are multiple answers, you can print any.


Examples  
```
inputCopy  
4 2  
1 2 2 3  
outputCopy  
YES  
1 1 2 2  
inputCopy  
5 2  
3 2 1 2 3  
outputCopy  
YES  
2 1 1 2 1  
inputCopy  
5 2  
2 1 1 2 1  
outputCopy  
NO  
```
Note
In the first example the answer 2 1 2 1 is also acceptable.

In the second example the answer 1 1 1 2 2 is also acceptable.

There exist other acceptable answers for both examples.

## C. Doors Breaking and Repairing  
time limit per test1 second
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are policeman and you are playing a game with Slavik. The game is turn-based and each turn consists of two phases. During the first phase you make your move and during the second phase Slavik makes his move.

There are 𝑛 doors, the 𝑖-th door initially has durability equal to 𝑎𝑖.

During your move you can try to break one of the doors. If you choose door 𝑖 and its current durability is 𝑏𝑖 then you reduce its durability to 𝑚𝑎𝑥(0,𝑏𝑖−𝑥) (the value 𝑥 is given).

During Slavik's move he tries to repair one of the doors. If he chooses door 𝑖 and its current durability is 𝑏𝑖 then he increases its durability to 𝑏𝑖+𝑦 (the value 𝑦 is given). Slavik cannot repair doors with current durability equal to 0.

The game lasts 10100 turns. If some player cannot make his move then he has to skip it.

Your goal is to maximize the number of doors with durability equal to 0 at the end of the game. You can assume that Slavik wants to minimize the number of such doors. What is the number of such doors in the end if you both play optimally?

Input
The first line of the input contains three integers 𝑛, 𝑥 and 𝑦 (1≤𝑛≤100, 1≤𝑥,𝑦≤105) — the number of doors, value 𝑥 and value 𝑦, respectively.

The second line of the input contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤105), where 𝑎𝑖 is the initial durability of the 𝑖-th door.

Output
Print one integer — the number of doors with durability equal to 0 at the end of the game, if you and Slavik both play optimally.

Examples  
```
inputCopy  
6 3 2  
2 3 1 3 4 2  
outputCopy  
6  
inputCopy  
5 3 3  
1 2 4 2 3  
outputCopy  
2  
inputCopy  
5 5 6  
1 2 6 10 3  
outputCopy  
2  
```
Note
Clarifications about the optimal strategy will be ignored.

## D. Balanced Ternary String  
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given a string 𝑠 consisting of exactly 𝑛 characters, and each character is either '0', '1' or '2'. Such strings are called ternary strings.

Your task is to replace minimum number of characters in this string with other characters to obtain a balanced ternary string (balanced ternary string is a ternary string such that the number of characters '0' in this string is equal to the number of characters '1', and the number of characters '1' (and '0' obviously) is equal to the number of characters '2').

Among all possible balanced ternary strings you have to obtain the lexicographically (alphabetically) smallest.

Note that you can neither remove characters from the string nor add characters to the string. Also note that you can replace the given characters only with characters '0', '1' and '2'.

It is guaranteed that the answer exists.

Input
The first line of the input contains one integer 𝑛 (3≤𝑛≤3⋅105, 𝑛 is divisible by 3) — the number of characters in 𝑠.

The second line contains the string 𝑠 consisting of exactly 𝑛 characters '0', '1' and '2'.

Output
Print one string — the lexicographically (alphabetically) smallest balanced ternary string which can be obtained from the given one with minimum number of replacements.

Because 𝑛 is divisible by 3 it is obvious that the answer exists. And it is obvious that there is only one possible answer.


Examples  
```
inputCopy  
3  
121  
outputCopy  
021  
inputCopy  
6  
000000  
outputCopy  
001122  
inputCopy  
6  
211200  
outputCopy  
211200  
inputCopy  
6  
120110  
outputCopy  
120120  
```

## E. Monotonic Renumeration  
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given an array 𝑎 consisting of 𝑛 integers. Let's denote monotonic renumeration of array 𝑎 as an array 𝑏 consisting of 𝑛 integers such that all of the following conditions are met:

𝑏1=0;
for every pair of indices 𝑖 and 𝑗 such that 1≤𝑖,𝑗≤𝑛, if 𝑎𝑖=𝑎𝑗, then 𝑏𝑖=𝑏𝑗 (note that if 𝑎𝑖≠𝑎𝑗, it is still possible that 𝑏𝑖=𝑏𝑗);
for every index 𝑖∈[1,𝑛−1] either 𝑏𝑖=𝑏𝑖+1 or 𝑏𝑖+1=𝑏𝑖+1.
For example, if 𝑎=[1,2,1,2,3], then two possible monotonic renumerations of 𝑎 are 𝑏=[0,0,0,0,0] and 𝑏=[0,0,0,0,1].

Your task is to calculate the number of different monotonic renumerations of 𝑎. The answer may be large, so print it modulo 998244353.

Input
The first line contains one integer 𝑛 (2≤𝑛≤2⋅105) — the number of elements in 𝑎.

The second line contains 𝑛 integers 𝑎1,𝑎2,…,𝑎𝑛 (1≤𝑎𝑖≤109).

Output
Print one integer — the number of different monotonic renumerations of 𝑎, taken modulo 998244353.


Examples   
```
inputCopy  
5  
1 2 1 2 3  
outputCopy  
2  
inputCopy  
2  
100 1  
outputCopy  
2  
inputCopy  
4  
1 3 3 7  
outputCopy  
4  
```

## F. Elongated Matrix  
time limit per test4 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
You are given a matrix 𝑎, consisting of 𝑛 rows and 𝑚 columns. Each cell contains an integer in it.

You can change the order of rows arbitrarily (including leaving the initial order), but you can't change the order of cells in a row. After you pick some order of rows, you traverse the whole matrix the following way: firstly visit all cells of the first column from the top row to the bottom one, then the same for the second column and so on. During the traversal you write down the sequence of the numbers on the cells in the same order you visited them. Let that sequence be 𝑠1,𝑠2,…,𝑠𝑛𝑚.

The traversal is 𝑘-acceptable if for all 𝑖 (1≤𝑖≤𝑛𝑚−1) |𝑠𝑖−𝑠𝑖+1|≥𝑘.

Find the maximum integer 𝑘 such that there exists some order of rows of matrix 𝑎 that it produces a 𝑘-acceptable traversal.

Input
The first line contains two integers 𝑛 and 𝑚 (1≤𝑛≤16, 1≤𝑚≤104, 2≤𝑛𝑚) — the number of rows and the number of columns, respectively.

Each of the next 𝑛 lines contains 𝑚 integers (1≤𝑎𝑖,𝑗≤109) — the description of the matrix.

Output
Print a single integer 𝑘 — the maximum number such that there exists some order of rows of matrix 𝑎 that it produces an 𝑘-acceptable traversal.


Examples  
```
inputCopy  
4 2  
9 9  
10 8  
5 3  
4 3  
outputCopy  
5  
inputCopy  
2 4  
1 2 3 4  
10 3 7 3  
outputCopy  
0  
inputCopy  
6 1  
3  
6  
2  
5  
1  
4  
outputCopy  
3  
```
Note
In the first example you can rearrange rows as following to get the 5-acceptable traversal:

```
5 3  
10 8  
4 3  
9 9  
```
Then the sequence 𝑠 will be [5,10,4,9,3,8,3,9]. Each pair of neighbouring elements have at least 𝑘=5 difference between them.

In the second example the maximum 𝑘=0, any order is 0-acceptable.

In the third example the given order is already 3-acceptable, you can leave it as it is.
