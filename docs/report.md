<!--
to compile this markdown file to a pdf, use the following command:

$ pandoc --read=markdown --write=latex --pdf-engine=xelatex --variable geometry:margin=10mm --variable documentclass:extarticle --variable fontsize:11pt --variable papersize:a4 --output=report.pdf report.md
-->

_Submission Information:_

-   Name of authors: Pia Schwarzinger (12017370), Yahya Jabary (11912007)
-   Date: 2024-04-18
-   Course and assignment: Assignment 1, Basics of Parallel Computing 191.114, SS 2024
-   `GROUP_SIZE`: 2
-   `GROUP_NUMBER`: 13

# 1. The Tasks

## 1.1. Compute Speed-up and Parallel Efficiency for 2 Instance Sizes

### Runtime and speed-up of parallel Julia set generator for $c_s$ case

_speedup_

-   $\begin{aligned}S_a(n,p) = \frac{T_{\text{seq}}(n)}{T_{\text{par}}(n,p)}\end{aligned}$ = absolute speedup
-   $\begin{aligned}S_r(n,p) = \frac{T_{\text{par}}(n, 1)}{T_{\text{par}}(n,p)}\end{aligned}$ = relative speedup
-   what difference does parallelization make?
-   where:
    -   $n$ = input size
    -   $p$ = number of processors
    -   $T_{\text{par}}(n,p)$ = parallel runtime
    -   $T_{\text{seq}}(n)$ = sequential runtime
-   use the relative speedup when there isn't a sequential implementation

_efficiency of parallelization_

-   $\begin{aligned}E(n,p) = \frac{T_{\text{seq}}(n)}{p \cdot T_{\text{par}}(n,p)} = \frac{1}{p} \cdot S_a(n,p)\end{aligned}$
-   what difference does each processor make?

_table_

| size | p   | mean runtime (s) | speed-up | par. eff. |
| ---- | --- | ---------------- | -------- | --------- |
| 155  | 1   | 0.276419         | 1        | 1         |
| 155  | 2   | 0.14614          | 1.89147  | 0.945733  |
| 155  | 4   | 0.0850049        | 3.2518   | 0.81295   |
| 155  | 8   | 0.0684728        | 4.03691  | 0.504614  |
| 155  | 16  | 0.0727858        | 3.7977   | 0.237356  |
| 155  | 24  | 0.0845242        | 3.27029  | 0.136262  |
| 155  | 32  | 0.0975262        | 2.8343   | 0.0885719 |
| 1100 | 1   | 13.42            | 1        | 1         |
| 1100 | 2   | 6.66189          | 2.01444  | 1.00722   |
| 1100 | 4   | 3.37751          | 3.97333  | 0.993333  |
| 1100 | 8   | 1.72664          | 7.7723   | 0.971537  |
| 1100 | 16  | 0.908652         | 14.7691  | 0.923069  |
| 1100 | 24  | 0.654567         | 20.5021  | 0.854253  |
| 1100 | 32  | 0.564249         | 23.7838  | 0.743243  |

### Runtime and speed-up of parallel Julia set generator for $c_b$ case

_table_

| size | p   | mean runtime (s) | speed-up | par. eff. |
| ---- | --- | ---------------- | -------- | --------- |
| 155  | 1   | 0.394086         | 1        | 1         |
| 155  | 2   | 0.210897         | 1.86862  | 0.934308  |
| 155  | 4   | 0.121818         | 3.23504  | 0.808759  |
| 155  | 8   | 0.0862224        | 4.57057  | 0.571321  |
| 155  | 16  | 0.0852527        | 4.62256  | 0.28891   |
| 155  | 24  | 0.0963721        | 4.08921  | 0.170384  |
| 155  | 32  | 0.108531         | 3.6311   | 0.113472  |
| 1100 | 1   | 19.1049          | 1        | 1         |
| 1100 | 2   | 9.67163          | 1.97536  | 0.987679  |
| 1100 | 4   | 4.90018          | 3.89883  | 0.974706  |
| 1100 | 8   | 2.4526           | 7.78967  | 0.973708  |
| 1100 | 16  | 1.28631          | 14.8525  | 0.928281  |
| 1100 | 24  | 0.900398         | 21.2183  | 0.884097  |
| 1100 | 32  | 0.746145         | 25.6049  | 0.800152  |

## 1.2. Influence of Patch Size

## 1.3. Finding the Best Patch Size

# 2. Speed-up Analysis

Comparing two sorting algorithms:

-   Algorithm 1: $T_{par}^{\mathcal{A}_1}(n,p)=\mathcal{O}(\frac{n\log n}p+\log n)$
-   Algorithm 2: $T_{par}^{\mathcal{A}_2}(n,p)=\mathcal{O}(\frac{n\log n}p+n)$

The best runtime for a sequential implementation is in $T_{\text{seq}^*}(n) = \mathcal{O}(n \log n)$.

_the absolute speed-up of algorithm 1_

_the absolute speed-up of algorithm 2_

# 3. Weak Scaling Analysis
