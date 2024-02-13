# Analysis of Algorithms

Efficiency of an algorithm can be analyzed at two different stages, before implementation and after implementation. They are the following.

## 1. A Priori Analysis

This is a theoretical analysis of an algorithm. Efficiency of an algorithm is measured by assuming that all other factors, for example, processor speed, are constant and have no effect on the implementation.

## 2. A Posteriori Analysis

This is an empirical analysis of an algorithm. The selected algorithm is implemented using programming language. This is then executed on target computer machine. In this analysis, actual statistics like running time and space required, are collected.

## Asymptotic Analysis

Defining mathematical boundation of run-time performance. It is input bound, and if there is no input it is constant.

Asymptotic analysis refers to computing the running time of any operation in mathematical units of computation. For example, the running time of one operation is computed as f(n) and may be for another operation it is computed as g(n2). This means the first operation running time will increase linearly with the increase in n and the running time of the second operation will increase exponentially when n increases. Similarly, the running time of both operations will be nearly the same if n is significantly small.

Usually, the time required by an algorithm falls under three types

### 1. Best Case

Minimum time required for program execution.

### 2. Average Case

Average time required for program execution.

### 3. Worst Case

Maximum time required for program execution.

## Asymptotic Notations

### Big O Notations

Big O describes the performance of an algorithm. It checks whether the algorithm is scalable when input grows very large.
**Notation:** O(n)

### Omega Notation

Expresses lower bound of an algorithm, measures best case.

### Theta Notation &theta;

Express both lower and upper bound.

## Common Asymptotic Notations

<table>
    <thead>
        <th>Name</th>
        <th>Notation</th>
    </thead>
    <tbody>
        <tr>
            <td>Constant</td>
            <td>0 (1)</td>
        </tr>
        <tr>
            <td>logarithmic</td>
            <td>O (log n)</td>
        </tr>
        <tr>
            <td>linear</td>
            <td>O (n)</td>
        </tr>
        <tr>
            <td>n log n</td>
            <td>O (n log n)</td>
        </tr>
         <tr>
            <td>quadratic</td>
            <td>O (n<sup>2</sup>)</td>
        </tr>
         <tr>
            <td>cubic</td>
            <td>O (n<sup>3</sup>)</td>
        </tr>
         <tr>
            <td>polynomial</td>
            <td>n<sup>O(1)</sup></td>
        </tr>
         <tr>
            <td>exponential</td>
            <td>O(2<sup>n</sup>)</td>
        </tr>
    </tbody>
</table>

## Time Complexity

- **Definition**: Quantifies the time an algorithm takes to run in relation to input size.
- **Purpose**: Evaluates how execution time grows as input size increases.

## Space Complexity

- **Definition**: Measures the memory space an algorithm uses concerning its input size.
- **Purpose**: Assesses memory efficiency and resource constraints.

## Big O Notation

- **Definition**: Represents the upper bound on an algorithm's resource usage growth rate.
- **Purpose**: Simplifies worst-case time or space complexity representation.

## Best, Worst, and Average Cases

- **Definition**: Algorithms may perform differently based on input scenarios.
- **Purpose**: Comprehensive analysis considering best, worst, and average-case complexities.

## Constant Time (O(1))

- **Definition**: Algorithms with fixed execution time, irrespective of input size.
- **Purpose**: Highly efficient for quick operations.

## Linear Time (O(n))

- **Definition**: Execution time proportional to input size.
- **Purpose**: Suitable for scalable tasks with linear growth.

## Logarithmic Time (O(log n))

- **Definition**: Divides input into smaller portions with each step.
- **Purpose**: Efficient for large datasets with quick access.

## Polynomial Time (O(n<sup>k</sup>))

- **Definition**: Execution time increases with input size, governed by the degree 'k'.
- **Purpose**: Useful for problems with known polynomial growth rates.

## Exponential Time (O(2<sup>n</sup>))

- **Definition**: Execution time grows exponentially with input size.
- **Purpose**: Impractical for large inputs due to rapid growth.
