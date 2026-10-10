# babel

in every page that could ever be written, find gold

https://navthings.github.io/babel

my own library of babel (borges, and jonathan basile's [libraryofbabel.info](https://libraryofbabel.info)). every page is 3200 characters from a-z, space, comma and full stop, so 29^3200 pages. none are stored, a page's address is the page run through a reversible shuffle (affine map mod 29^3200, flip the digits, another affine map). so search is instant, it just runs the shuffle backwards.

- mine: web workers read random pages and keep the longest run of real words. ~60k pages/s per thread on my mac
- search: type something, get its page and address, or send it to basile's search
- browse: paste an address, prev, next, random

edit `src.html`, then `python3 build.py` to inline `words.txt` (40k words from SCOWL) into `index.html`
