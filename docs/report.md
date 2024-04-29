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
| 155  | 1   | 0.276419         | 1        | 1.42473   |
| 155  | 2   | 0.14614          | 1.89147  | 1.34742   |
| 155  | 4   | 0.0850049        | 3.2518   | 1.15824   |
| 155  | 8   | 0.0684728        | 4.03691  | 0.71894   |
| 155  | 16  | 0.0727858        | 3.7977   | 0.338169  |
| 155  | 24  | 0.0845242        | 3.27029  | 0.194137  |
| 155  | 32  | 0.0975262        | 2.8343   | 0.126191  |
| 1100 | 1   | 13.42            | 1        | 1.40137   |
| 1100 | 2   | 6.66189          | 2.01444  | 1.41149   |
| 1100 | 4   | 3.37751          | 3.97333  | 1.39203   |
| 1100 | 8   | 1.72664          | 7.7723   | 1.36149   |
| 1100 | 16  | 0.908652         | 14.7691  | 1.29356   |
| 1100 | 24  | 0.654567         | 20.5021  | 1.19713   |
| 1100 | 32  | 0.564249         | 23.7838  | 1.04156   |

keep in mind that while the speed-up was calculated using `p=1` as the reference point, the parallel efficiency was calculated using an average of the sequential runtime, by running the following commands 3 times and averaging the results:

```bash
srun -p q_student -t 1 -N 1 -c 32 python3 julia.py --size 155 --nprocs 1 # 155;20;1;0.39382300106808543
srun -p q_student -t 1 -N 1 -c 32 python3 julia.py --size 1100 --nprocs 1 # 1100;20;1;18.806384983938187
```

### Runtime and speed-up of parallel Julia set generator for $c_b$ case

_table_

| size | p   | mean runtime (s) | speed-up | par. eff. |
| ---- | --- | ---------------- | -------- | --------- |
| 155  | 1   | 0.394086         | 1        | 0.711286  |
| 155  | 2   | 0.210897         | 1.86862  | 0.66456   |
| 155  | 4   | 0.121818         | 3.23504  | 0.575259  |
| 155  | 8   | 0.0862224        | 4.57057  | 0.406373  |
| 155  | 16  | 0.0852527        | 4.62256  | 0.205497  |
| 155  | 24  | 0.0963721        | 4.08921  | 0.121191  |
| 155  | 32  | 0.108531         | 3.6311   | 0.0807109 |
| 1100 | 1   | 19.1049          | 1        | 0.68691   |
| 1100 | 2   | 9.67163          | 1.97536  | 0.678447  |
| 1100 | 4   | 4.90018          | 3.89883  | 0.669536  |
| 1100 | 8   | 2.4526           | 7.78967  | 0.66885   |
| 1100 | 16  | 1.28631          | 14.8525  | 0.637646  |
| 1100 | 24  | 0.900398         | 21.2183  | 0.607295  |
| 1100 | 32  | 0.746145         | 25.6049  | 0.549633  |

keep in mind that while the speed-up was calculated using `p=1` as the reference point, the parallel efficiency was calculated using an average of the sequential runtime, by running the following commands 3 times and averaging the results:

```bash
srun -p q_student -t 1 -N 1 -c 32 python3 julia.py --size 155 --nprocs 1 --benchmark # 155;20;1;0.2803074959665537
srun -p q_student -t 1 -N 1 -c 32 python3 julia.py --size 1100 --nprocs 1 --benchmark # 1100;20;1;13.123375411145389
```

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

# Appendix

System stats:

```plaintext
bopc23s9@hydra-head:~$ lscpu

Architecture:                    x86_64
CPU op-mode(s):                  32-bit, 64-bit
Byte Order:                      Little Endian
Address sizes:                   46 bits physical, 48 bits virtual
CPU(s):                          16
On-line CPU(s) list:             0-15
Thread(s) per core:              1
Core(s) per socket:              16
Socket(s):                       1
NUMA node(s):                    1
Vendor ID:                       GenuineIntel
CPU family:                      6
Model:                           85
Model name:                      Intel(R) Xeon(R) Gold 6130 CPU @ 2.10GHz
Stepping:                        4
CPU MHz:                         1000.151
CPU max MHz:                     3700.0000
CPU min MHz:                     1000.0000
BogoMIPS:                        4200.00
L1d cache:                       512 KiB
L1i cache:                       512 KiB
L2 cache:                        16 MiB
L3 cache:                        22 MiB
NUMA node0 CPU(s):               0-15
Vulnerability Itlb multihit:     KVM: Mitigation: VMX unsupported
Vulnerability L1tf:              Mitigation; PTE Inversion
Vulnerability Mds:               Mitigation; Clear CPU buffers; SMT disabled
Vulnerability Meltdown:          Mitigation; PTI
Vulnerability Mmio stale data:   Mitigation; Clear CPU buffers; SMT disabled
Vulnerability Retbleed:          Mitigation; IBRS
Vulnerability Spec store bypass: Mitigation; Speculative Store Bypass disabled via prctl and seccomp
Vulnerability Spectre v1:        Mitigation; usercopy/swapgs barriers and __user pointer sanitization
Vulnerability Spectre v2:        Mitigation; IBRS, IBPB conditional, RSB filling, PBRSB-eIBRS Not affected
Vulnerability Srbds:             Not affected
Vulnerability Tsx async abort:   Mitigation; Clear CPU buffers; SMT disabled
Flags:                           fpu vme de pse tsc msr pae mce cx8 apic sep mtrr pge mca cmov pat pse36 clflush dts ac
                                 pi mmx fxsr sse sse2 ss ht tm pbe syscall nx pdpe1gb rdtscp lm constant_tsc art arch_p
                                 erfmon pebs bts rep_good nopl xtopology nonstop_tsc cpuid aperfmperf pni pclmulqdq dte
                                 s64 monitor ds_cpl smx est tm2 ssse3 sdbg fma cx16 xtpr pdcm pcid dca sse4_1 sse4_2 x2
                                 apic movbe popcnt tsc_deadline_timer aes xsave avx f16c rdrand lahf_lm abm 3dnowprefet
                                 ch cpuid_fault epb cat_l3 cdp_l3 invpcid_single pti intel_ppin ssbd mba ibrs ibpb stib
                                 p fsgsbase tsc_adjust bmi1 hle avx2 smep bmi2 erms invpcid rtm cqm mpx rdt_a avx512f a
                                 vx512dq rdseed adx smap clflushopt clwb intel_pt avx512cd avx512bw avx512vl xsaveopt x
                                 savec xgetbv1 xsaves cqm_llc cqm_occup_llc cqm_mbm_total cqm_mbm_local dtherm ida arat
                                  pln pts hwp hwp_act_window hwp_epp hwp_pkg_req pku ospke md_clear flush_l1d
```
