Hard sort
===

This one might be a bit hard to understand for younger audiences, as it has somewhat unorthodox requirements. On the bright side, it requires absolutely no knowledge of programming in any language! 😁

What you need for this is [MS-DOS](https://en.wikipedia.org/wiki/MS-DOS) and any editor.

The algorithm:

1. Make a directory on your disk, for example `mkdir sort`.

2. Enter that directory: `cd sort`.

3. For each item of the list you want to sort, create a file with the name corresponding to that item. For example, create files named `17.txt`, `13.txt`, and `19.txt`.

4. Defragment your disk using the `/s` option, for example `defrag c: /f /sn /skiphigh`.

This has some minor drawbacks:

1. File names are strings, so numbers need to be prefixed with zeros to have the same length.

2. Strings comparison is case-insensitive.

3. The length of file names - and therefore the items you're sorting - is limited to 8 characters.

4. Finding a working computer running DOS might prove to be a tad problematic.

But all of this obviously fades away in comparison to overwhelming advantages, like

1. You don't need to know any programming languages.

2. You get a long coffee break, because DOS is not multitasking like Linux and modern _wannabe_ "operating systems" like M$ Windows and MacOS, and your computer will be unavailable while this is running. Don't ruin this by using a virtual machine!

3. The length of the process is almost completely independent on the length of your list as it depends on the content and fragmentation of your disk. This means that, in a somewhat stretched theory, its complexity is O(1). No other sort gets even close to that!

    * Bonus points: observe people's faces when you tell them that "one of the slowest sort in existence is O(1)". You probably won't be able to tell apart those confused by that whole statement from those confused by "what the Hell is 'oh of one'?!".
