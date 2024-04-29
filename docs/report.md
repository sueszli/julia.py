<!--
to compile this markdown file to a pdf, use the following command:

$ pandoc --read=markdown --write=latex --pdf-engine=xelatex --variable geometry:margin=10mm --variable documentclass:extarticle --variable fontsize:11pt --variable papersize:a4 --output=report.pdf report.md
-->

<!-- make sure to reference and label every table and figure. the labels must have reasonable names -->

_Submission Information:_

-   Name of authors: Pia Schwarzinger (12017370), Yahya Jabary (11912007)
-   Date: 2024-04-18
-   Course and assignment: Assignment 1, Basics of Parallel Computing 191.114, SS 2024
-   `GROUP_SIZE`: 2
-   `GROUP_NUMBER`: 13

# 1. The Tasks

## 1.1. Compute Speed-up and Parallel Efficiency for 2 Instance Sizes

_Speedup_

-   $\begin{aligned}S_a(n,p) = \frac{T_{\text{seq}}(n)}{T_{\text{par}}(n,p)}\end{aligned}$ = absolute speedup
-   $\begin{aligned}S_r(n,p) = \frac{T_{\text{par}}(n, 1)}{T_{\text{par}}(n,p)}\end{aligned}$ = relative speedup
-   What difference does parallelization make?
-   Where:
    -   $n$ = input size
    -   $p$ = number of processors
    -   $T_{\text{par}}(n,p)$ = parallel runtime
    -   $T_{\text{seq}}(n)$ = sequential runtime
-   Use the relative speedup when there isn't a sequential implementation

_Efficiency of Parallelization_

-   $\begin{aligned}E(n,p) = \frac{T_{\text{seq}}(n)}{p \cdot T_{\text{par}}(n,p)} = \frac{1}{p} \cdot S_a(n,p)\end{aligned}$
-   what difference does each processor make?

### Runtime and speed-up of parallel Julia set generator for $c_s$ case

_Table_

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

Keep in mind that while the speed-up was calculated using `p=1` as the reference point, the parallel efficiency was calculated using an average of the sequential runtime, by running the following commands 3 times on the Hydra-cluster and averaging the results:

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

Keep in mind that while the speed-up was calculated using `p=1` as the reference point, the parallel efficiency was calculated using an average of the sequential runtime, by running the following commands 3 times on the Hydra-cluster and averaging the results:

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

## A.1. System Information

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

## A.2. Raw Data

### `output_exp22_1.csv`

| size | patch | nprocs | time                |
| ---- | ----- | ------ | ------------------- |
| 155  | 26    | 1      | 0.27615245105698705 |
| 155  | 26    | 1      | 0.27596693905070424 |
| 155  | 26    | 1      | 0.2771365772932768  |
| 1100 | 26    | 1      | 13.435972596984357  |
| 1100 | 26    | 1      | 13.452274681068957  |
| 1100 | 26    | 1      | 13.371691829990596  |
| 155  | 26    | 2      | 0.14638189878314734 |
| 155  | 26    | 2      | 0.14576987363398075 |
| 155  | 26    | 2      | 0.1462678317911923  |
| 1100 | 26    | 2      | 6.670089309103787   |
| 1100 | 26    | 2      | 6.613465172238648   |
| 1100 | 26    | 2      | 6.7021133550442755  |
| 155  | 26    | 4      | 0.08490922581404448 |
| 155  | 26    | 4      | 0.08491231314837933 |
| 155  | 26    | 4      | 0.08519301796332002 |
| 1100 | 26    | 4      | 3.3561069620773196  |
| 1100 | 26    | 4      | 3.3553116391412914  |
| 1100 | 26    | 4      | 3.421122542116791   |
| 155  | 26    | 8      | 0.06856991816312075 |
| 155  | 26    | 8      | 0.06856326712295413 |
| 155  | 26    | 8      | 0.06828531296923757 |
| 1100 | 26    | 8      | 1.6898975907824934  |
| 1100 | 26    | 8      | 1.7937131081707776  |
| 1100 | 26    | 8      | 1.6963165369816124  |
| 155  | 26    | 16     | 0.07205457100644708 |
| 155  | 26    | 16     | 0.0730455950833857  |
| 155  | 26    | 16     | 0.07325727492570877 |
| 1100 | 26    | 16     | 0.9077705508098006  |
| 1100 | 26    | 16     | 0.9078279393725097  |
| 1100 | 26    | 16     | 0.9103577299974859  |
| 155  | 26    | 24     | 0.0845845378935337  |
| 155  | 26    | 24     | 0.08471266506239772 |
| 155  | 26    | 24     | 0.08427527407184243 |
| 1100 | 26    | 24     | 0.656599803827703   |
| 1100 | 26    | 24     | 0.6573387430980802  |
| 1100 | 26    | 24     | 0.6497617312707007  |
| 155  | 26    | 32     | 0.0973281990736723  |
| 155  | 26    | 32     | 0.09837603475898504 |
| 155  | 26    | 32     | 0.09687442006543279 |
| 1100 | 26    | 32     | 0.5734831769950688  |
| 1100 | 26    | 32     | 0.5541784320957959  |
| 1100 | 26    | 32     | 0.565086467191577   |

### `output_exp22_2.csv`

| size | patch | nprocs | time                |
| ---- | ----- | ------ | ------------------- |
| 155  | 26    | 1      | 0.392238802742213   |
| 155  | 26    | 1      | 0.39877972193062305 |
| 155  | 26    | 1      | 0.3912382051348686  |
| 1100 | 26    | 1      | 19.34426457900554   |
| 1100 | 26    | 1      | 18.90565126761794   |
| 1100 | 26    | 1      | 19.064889647066593  |
| 155  | 26    | 2      | 0.20706806099042296 |
| 155  | 26    | 2      | 0.20968409720808268 |
| 155  | 26    | 2      | 0.2159389308653772  |
| 1100 | 26    | 2      | 9.65854894882068    |
| 1100 | 26    | 2      | 9.758664200082421   |
| 1100 | 26    | 2      | 9.597689433023334   |
| 155  | 26    | 4      | 0.12078673578798771 |
| 155  | 26    | 4      | 0.12187985517084599 |
| 155  | 26    | 4      | 0.12278737686574459 |
| 1100 | 26    | 4      | 4.8538289330899715  |
| 1100 | 26    | 4      | 4.949722504708916   |
| 1100 | 26    | 4      | 4.896979348734021   |
| 155  | 26    | 8      | 0.08609647722914815 |
| 155  | 26    | 8      | 0.08687825128436089 |
| 155  | 26    | 8      | 0.0856924457475543  |
| 1100 | 26    | 8      | 2.4588615149259567  |
| 1100 | 26    | 8      | 2.4403636367060244  |
| 1100 | 26    | 8      | 2.4585742950439453  |
| 155  | 26    | 16     | 0.08432547515258193 |
| 155  | 26    | 16     | 0.08534767106175423 |
| 155  | 26    | 16     | 0.08608504896983504 |
| 1100 | 26    | 16     | 1.2857805700041354  |
| 1100 | 26    | 16     | 1.28942183079198    |
| 1100 | 26    | 16     | 1.2837325409054756  |
| 155  | 26    | 24     | 0.09584450582042336 |
| 155  | 26    | 24     | 0.09703108435496688 |
| 155  | 26    | 24     | 0.09624077333137393 |
| 1100 | 26    | 24     | 0.9055881663225591  |
| 1100 | 26    | 24     | 0.8943913546390831  |
| 1100 | 26    | 24     | 0.9012130876071751  |
| 155  | 26    | 32     | 0.10889460984617472 |
| 155  | 26    | 32     | 0.10903614293783903 |
| 155  | 26    | 32     | 0.1076613599434495  |
| 1100 | 26    | 32     | 0.7539521278813481  |
| 1100 | 26    | 32     | 0.7489344119094312  |
| 1100 | 26    | 32     | 0.7355474359355867  |

### `output_exp23.csv`

| size | patch | nprocs | time               |
| ---- | ----- | ------ | ------------------ |
| 950  | 1     | 32     | 60.38315498735756  |
| 950  | 1     | 32     | 58.993379454128444 |
| 950  | 1     | 32     | 59.664796941913664 |
| 950  | 5     | 32     | 2.4295669128187    |
| 950  | 5     | 32     | 2.457375079859048  |
| 950  | 5     | 32     | 2.430592040065676  |
| 950  | 10    | 32     | 0.8235339601524174 |
| 950  | 10    | 32     | 0.8456530389375985 |
| 950  | 10    | 32     | 0.8123667249456048 |
| 950  | 20    | 32     | 0.592178599908948  |
| 950  | 20    | 32     | 0.5885163000784814 |
| 950  | 20    | 32     | 0.5882865060120821 |
| 950  | 55    | 32     | 0.640842576045543  |
| 950  | 55    | 32     | 0.6622877516783774 |
| 950  | 55    | 32     | 0.6463527246378362 |
| 950  | 150   | 32     | 1.804339012131095  |
| 950  | 150   | 32     | 1.7855969751253724 |
| 950  | 150   | 32     | 1.7837719358503819 |
| 950  | 400   | 32     | 5.342996523249894  |
| 950  | 400   | 32     | 5.354430069215596  |
| 950  | 400   | 32     | 5.3442102540284395 |

### `output_exp24.csv`

| size | patch | nprocs | time               |
| ---- | ----- | ------ | ------------------ |
| 800  | 1     | 16     | 51.77733509801328  |
| 800  | 1     | 16     | 48.679752216208726 |
| 800  | 1     | 16     | 49.604969315230846 |
| 800  | 2     | 16     | 12.208631441928446 |
| 800  | 2     | 16     | 12.400218938011676 |
| 800  | 2     | 16     | 12.67593849496916  |
| 800  | 3     | 16     | 5.231156553607434  |
| 800  | 3     | 16     | 5.173088782932609  |
| 800  | 3     | 16     | 5.30134785734117   |
| 800  | 4     | 16     | 2.795454104896635  |
| 800  | 4     | 16     | 2.8061751988716424 |
| 800  | 4     | 16     | 2.743914455641061  |
| 800  | 5     | 16     | 1.7844559531658888 |
| 800  | 5     | 16     | 1.795137454289943  |
| 800  | 5     | 16     | 1.754671474918723  |
| 800  | 6     | 16     | 1.2681594076566398 |
| 800  | 6     | 16     | 1.2242525001056492 |
| 800  | 6     | 16     | 1.2942032269202173 |
| 800  | 7     | 16     | 1.0078809931874275 |
| 800  | 7     | 16     | 1.0316235939972103 |
| 800  | 7     | 16     | 1.0379106737673283 |
| 800  | 8     | 16     | 0.8636039649136364 |
| 800  | 8     | 16     | 0.8836448309011757 |
| 800  | 8     | 16     | 0.8675666828639805 |
| 800  | 9     | 16     | 0.8217232823371887 |
| 800  | 9     | 16     | 0.8141451748088002 |
| 800  | 9     | 16     | 0.8879383755847812 |
| 800  | 10    | 16     | 0.8032627403736115 |
| 800  | 10    | 16     | 0.790965499356389  |
| 800  | 10    | 16     | 0.7719701924361289 |
| 800  | 11    | 16     | 0.775052934885025  |
| 800  | 11    | 16     | 0.7863136758096516 |
| 800  | 11    | 16     | 0.7699855691753328 |
| 800  | 12    | 16     | 0.7268759598955512 |
| 800  | 12    | 16     | 0.7416912410408258 |
| 800  | 12    | 16     | 0.7239395705983043 |
| 800  | 13    | 16     | 0.7274400270543993 |
| 800  | 13    | 16     | 0.7136987750418484 |
| 800  | 13    | 16     | 0.7242374992929399 |
| 800  | 14    | 16     | 0.7333642770536244 |
| 800  | 14    | 16     | 0.7298130737617612 |
| 800  | 14    | 16     | 0.7357385512441397 |
| 800  | 15    | 16     | 0.7113026860170066 |
| 800  | 15    | 16     | 0.7115092552267015 |
| 800  | 15    | 16     | 0.7147729960270226 |
| 800  | 16    | 16     | 0.7343269921839237 |
| 800  | 16    | 16     | 0.7277633068151772 |
| 800  | 16    | 16     | 0.7470175549387932 |
| 800  | 17    | 16     | 0.7087195003405213 |
| 800  | 17    | 16     | 0.7273335340432823 |
| 800  | 17    | 16     | 0.7066979217343032 |
| 800  | 18    | 16     | 0.7008385430090129 |
| 800  | 18    | 16     | 0.7211737250909209 |
| 800  | 18    | 16     | 0.7053795196115971 |
| 800  | 19    | 16     | 0.704965204000473  |
| 800  | 19    | 16     | 0.7185817346908152 |
| 800  | 19    | 16     | 0.7119517708197236 |
| 800  | 20    | 16     | 0.7045390028506517 |
| 800  | 20    | 16     | 0.7090244409628212 |
| 800  | 20    | 16     | 0.6993431178852916 |
| 800  | 21    | 16     | 0.7067825132980943 |
| 800  | 21    | 16     | 0.7152607310563326 |
| 800  | 21    | 16     | 0.7141714952886105 |
| 800  | 22    | 16     | 0.7289159940555692 |
| 800  | 22    | 16     | 0.7070880490355194 |
| 800  | 22    | 16     | 0.7090400322340429 |
| 800  | 23    | 16     | 0.7122855372726917 |
| 800  | 23    | 16     | 0.7262964779511094 |
| 800  | 23    | 16     | 0.7180132349021733 |
| 800  | 24    | 16     | 0.7030764939263463 |
| 800  | 24    | 16     | 0.7233439306728542 |
| 800  | 24    | 16     | 0.7046146122738719 |
| 800  | 25    | 16     | 0.7067729285918176 |
| 800  | 25    | 16     | 0.7068284871056676 |
| 800  | 25    | 16     | 0.7069635195657611 |
| 800  | 26    | 16     | 0.7092408840544522 |
| 800  | 26    | 16     | 0.7142819189466536 |
| 800  | 26    | 16     | 0.7060380070470273 |
| 800  | 27    | 16     | 0.7240377422422171 |
| 800  | 27    | 16     | 0.703698709141463  |
| 800  | 27    | 16     | 0.7189373909495771 |
| 800  | 28    | 16     | 0.7107441178523004 |
| 800  | 28    | 16     | 0.7102009649388492 |
| 800  | 28    | 16     | 0.7038759361021221 |
| 800  | 29    | 16     | 0.7044810829684138 |
| 800  | 29    | 16     | 0.7004124890081584 |
| 800  | 29    | 16     | 0.7011993718333542 |
| 800  | 30    | 16     | 0.7012511510401964 |
| 800  | 30    | 16     | 0.7043010322377086 |
| 800  | 30    | 16     | 0.7103770151734352 |
