# Numberplate-finder

Finds UK private registrations that read as words, by checking every word in an English dictionary against the current UK plate format (`AB12 CDE`).

The script takes every 4-letter word whose last two letters map to a valid number and turns it into the first half of a plate. Add whatever three letters you like on the end

Here is the 'leet list'
```python
cool_letters2 = {
                 "OR": "02", "OE": "03", "OA": "04", "OS": "05", "OG": "06", "OT": "07", "OB": "08", "OP": "09",
                 "IO": "10", "II": "11", "IR": "12", "IE": "13", "IA": "14", "IS": "15", "IG": "16", "IT": "17",
                 "IB": "18", "IP": "19", "RO": "20", "RI": "21", "RR": "22", "RE": "23", "RA": "24", "RS": "25",
                 "RG": "26",
                 "SI": "51", "SR": "52", "SE": "53", "SA": "54", "SS": "55", "SG": "56", "ST": "57", "SB": "58",
                 "SP": "59", "GO": "60", "GI": "61", "GR": "62", "GE": "63", "GA": "64", "GS": "65", "GG": "66",
                 "GT": "67", "GB": "68", "GP": "69", "TO": "70", "TI": "71", "TR": "72", "TE": "73", "TA": "74",
                 "TS": "75", "TG": "76"
		 #,
                 # L as 1, Z as 2
                 #"OZ": "02", "LO": "10", "LI": "11", "IL": "11", "LL": "11", "LR": "12", "IZ": "12", "LZ": "12",
                 #"LE": "13", "LA": "14", "LS": "15", "LG": "16", "LT": "17", "LB": "18", "LP": "19", "ZO": "20",
                 #"ZI": "21", "RL": "21", "ZL": "21", "ZR": "22", "RZ": "22", "ZZ": "22", "ZE": "23", "ZA": "24",
                 #"ZS": "25", "ZG": "26", "SL": "51", "SZ": "52", "GL": "61", "GZ": "62", "TL": "71", "TZ": "72"
                 }
```                 
Uncomment the last bit if you want to sub L for 1, Z for 2.

## Usage

```
pip install "english-words>=2.0"
python plates4.py
```

Results are written to `4LetterPlates2.txt`. A pre-generated copy is included in the repo if you just want to browse.



Not everything in the output can actually be issued. Check against the DVLA rules:

- **First letter** must be a real DVLA region, so nothing starting with I, J, Q, T, U, X or Z.
- **Second letter** can't be I, Q or Z.
- **The number** must be a real age identifier: 02–26 (March plates) or 51–76 (September plates).
- **Can't make a car look newer than it is.** A 57 plate can only go on a car registered from September 2007 onwards.
- DVLA withholds anything offensive, and many good ones are already sold.



## Also in here

`generate_five_letter_plate()` does the same for the older prefix format, swapping the second letter of a 5-letter word for a digit (e.g. `B4KER`). It's disabled by default. Uncomment it in `__main__` to use it.
