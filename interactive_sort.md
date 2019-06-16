Interactive sort
===

This one is quite simple and reuses only one readily available module: you.

The algorithm:

1. Put the elements in a list.

2. Go through all permutations of the list.

3. For each permutation, ask the user if it's sorted. If yes, quit; if not, go to the next permutation.

4. If you exhaust all the permutations, the user messed up. Go back to step 2.

The good sides of this are obvious:

1. Any criterion for sorting is supported out of the box (no extra coding needed!).

2. It's reliable, because it goes through all the permutations, not skipping a single one due to some pesky "optimization".

3. It keeps users' minds sharp and focused. It will also keep _you_ in their minds, albeit not in the most pleasant context.

4. It makes your users look very busy and unavailable if anyone checks on them while "working". Kinda like that "[compiling](https://xkcd.com/303/)" thing we used to use as an excuse in the older days.

The bad sides of this algorithm:

* There aren't any real downsides to it. If you see one, you're probably just lazy.

A bit ~ugly~ PERLish example written in Python can be seen [here](interactive_sort.py). I'll gladly accept contributions in other languages.
