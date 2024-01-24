
---

# Word Permutation Translator

## Overview

This Python script takes a statement with jumbled words as input and rearranges each word to form a coherent sentence. It utilizes the `itertools` library for generating permutations and the `wordfreq` library to evaluate the likelihood of each permutation based on Zipf frequency.

## Usage

1. **Installation:**
   - Ensure you have the required libraries installed:
     ```bash
     pip install wordfreq
     ```

2. **Run the Script:**
   - Execute the Python script in your terminal or preferred Python environment.

3. **Input:**
   - Provide a statement with jumbled words as input. For example:
     ```python
     taken_statement = "Three were two gerat dyas in ym lief"
     ```

4. **Output:**
   - The script will output a translated statement with the rearranged words. For example:
     ```python
     Output: "there were two great days in my life"
     ```

## Examples

### Example 1

**Input:**
```python
taken_statement = "If Yuo aer Albe To Raed Tihs"
```

**Output:**
```python
Output: "if you are able to read this"
```

### Example 2

**Input:**
```python
taken_statement = "The rset can be a toatl mses"
```

**Output:**
```python
Output: "the rest can be a total mess"
```

### Example 3

**Input:**
```python
taken_statement = "the huamn mnid deos not raed ervey lteter by istlef"
```

**Output:**
```python
Output: "human mind does not read every letter by itself"
```

### Example 4

**Input:**
```python
taken_statement = "Three were two gerat dyas in ym lief"
```

**Output:**
```python
Output: "there were two great days in my life"
```

## Notes

- The script uses the Zipf frequency from the `wordfreq` library to determine the likelihood of each permutation.
- Adjustments to the code or input can be made to experiment with different statements.

Feel free to explore and experiment with the script to understand word permutations and their impact on readability.

--- 

Customize the README file according to your preferences and include any additional information that might be helpful for users or developers interacting with your Python script.
