Computational Support for "An Approach to the Collatz Conjecture via Inductive Inequality and Modular Equidistribution"
This repository contains the Python code used to generate the computational evidence and statistical results presented in the manuscript.

Contents
collatz_simulations.py: The main Python script that performs the Collatz sequence simulations, calculates visit proportions to residue classes modulo 4, and computes the average exponents $\bar{k}_n$.
Requirements
The code uses standard Python libraries: - math - random - decimal - datetime - subprocess

No special installations are required beyond a standard Python 3 environment.

Usage
Clone this repository or download the collatz_simulations.py file.
Run the script from the command line: ```bash python collatz_simulations.py ```
The script will output results to a text file with a timestamped filename.
Description of Key Functions
The script models the Collatz process as a Markov chain on $\mathbb{Z}/4\mathbb{Z}$.
It runs multiple experiments with large random numbers ($> 2^{60}$) to empirically verify the stationary distribution $\mu = (\frac{1}{3}, \frac{1}{6}, \frac{1}{3}, \frac{1}{6})$.
It also includes a "Quasi-Fibonacci" model for comparative analysis.
Results
The output file contains the proportions of visits to each residue class and the computed limit of the sequences, matching the theoretical predictions presented in the paper.

Contact
For any questions regarding this code, please contact the corresponding author: denitox@proton.me
