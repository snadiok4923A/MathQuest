# MathQuest — Educational Arithmetic Game

A terminal-based learning game that turns arithmetic practice into a 10-round challenge.

## What students practice
- Addition and subtraction
- Multiplication and division
- Mental arithmetic and accuracy
- Increasing difficulty and timed-feeling quick rounds
- Learning through score, streak, and rank feedback

## Features
- Five difficulty levels
- Randomly generated questions
- Four multiple-choice answers
- Combo scoring for consecutive correct answers
- Personal-best score saved locally
- Five automated tests
- No third-party packages

## Run
```bash
python main.py
```

## Controls
Choose menu options with numbers. During a challenge, enter 1–4 to answer or Q to stop the run.

## Tests
```bash
python -m unittest discover -s tests -v
```

## Project structure
- `main.py` — menus and game loop
- `mathquest/engine.py` — question generation, choices, scoring, ranks
- `tests/test_engine.py` — automated tests

Python 3.10+. MIT License.
