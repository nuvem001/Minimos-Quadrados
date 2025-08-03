# IMPLEMENTATION OF THE LEAST SQUARES METHOD FOR LINEAR ADJUSTMENT
# Numerical Methods Implementation Report

## 1. Introduction
### 1.1 Context and Objectives
The least squares method is widely used in engineering and sciences to fit linear models to experimental data. This work aims to:
- Implement a multivariate linear adjustment (variables x₁, x₂) without ready-made libraries
- Numerically validate the results
- Document the process according to technical standards

## 2. Methodology
### 2.1 Mathematical Model
The adjusted model is:

y = β₀ + β₁x₁ + β₂x₂

where:
- β₀, β₁, β₂ are coefficients to be determined
- x₁, x₂ are independent variables (e.g., parents' heights)
- y is the dependent variable (e.g., daughter's height)

### 2.2 Normal System
The linear system Aβ = b is derived.

### 2.3 Implemented Algorithms
1. **Normal System Assembly**:
   - Direct sum calculation
2. **Gaussian Elimination with Pivoting**:
   - Partial pivoting for stability (Chapra, Ch. 9)
   - Back substitution to solve the triangular system

## 3. Implementation
### 3.1 Code Structure
Modules:
- `gaussian_elimination.py`: Linear system solver
- `least_squares.py`: Normal system calculation
- `main.py`: User interface

### 3.2 Flowchart
1. Read data (x₁, x₂, y)
2. Assemble A and b
3. Solve system via Gaussian Elimination
4. Output coefficients β

## 4. Results and Discussion
### 4.1 File 1 Adjustment
Least squares solution:

β₀ = 0.466880
β₁ = 0.367032
β₂ = 0.305567

Adjusted equation:

y = 0.466880 + 0.367032*x₁ + 0.305567*x₂

### 4.2 File 2 Adjustment
Least squares solution:

β₀ = 0.589870
β₁ = 0.339350
β₂ = 0.360755

Adjusted equation:

y = 0.589870 + 0.339350*x₁ + 0.360755*x₂

## References
1. CAMPOS, F. F. *Algoritmos Numéricos*. 2nd ed. Belo Horizonte: UFMG, 2007.
2. CHAPRA, S. C.; CANALE, R. P. *Numerical Methods for Engineers*. 7th ed. New York: McGraw-Hill Education, 2015. 926 p. ISBN 978-0-07-339792-4.
