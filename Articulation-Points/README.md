# 🔍 Articulation Points in Graphs using DFS

[![فارسی](https://img.shields.io/badge/lang-فارسی-blue)](README.fa.md)

> **تغییر زبان:** روی نشانه‌ی بالا کلیک کنید تا نسخه‌ی انگلیسی را ببینید.an.

## 📖 What is the Problem?

An **articulation point** (or cut vertex) in an undirected graph is a vertex whose removal increases the number of connected components. Finding these vertices is important in network reliability, analyzing communication networks, and understanding graph structure.

## ⚙️ How Does the Algorithm Work?

We use **Depth‑First Search (DFS)** and compute two values for each vertex `u`:

- `DFNum(u)`: the discovery time (order) of `u` during DFS.
- `Low(u)`: the smallest `DFNum` reachable from `u` using tree edges or at most one back edge.

Then a non‑root vertex `u` is an articulation point if it has a child `v` with:

    ```
    Low(v) ≥ DFNum(u)
    ```


The root is an articulation point if it has **more than one child** in the DFS tree.

The algorithm runs in **O(V + E)** time.

## 📄 Full Report (PDF)

The complete research report, including the algorithm, proof of correctness, and an example, is available here:

[📗 Download / View English Report](doc/English.pdf)

> GitHub can preview the PDF directly – just click the link.

## 🧪 Example Graph

The report walks through a concrete example step by step, showing the DFS tree, computed values, and the final set of articulation points.

## 👤 Author

**Mohammad Javad Abdolahi** – Graph Theory course project – February 2023

## 📜 License

MIT