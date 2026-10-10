# babel

my own version of the library of babel, plus a miner that digs through it looking for real english.

live: https://navthings.github.io/babel

## what it is

borges wrote a story about a library that has every possible book in it. every page is 40 lines of 80 characters, 26 letters plus space, comma and full stop. so it has every book ever written, every book that will be written, and an absurd amount of pure garbage.

jonathan basile actually built it at [libraryofbabel.info](https://libraryofbabel.info). this is me building my own from scratch to see how it works.

there are 29^3200 pages, around 4.7 × 10^4679. you obviously cant store that, so nothing is stored. every page has a number, and a reversible shuffle turns the number into the page text and the text back into the number. thats why search is instant: it doesnt look for your text, it just runs the shuffle backwards and tells you where it lives.

the shuffle is an affine map mod 29^3200, then reversing the digits, then another affine map. inverses use hensel lifting since the modulus is a prime power. all of it is plain js BigInt.

## the three tabs

**mine**: web workers read random pages and keep the longest unbroken run of real words (40k common words from SCOWL). records so far land around 10 to 20 characters, the odds fall off a cliff after that. about 60k pages a second per thread on a laptop.

**search**: type anything, get its exact page and address. "alone on the page" pads it with spaces, "among noise" hides it in random letters.

**browse**: paste an address, step to the next or previous page, or jump to a random one.

## files

- `src.html` the actual page
- `words.txt` the word list
- `build.py` inlines the words into src.html and writes `index.html`

edit src.html then run `python3 build.py`.

## why

i wanted to see how the original works, and whether brute force could find anything readable. it cant really, which is kind of the point.
