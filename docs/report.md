<!--
to compile this markdown file to a pdf, use the following command:

$ pandoc --read=markdown --write=latex --output=report.pdf --pdf-engine=xelatex --variable geometry:margin=20mm --variable documentclass:extarticle --variable fontsize:11pt report.md
-->

**Group 13:** Pia Schwarzinger (12017370), Yahya Jabary (11912007)

# 1. The Tasks

## 1.1. Compute Speed-up and Parallel Efficiency for 2 Instance Sizes

Runtime and speed-up of parallel Julia set generator for $c_s$ case.

| size | p        | mean runtime (s) | speed-up | par. eff. |
| ---- | -------- | ---------------- | -------- | --------- |
| 155  | 1        | 4.3              | fill     | fill      |
|      | $\vdots$ |                  | ..       | ..        |
| 155  | 32       | 5.1              |          |           |
| 1100 | 1        | 6.3              |          |           |
|      | $\vdots$ |                  |          |           |
| 1100 | 32       | 6.1              |          |           |

Runtime and speed-up of parallel Julia set generator for $c_b$ case.

| size | p        | mean runtime (s) | speed-up | par. eff. |
| ---- | -------- | ---------------- | -------- | --------- |
| 155  | 1        | 4.3              | fill     | fill      |
|      | $\vdots$ |                  | ..       | ..        |
| 155  | 32       | 5.1              |          |           |
| 1100 | 1        | 6.3              |          |           |
|      | $\vdots$ |                  |          |           |
| 1100 | 32       | 6.1              |          |           |

Tables above show the runtime measurements and the respective speed-up and efficiency values for the cases $c_s$ and $c_b$.

## 1.2. Influence of Patch Size

## 1.3. Finding the Best Patch Size

# 2. Speed-up Analysis

# 3. Weak Scaling Analysis

# 4. Conclusion
