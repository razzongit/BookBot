# 📚 BookBot

BookBot is a simple Python program that analyzes the text of a book and provides useful statistics like word count and character frequency. BookBot is my first [Boot.dev](https://www.boot.dev) project!

## 🚀 Features

*   Counts the total number of words in a text file.
*   Counts each character’s frequency (case-insensitive).
*   Sorts characters by frequency in descending order.
*   Prints a clean summary in the terminal.

---

## 🛠️ How It Works

*   The program takes the **path to a book (text file)** as a command-line argument.
*   It reads the book, splits it into words, and counts words + characters.
*   It outputs statistics in a nicely formatted way.

---

## 📦 Installation & Setup

1.  Clone this repository:

```
	git clone https://github.com/your-username/bookbot.git
	cd bookbot
```

    2. Make sure you have **Python 3.7+** installed:

```
python3 --version

```

---

## ▶️ Usage

Run the program by passing the path to a text file:

```
python3 main.py <path_to_book>
```

Example:

```
python3 main.py books/frankenstein.txt
```

---

## 🖥️ Example Output

```
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt
----------- Word Count ----------
Found 78,456 total words
----------- Character Count ----------
e: 46092
t: 32001
a: 29010
o: 28012
n: 27005
...
```