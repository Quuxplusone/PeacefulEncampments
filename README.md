# Peaceful Encampments visualizer

Instructions for use:

- Go to [https://quuxplusone.github.io/PeacefulEncampments/encamp4.html](https://quuxplusone.github.io/PeacefulEncampments/encamp4.html).

- Click in the margin around the square (close to the square's border, but just outside the square). This creates a stripe running across the square. The orientation of the stripe (vert, horiz, slash, or backslash) corresponds to which edge of the square you clicked near (top, right, bottom, or left). Everything outside of the stripe will turn green. The area inside the stripe is now marked "safe for red soldiers, in this one direction"; which is to say, "hazardous to the green army."

- Click in each of the three other margins to make four stripes. Click and drag their circular "handles" to move them around until all four stripes intersect at a point. The region where all four stripes intersect is guaranteed to be safe for red in all four directions. The region of the intersection will turn red.

- The text at the top of the screen displays "Red area" and "Green area" as a fraction of the unit square. Drag the handles around and watch the areas change.

- You can click in the margins to create additional stripes, if you need them.

- If you have made too many stripes, you can merge adjacent stripes back together by causing them to overlap.

- Click "Save in address bar" to save a JSON representation of the picture into your browser's address bar. You can copy and paste it from there to share your creation with other people. You can also use [urldecoder.org](https://www.urldecoder.org) / [urlencoder.org](https://www.urlencoder.org) to see what's in the JSON or to edit it by hand.

- Click "Jiggle" to randomly jiggle the stripes a little bit. If the random jiggling improves the solution (i.e., increases the size of the smallest army), then you'll see the new solution on your screen. If the random jiggling fails to help, nothing will happen.

- Type "J" to turn on auto-jiggle: it'll jiggle the solution every few milliseconds until you hit "J" again to cancel auto-jiggle. This is how I quickly turn a vague arrangement into an optimal solution.

- Click "Bigger" to zoom in; then click "Smaller" to zoom back out.

- Finally, the button labeled "red" indicates for which color army the stripes you're currently placing are "safe." After you place at least one red stripe, you can click this button to make it say "green," and start laying stripes that are safe for green soldiers. Areas outside any of your stripes — areas that are now unsafe for red and unsafe for green — will immediately turn blue. Now you're working on a three-army solution.

- After laying at least one green stripe, you can click the button to make it say "blue" and start working on a four-army solution. And so on, all the way up to a 20-army solution.

- Clicking the color button several times will cycle it through the currently available colors, so that you can go back and continue laying red stripes if you want.

- Type "W", "A", "S", or "D" to nudge every stripe in lockstep a tiny bit up, left, down, or right, respectively.

- Type "R" to make the jiggler respect 4-way symmetries in the arrangement. Type "R" again to stop respecting symmetries.
