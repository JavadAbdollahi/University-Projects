# 🌳 Prüfer Code and Its Uniqueness for Trees

[![فارسی](https://img.shields.io/badge/lang-فارسی-blue)](README.fa.md)

> **تغییر زبان:** روی نشانه‌ی بالا کلیک کنید تا نسخه‌ی فارسی را ببینید.

## 📖 What is the Prüfer Code?

The **Prüfer code** is a unique sequence of length \(n-2\) associated with any labeled tree on \(n\) vertices. It provides a compact representation and proves that the number of labeled trees is \(n^{n-2}\).

## ⚙️ How Does It Work?

### Encoding (Tree → Code)
1. Find the smallest leaf (vertex of degree 1).
2. Output its neighbor.
3. Remove the leaf.
4. Repeat until two vertices remain.

### Decoding (Code → Tree)
1. Compute the degree of each vertex.
2. Repeatedly connect the smallest vertex of degree 1 to the first element of the code, then decrease degrees.
3. Finally connect the two remaining vertices.

## 📄 Full Report (PDF)

The complete report, including algorithms, examples, and proofs, is available here:

[📗 Download / View English Report](doc/English.pdf)

> GitHub can preview the PDF directly – just click the link.

## 🧪 Example

The report walks through a concrete example step by step, showing both encoding and decoding for a tree with 6 vertices.

## 👤 Authors

**Mohammad Hossein Kazemini – Mohammad Javad Abdolahi**  
Graph Theory course project – February 2025

## 📜 License

MIT