# 🗼 Tower of Hanoi (3D Torus Animation) – Maple

<img src="https://img.shields.io/badge/Maple-2023+-red?logo=maple&logoColor=white" alt="Maple"> <img src="https://img.shields.io/badge/License-MIT-green">

> An implementation of the classic Tower of Hanoi puzzle with a **3D torus‑shaped (donut) animation** of the disks.  
> The recursive solution is shown step by step, and each disk is drawn as a colourful torus that moves between three pegs.  
> The animation is fully interactive and can be exported as a GIF.

---

## 📖 Background – The Legend

There is a legend, often attributed to Édouard Lucas (a French mathematician in the late 1800s), concerning a puzzle being played by a temple of monks near Hanoi, Vietnam. The puzzle consists of three pegs and **64 golden disks**. All disks begin stacked on one peg in order of size – the largest at the base and the smallest at the top. The monks must move all disks from the starting peg to another peg by moving **one disk at a time**, never placing a larger disk on top of a smaller one. The legend predicts that when the monks finish, the world will end.

Fortunately, even if the legend were true, there is little to worry about: moving 64 disks at one move per second would take about **585 billion years**!  
`(2^64 - 1) seconds ≈ 584.9 × 10^9 years`

---

## ✨ Features

- Recursive solution for any number of disks (tested with `n ≤ 6` for performance)
- Console output showing each move (`Move disk X from rod Y to rod Z`)
- **3D graphical animation** where each disk is a **torus (donut)**:
  - Disk size (radius) corresponds to its number (larger number = larger radius)
  - Colour gradient (disk size determines colour)
  - Disks are stacked vertically with a fixed height offset
  - Three pegs placed horizontally (A: left, B: centre, C: right)
- Step‑by‑step animation: all moves are recorded and played back as an `insequence` display
- Fully implemented in **Maple** using `plot3d` and `plottools`

---

## 🖼 Sample Output (6 disks)

![Hanoi Animation](Animations/Hanoi_10.gif)

> *Above: 6 disks being moved from peg A to peg C using peg B as auxiliary. The torus‑shaped disks are colour‑coded and smoothly animated.*

---

## 📁 Code Structure (main functions)

| Function / Variable | Description |
|---------------------|-------------|
| `hanoi(N, from, aux, to)` | Recursive procedure that prints each move to the console. |
| `Hanoi(n, from, aux, to)` | Wrapper that prints total number of moves and calls `hanoi`. |
| `move(L1, L2)` | Moves the top disk (last element) from list `L1` to list `L2`. |
| `mover(p1, p2)` | Global rod update: moves disk from peg `p1` to peg `p2` using global variables `rodA`, `rodB`, `rodC`. |
| `frame(R1, R2, R3)` | Creates a **3D torus** for each disk in the three rods. Returns a `display` of all tori. |
| `Ghanoi(N, from, aux, to)` | Recursive procedure that performs moves **and** appends a `frame` to the global `anime` list. |
| `GHanoi(n, from, aux, to)` | Initialises rods, clears `anime`, calls `Ghanoi`, and prepares the animation. |
| `anime` (global) | List of frames (one per move) to be played later. |

---

## 🚀 How to Run

1. Open Maple and load the worksheet (`.mw`) or execute the code in a Maple worksheet.
2. Make sure the `plots` package is loaded (already in the code).
3. Set the number of disks (e.g., `n := 6`).
4. Run the animation:
   ```maple
   GHanoi(n);
   display(anime, insequence = true, scaling = constrained, axes = none);
   ```
5. You will see a 3D animation of the disks moving between the three pegs.
   To export as GIF:
   - Right‑click on the animation → Export → GIF → choose file name (e.g., hanoi_10.gif).
   You can also watch the console output of moves:
   ```maple
   Hanoi(n);
   ```

--- 

## 📊 Recursive Algorithm

Let `S(n)` be the minimal number of moves for `n` disks.  
The recursive relation is:

```
S(n) = 2·S(n−1) + 1, with S(0) = 0.
```


This yields the closed form:  
**`S(n) = 2ⁿ − 1`**

For example:
| n | moves |
|---|-------|
| 1 | 1 |
| 2 | 3 |
| 3 | 7 |
| 4 | 15 |
| 6 | 63 |
| 64 | 2⁶⁴−1 ≈ 1.84×10¹⁹ |

The recursive steps are:
1. Move the top `n−1` disks from the source peg to the auxiliary peg.
2. Move the largest disk (n) from source to target peg.
3. Move the `n−1` disks from auxiliary to target peg.

---

## 🧪 Try Different Numbers of Disks

- **1 disk** – Trivial, animation is very short.
- **3 disks** – 7 moves, good for understanding the pattern.
- **4–5 disks** – Still runs quickly, nice to watch.
- **6 disks** – 63 moves, animation is longer but still smooth.
- **7+ disks** – The number of frames grows exponentially; Maple may slow down or run out of memory.  
  ⚠️ **Recommended maximum: 6 disks** for smooth animation.

To change the number of disks, simply modify:
```maple
n := 4;          # number of disks
GHanoi(n);
display(anime, insequence = true);
```

---

## 🖼 3D Graphics – How the Torus is Drawn

Each disk is drawn using a **torus** parametrisation:
```
x = (R + cos(u))·sin(v)
y = (R + cos(u))·cos(v)
z = sin(u) + height_offset
```


- `R` = radius of the disk (larger for bigger disks)
- `u, v` run from `0` to `2π` (full torus)
- `height_offset = 1.7·i` where `i` is the disk's position in the stack (1 = bottom)
- Colour is determined by the disk number (the Maple `color` option).

The three pegs are placed at different `x` positions:
- Peg A (left):    `x` shifted by `0`
- Peg B (center):  `x` shifted by `2·mn + 2`, where `mn` = max disk size
- Peg C (right):   `x` shifted by `4·mn + 4`

This creates a clear, colourful, and easily understandable 3D scene.

---

## 📥 Prerequisites

- Maple 2023 or newer (older versions may work if they support `plot3d` with `insequence`)
- Package `plots` (loaded automatically with `with(plots)`)

---

## 👤 Author

Mohammad Javad Abdolahi – University project for Programming with Maple, Dr. Amir Hashemi & Combinatorics, Dr. Behnaz Omomi – February 2023

---

## 📜 License

This project is licensed under the MIT License – free to use, modify, and distribute.

---

> 🌟 If you like this project, please **⭐ Star** the repository!

---

## 🔗 Related Projects

- [Forest Fire Simulation (Maple)](https://github.com/javadabdolahi/University-Projects/Forest-Fire-Simulation)
- [Conway's Game of Life (Maple)](https://github.com/javadabdolahi/University-Projects/Game-of-Life)
