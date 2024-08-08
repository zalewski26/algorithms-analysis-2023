# Analysis of Algorithms

This repository contains the projects and assignments completed as part of the Analysis of Algorithms course at the Wrocław University of Science and Technology. The projects span various topics related to algorithms, including leader election, approximate counting, probabilistic data structures, and blockchain analysis. Each task is described in detail below:

## Leader Election

### Task 1
- Implement a simulator that allows testing the leader election algorithm for a known number of nodes $n$ (second scenario) and for a known upper limit $u$ on the number of nodes $n$ (third scenario). You can use any programming language.

### Task 2
- Let the random variable $L$ denote the number of slots required to start the leader election algorithm. Using the simulator from the previous task, draw the empirical distribution (histogram) of the random variable $L$ for both considered scenarios. For the scenario with a known upper limit $u$, consider three cases: $n = 2$, $n = u/2$, and $n = u$. Justify the results.

### Task 3
- For the scenario with a known number of nodes $n$, use the simulator to estimate the expected value $E[L]$ and variance $\text{Var}[L]$. Check if the results agree with the theoretical outcomes.

### Task 4
- Consider the scenario with a known upper limit $u$. According to the notation introduced in the lecture materials, let $S_{L,n}$ denote the event that in one round of the algorithm with duration $L = \lceil \log_2 u \rceil$, the leader election is successful if there is exactly one leader. Design appropriate experiments and, using simulations, verify the correctness of Theorem 1 from the lecture materials: $\Pr[S_{L,n}] \geq \lambda \approx 0.579$.

## MinCount

### Task 5
- Implement the MinCount algorithm $\text{MinCount}(k, h, \mathcal{M})$ and test its operation:

  a) Consider a multiset $\mathcal{M}_n = (S_n, m)$ such that $|S_n| = n$ for $n = 1, 2, \ldots, n$, and all elements $S_n$ are disjoint. How does the function $h$ change in relation to the estimated value $\hat{n}$ used in the algorithm?

  b) For $k = 2, 3, 10, 100, 400$ and multisets from point a), draw graphs with the value of $n$ on the horizontal axis and the value of the ratio $\hat{n}/n$ on the vertical axis.

  c) Experimentally adjust the value of $k$ so that in 95% of cases $\left| \frac{\hat{n}}{n} - 1 \right| < 10\%$.

### Task 6
- For several different hash functions $h: S \to \{0, 1\}^B$ and different values of the parameter $B$, test the operation of the MinCount algorithm $\text{MinCount}(k, h, \mathcal{M})$. Try to find a hash function $h$ for which the algorithm works much worse and explain what could result in worse accuracy. Consider the case when $S = [10^6]$.

### Task 7
- Your task is to compare the theoretical results on the concentration of the estimator $\hat{n}$ used in the MinCount algorithm $\text{MinCount}(k, h, \mathcal{M})$ obtained by Chernoff's and Chebyshev's inequalities with the results of simulations. For $n = 1, 2, \ldots, 100, k = 400$ and $\delta = 5\%, 10\%, 25\%$, plot graphs of $\hat{n}/n$ (obtained experimentally) for values $1 - \delta$ and $1 + \delta$, for which

$$
\Pr \left[ 1 - \delta < \frac{\hat{n}}{n} < 1 + \delta \right] > 1 - \alpha.
$$

## HyperLogLog

### Task 8
- Implement the HyperLogLog algorithm with corrections and test its operation for different values of the parameter $m$ (number of registers) and different hash functions. Create plots analogous to those in Task 5. Compare the accuracy of the MinCount and HyperLogLog algorithms when both have the same amount of memory available (you can assume that 5 bits are needed per register in HyperLogLog and 32 bits per hash value in MinCount).

## Blockchain

### Task 9
- Let $0 < q < 1/2$ denote the probability that the adversary will mine the next block despite having a fraction of the computational power $q$ in their possession. Let $n$ denote the number of confirmations (overbuilt blocks) needed to consider the transaction confirmed. Let $P(n, q)$ denote the probability that an adversary with power $q$ will possess a blockchain of length at least equal to the honest users' chain, in which $n$ blocks were mined containing the considered transaction and $n$ blocks were mined later.

  a) Compare the formulas for $P(n, q)$ obtained by Nakamoto and Grunspan. Specifically:
     - Let $n = 1, 3, 6, 12, 24, 48$ and plot $P(n, q)$ as a function of $q$,
     - Determine the allowable probability of the adversary's success $P(n, q) = 0.1\%, 1\%, 10\%$ and plot the corresponding values by adjusting $n$ based on $q$.

  b) Implement a "double spending" attack simulator that will experimentally approximate the probability of the event $P(n, q)$ as a function of $n$ and $q$. 
     - Hint: Design an experiment and repeat it multiple times (Monte Carlo method). Carefully and accurately describe the operation and code of the simulator.

  c) Compare the simulator results with the analytical results (plots). If discrepancies arise, try to explain them.

## Self-Stabilization

### Task 10
- Implement a simulator for Dijkstra's Mutual Exclusion algorithm. For a fixed $n$ denoting the number of processes in a ring, verify that starting from any initial configuration, the algorithm will reach a legal configuration. If certain configurations can be reached in a few possible configurations, determine which one happens first, each execution should be verified. What is the largest number of steps until a legal configuration is reached for a fixed $n$? For what values of $n$ can a configuration be reached in the shortest time? For this task, you need to achieve $3 \times N$ points, where $N$ denotes the largest value of $n$ for which you verified the algorithm.

### Task 11
- Consider a graph $G = (V, E)$. Two vertices $v, w \in V$ are independent if $\{v, w\} \notin E$. A subset $S \subseteq V$ of vertices is independent if all its elements are pairwise independent. Using the Maximal Matching algorithm discussed in the lecture, propose, implement, and test a self-stabilizing algorithm to find a maximal independent set in an undirected graph. Provide convincing arguments for the correctness of the algorithm (formally, this is the task for the exercise). Algorithms for finding maximal independent sets have applications in frequency assignment problems in wireless networks.

## Markov Chains

### Task 12
- For a given directed graph $G$ with $n$ vertices, define the Google matrix $M_G$ as:

$$
M_G = (1 - \alpha) P_G + \frac{\alpha}{n} J_n,
$$

where $P_G$ is a stochastic matrix of size $n \times n$ describing the transition probabilities between the vertices of the graph $G$, $J_n$ is an $n \times n$ matrix of all ones, and $\alpha \in [0, 1]$ is the damping factor. The graph below shows the connection scheme between six websites. Calculate the stationary distribution for the Markov chain associated with the matrix $M_G$ for $\alpha = 0, 0.15, 0.5, 1$. What happens if the connection between states 2 and 3 is removed? What is the stationary distribution of the matrix $\frac{1}{2} I_n + \frac{1}{2} P_G$? Why is it sometimes called the boredom coefficient?

### Task 13
- Consider a Markov chain with the state space $\{0, 1, 2, 3\}$ and the transition matrix

$$
P = \begin{pmatrix}
0 & 3/10 & 1/10 & 6/10 \\
1/10 & 7/10 & 2/10 & 0 \\
4/10 & 0 & 6/10 & 0 \\
0 & 2/10 & 3/10 & 5/10
\end{pmatrix}
$$

  a) Find the stationary distribution $\pi = (\pi_0, \pi_1, \pi_2, \pi_3)$ for this Markov chain.
  b) Find the probability of being in state 3 after 30 steps, starting from state 0.
  c) Find the probability of being in state 3 after 128 steps, starting from state 0. How many steps does it take to get to within $\epsilon = 0.01$ of the stationary distribution?
  d) Find the value of $\delta$ for which $\left|P_{ij}^n - \pi_j\right| \leq \epsilon$ for all $i, j$ and $n \geq \delta$.

### Task 14
- Assume we have a Markov chain described by the Google matrix $M_G$ defined in formula (1), where the adjacency matrix of the directed graph $G$ is

$$
N_G = \begin{pmatrix}
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 1 & 0 \\
1 & 0 & 0 & 1 & 0 \\
0 & 1 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 & 0
\end{pmatrix}
$$

and $\vec{\pi}_0 = (1/5, 1/5, 1/5, 1/5, 1/5)$ is the initial distribution of the chain states. Check what the distribution will be after the next 25 steps $(\alpha = 0, 1/4, 1/2, 3/4, 1)$. How does the parameter $\alpha$ affect the convergence time to the stationary distribution? Does the value of the parameter $\alpha$ affect the ranking of pages in the PageRank algorithm? Draw the plots.

## Generating Functions

### Task 15
- By setting up the appropriate recurrence relation and using the generating function, find the number of lines of code executed in the following algorithm. Verify your answer experimentally.

```cpp
int f(int n) {
    int s = 0;
    if (n == 0) then return 1;
    else 
        for (int i = 0; i < n; i++) do
            s += f(i);
        end for
    return s;
end if
}