I got inspired to create my own computer vision project tonight, and within 3 hours I had 4 separate breakthroughs—breakthroughs that can theoretically be integrated into a pipeline where particular steps are executed only as needed  / when an exact raw card match isn’t available in the database. The 4 are:

I built a test image database of player faces and proved out that I could make software that successful identified when cards had the same face, even when the poses were quite different, helmet vs. not and so on. The attached Lawlar cards match at 99.8832015991211%, whereas comparing the card on the right to a similar Rhys Hoskins card result in “The faces do not match”
I trained a ML model from scratch to recognize Topps, Bowman & Bowman Chrome logos in a number of different contexts (boxes, packs, cards from various sets and years)
Combined a distinct text recognition function with the possibility to check for player and (insert) set names. Combining this with 1 & 2 can get some interesting results even with out #4
Tonight I studied the computer vision concept of homography for a couple minutes… and wrote a pretty decent raw image scanning algorithm in less than 2 hours. It works by grey-scaling the images, running a Scale-Invariant Feature Transform (converting a high-contrast form of the image data into manageable numbers) and running an approximate nearest neighbor algorithm on the result of the SIFT. I tweaked the number of “features” that needed to match and how close those matches needed to be until I achieved the following results:
Comparing a very crooked 2023 Bowman Paper Rhys Hoskins to the centered “core” image, the algorithm returns a high confidence match. 
Comparing a 2023 Bowman Paper Trea Turner to the centered “core” image of Rhys, the algorithm returns a low confidence match, discovering that the Phillies logo and aspects of the graphic design are the exact same, but the photos are quite different. This enables me to return an OK result when the exact card is not in my database
Comparing a 2023 Bowman Chrome Jordan Lawlar to the centered “core” image of paper Rhys, the algorithm returns a 100% non match, given that the cards have a different brand logo, team logo and finish

I thought—and was able to implement a prototype—of all of those in three hours. It took me longer to write this summary than it did to write some of the functions themselves. Step 4 still requires access to well-aligned images of cards to seed the database with—I think that’s unavoidable with raw cards if you want to differentiate between similar cards in the same set. However, I think I could create a system that leverages a combination of techniques to have a raw card scanning system that’s pretty good. Other elements of the pipeline could be an edge color detection step for color variations, a super high contract edge detection step to detect atomic or mojo refractors (and similar print effects).

Image legend: 1) 99.9% confidence those cards are both Jordan Lawlar; 2) my SIFT engine detecting those cards are of the same team but aren’t the same card; 3) my SIFT engine recognizing those are the same card; 4) my logo-focused ML model successfully identified that card is a Bowman Chrome card but not a Bowman paper or Topps card

![lawlar](https://github.com/jameswomack/sights-on-september/assets/77849/72c81085-1ddd-456a-86a1-4189d803b860)
![10_trea-turner_grey](https://github.com/jameswomack/sights-on-september/assets/77849/9bd5c4c8-dccf-4551-a94e-cebedc483df2)
![matches](https://github.com/jameswomack/sights-on-september/assets/77849/f781a412-3aeb-4c64-a81b-fc385bbdf08c)
![card_2023-bowman-chrome_sights](https://github.com/jameswomack/sights-on-september/assets/77849/f3bf3017-6589-4a91-abb9-8859ae3ff4f2)