# ⚡ Quick Sort: Comparison of Pivot Selection Strategies

<img src="https://img.shields.io/badge/Python-3.8+-blue?logo=python" alt="Python"> <img src="https://img.shields.io/badge/License-MIT-green">

> An experimental analysis of the Quick Sort algorithm using five different pivot selection strategies: **first**, **last**, **middle**, **median‑of‑three**, and **random**.  
> The code measures sorting time on various input types (sorted, reversed, worst‑case for middle pivot, worst‑case for median‑of‑three, and random lists) and demonstrates why **random pivot selection** is the most robust choice in practice.

---

## 📖 Overview

Quick Sort is a divide‑and‑conquer algorithm. Its performance heavily depends on the **balance** of the partitions created by the pivot element. A perfectly balanced partition (half the elements on each side) gives `O(n log n)` time, while a completely unbalanced partition (one side empty) gives `O(n²)`.

Different pivot selection strategies behave differently on specific input patterns. This project implements and compares five strategies on multiple list types to see which one consistently yields the best performance.

---

## 🎯 Pivot Selection Strategies

| Strategy | Description | Best case | Worst case |
|----------|-------------|-----------|------------|
| **first** | Always pick the first element | Already random data | Already sorted or reverse sorted |
| **last**  | Always pick the last element | Already random data | Already sorted or reverse sorted |
| **middle**| Pick the middle element | Sorted / reversed data | Specially crafted “worst‑case for middle” |
| **median‑of‑three** | Median of first, middle, last elements | Most inputs | Specially crafted adversarial lists |
| **random** | Pick a uniformly random element | Any input | Probability of worst case is negligible |

---

## 🧪 Experiment Setup

- **List size** : 30,000 elements
- **Input types**:
  1. **Sorted** – already in ascending order
  2. **Reversed** – descending order
  3. **Worst‑case for middle pivot** – constructed to make the middle pivot always unbalanced
  4. **Worst‑case for median‑of‑three** – constructed to defeat median‑of‑three
  5. **Random** – uniformly shuffled
- **Metrics**: actual sorting time in seconds (measured with `time.time()`)
- **Recursion limit** increased to handle deep recursion (not needed for random pivot but for deterministic worst cases)

The code runs each pivot strategy on each list type and records the time.

---

## 📊 Experimental Results (30,000 elements)

| List Type | first   | middle  | last    | median‑of‑three | random  |
|-----------|---------|---------|---------|-----------------|---------|
| Sorted    | 33.885  | **0.026**| 34.156  | 0.030           | 0.042   |
| Reversed  | 33.566  | **0.025**| 35.854  | 0.030           | 0.040   |
| Worst‑case (middle pivot) | 14.982 | 34.134 | 14.228 | **0.043**       | 0.040   |
| Worst‑case (median‑of‑three) | 7.252 | 8.087 | 7.522 | 16.530          | **0.041** |
| Random    | 0.038   | 0.042   | 0.030   | 0.040           | 0.045   |

> *Times are in seconds. The best time for each row is shown in **bold**.*

### Key observations

1. **First / last pivot** are catastrophic on sorted and reversed lists (≈34 s) but fast on random data (≈0.04 s).
2. **Middle pivot** works perfectly on sorted/reversed (≈0.025 s) but fails dramatically on its own worst‑case list (34 s).
3. **Median‑of‑three** handles sorted/reversed and the middle‑pivot worst‑case very well, but it has its own adversarial input where it becomes slow (16.5 s).
4. **Random pivot** never exceeds **0.045 seconds** on any tested input – it is the most consistent and robust strategy.

---

## 📐 Correct Mathematical Analysis

### Why does random pivot work so well?

The performance of Quick Sort depends on the **rank** of the pivot – i.e., how many elements are smaller than it. If the pivot’s rank is between `n/4` and `3n/4`, the partition is balanced (each side contains at most `3n/4` elements).

For a **randomly chosen pivot**:
- Probability that the pivot lies in the central 50% (rank between 25% and 75%) is exactly **0.5**.
- Even if the pivot is outside this central region, the recursion depth only increases by a constant factor.

A standard result in randomized algorithms:  
> *The expected number of comparisons for randomized Quick Sort is **O(n log n)**, and the probability that the running time exceeds `c n log n` is less than `1/n²` for large `n`.*

This guarantee holds **for any input** – the randomness is inside the algorithm, not assumed on the data. In contrast, deterministic strategies (first, last, middle, median‑of‑three) can be forced to run in `O(n²)` by an adversary who knows the strategy.

### Common misconception – the Central Limit Theorem

**CLT does not explain the success of random pivot.**  
- CLT concerns the distribution of **sample means** (averages of many independent samples), not the distribution of single random selections.  
- In Quick Sort we pick **one** pivot per recursive call, not an average of many pivots.  
- The reason random pivot works is simply that with probability at least 1/2 we get a reasonably balanced split, and this probabilistic fact repeats at each level of recursion – leading to an expected logarithmic depth.

Thus, the correct reasoning is based on **expected value analysis** and **Chernoff‑style bounds**, not on the Central Limit Theorem.

---

## 🚀 How to Run

1. Make sure you have Python 3.8+ installed.
2. Copy the code into a file, e.g., `quick_sort_analysis.py`.
3. Run the script:
   ```bash
   python quick_sort_analysis.py
   ```
4. The script will:
   - Generate the lists (30,000 elements each)

   - Show initial states (first, middle, last 10 elements)

   - Sort each list with each pivot strategy and print the time

   - Finally, display a summary table of all sorting times

> You can change `num_elements` and `display_count` at the top of the script.

## 📁 Code Structure

| Function | Description |
|----------|-------------|
| `quick_sort(arr, pivot_choice)` | Recursive Quick Sort with pivot strategy parameter. |
| `create_lists(size)` | Generates five types of lists (sorted, reversed, worst‑case for middle, worst‑case for median‑of‑three, random). |
| `sort_and_show(arr, pivot_choice, list_name, display_count)` | Times the sort and prints the result and a sample of sorted elements. |
| `record_time(...)` | Stores measured times in a dictionary. |
| `show_all_sorting_times()` | Prints the complete comparison table. |

---

## 📥 Prerequisites

- Python 3.8 or newer
- Standard libraries: `random`, `time`, `sys`

No external packages are needed.

---

## 👤 Author

Mohammad Javad Abdolahi – University project for Data Structures – February 2024

---

## 📜 License

This project is licensed under the MIT License – free to use, modify, and distribute.

---

> 🌟 If you find this analysis useful, please **⭐ Star** the repository!

---

## 💬 FAQ

**Q:** Why does `median‑of‑three` fail on the last worst‑case list?  
**A:** The list was specifically constructed so that the median of the first, middle, and last elements always falls near one extreme, causing unbalanced partitions. This shows that even “smart” deterministic strategies can be fooled.

**Q:** Can I run with more than 30,000 elements?  
**A:** Yes, but be careful with recursion depth. The script already sets a high recursion limit. However, the deterministic strategies may become extremely slow (many seconds) for much larger sorted lists.

**Q:** Does random pivot ever become slow?  
**A:** Theoretically yes, but the probability is astronomically small. In practice, on a standard computer, you will never see a slow run on random pivot.

**Q:** Why is the median‑of‑three sometimes faster than random in the table?  
**A:** For small inputs or specific patterns, median‑of‑three can indeed be slightly faster because it avoids the overhead of generating a random number. However, random pivot is **robust** – it will never be catastrophically slow, while median‑of‑three can be (as shown in the last row).