# Vax-Man

## System Requirement

- Tested with Python v3.10.2.
- Python should be configured with Tk.

## How to Run

1. Install dependencies. Use a virtual environment if you'd like to.
   ```sh
   pip install -r requirements.txt
   ```
1. Run.
   ```sh
   python vaxman.py
   ```

## Rules

The rules are similar to Pac-Man with several notable exceptions:

- Vax-Man can kill a ghost if he comes into contact with it (vaccinates it).
- Contact with a ghost does not kill Vax-Man.
- Each ghost that has not yet been hit multiplies itself every 30 seconds (the infection grows).
- The goal of the game is to collect all the dots before the number of ghosts grows to 32 times the original number.
