# Wordle Helper

A simple Python command-line assistant designed to help users narrow down valid guesses while solving **Wordle-style** puzzles.  
The tool filters a list of valid five-letter English words based on user feedback after each guess.

---

## 📌 Features

- Loads a dictionary of English words and filters for valid **5-letter candidates**
- Interactive CLI for entering guesses and outcome patterns
- Dynamically narrows the word list using:
  - **Green letters** (`2`) → correct letter in correct position  
  - **Yellow letters** (`1`) → letter exists but in different position  
  - **Gray letters** (`0`) → letter not in the target word (unless proven present elsewhere)

> Note: This implementation does **not** currently apply letter frequency heuristics or probability scoring — it is strictly a filtering helper.

---

## 🔧 Requirements

- Python 3.8+
- `words_dictionary.json` from:  
  https://github.com/dwyl/english-words/blob/master/words_dictionary.json

Place the file in the same directory as the script.

---

## ▶️ How to Run
    python wordle_helper.py

## 🧠 Logic Summary

The filtering rules follow standard Wordle constraints:
- 0	= Letter not in the word remove words containing that letter (unless marked present elsewhere)
- 1	= Yellow, correct letter, wrong position	Keep only words containing the letter, but not in that position
- 2	= Green, correct letter in correct position	Keep only words with that letter in that exact index
  
## 📁 Project Structure

    📂 Wordle-Helper
     ├─ wordle_helper.py
     └─ words_dictionary.json

## 🛠 Possible Future Improvements

- Statistical scoring / best-next-guess algorithm
- UI improvements
- Support for custom dictionaries and languages
- Export list narrowing history
- Solve mode (automatic guessing)

## 🧑‍💻 Author

Nicholas Ragano — 10/23/2023
