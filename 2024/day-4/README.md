# README

Because this one has been a pain in the butt (I'm dumb and took too long to figure out how to write the diagonal scan correctly), I'm writing this down here. I have the sample input saved here, which is supposed to return 18 possible matches for the `XMAS` search string for part one of the problem.

```plaintext
M M M S X X M A S M
M S A M X M S M S A
A M X S X M A A M M
M S A M A S M S M X
X M A S A M X A M M
X X A M M X X A M A
S M S M S A S X S S
S A X A M A S A A A
M A M M M X M M M M
M X M X A X M A S X
```

I spent a lot of time on part one mostly because I'm an idiot who didn't understand how
to write a diagonal parser correctly, and I messed up my very manual implementation of a
matrix rotation. I ended up using a one-liner I found on a very old StackOverflow question
and fixed the check for overlapping the middle line when parsing diagonally and voila,
it's all working now.


For part two, I have to find all instances of the MAS substring present on the grid in an X shape.

...

I can see why the elf was looking quizzical upon seeing the solution to part one.

This was a few minutes of thinking. My solution was just scanning for all A's, and matching the four
elements diagonally adjecent to that A with a set of four possible combinations.
