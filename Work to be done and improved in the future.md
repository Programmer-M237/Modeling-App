1. **Arrange the returning to alternative form with preserved data to make it flexible**:

&nbsp;	From the beginning it was solely designed to grab the data from the alternative widget and store whenever the alternative base or default option is chosen. This works if the previous form type was alternative, but doesn't if the previous form type is alternative base or default because when the user switches from alternative to another form type, the data of the alternative widget is grab and store and the alternative widget is cleared (to make the user aware that form type have been changed and show that it is now disable), so no data is grab if the user switch a non-alternative form type (other different form types apart from the alternative form type) to another non-alternative from type, the data stored is lost. I used this method for all objects demanding different form types and noticed the error at object 23. 

&nbsp;	To resolve this problem, we have to make sure the code that grabs the data to only run if the previous form type is alternative (so we will need to create a new string var prev\_form\_type to store the previous form type and be it updated regularly). Ask technical details from Programmer M

2\.	**Build the right algorithm for teams with roles (still for flexibility purposes)**:

&nbsp;	Generally, a usual behavior of algorithms of most of the objects (which are easier compared to this) selects elements from a pool (irony for explanation) to group it. But for the case of this object, the elements are selected from a pool to group them, and the elements from each group is selected again to further  group it. This two grouping systems make this object complex. I type vibe coded this on all AIs possible, known could give me what I wanted exactly (seems as AI have difficulties in combinatorics \[one of the main reason why this app have to be created])

3\.	**Build the right algorithm for necklace case (direction doesn't matter and reflection identical, and guess what still for flexibility purposes)**:

&nbsp;	AIs also seems to have difficulties with circular permutations. Under hard struggle of vibe coding, I got the right algorithms for the three other cases, but AIs kept confusing me on this case (showcasing it complexity). But I learnt that the correct implementation of this case is done using the Burnside's lemma (others are done through the usual combinatorial rules). 

4\.	**Highly optimized the backend**:

&nbsp;	From the very beginning even before I began researching on ways to build this app, I knew that high speed, efficient memory usage and optimization was needed. The algorithms I used presently are not optimized and majority even work but on heavy computations (not using generators). After the construction of the object types, I will optimized all the backend using generators (#1), and cython optimized code syntax (#2), and maybe some more optimizations. These may not still be enough, but it will do some optimization in it. More optimizations will brought in the future (scaling)

5\. **Check the backend of object 24 (asked from a combinatorial expert)**



***Generally one important need for this project was a combinatorial expert (which I looked for one but couldn't find, I think employing one will be the best solution). I myself I may be a genius, but I'm aren't an expert at combinatorics, in fact I never heard of combinatorics until when I began advancing number system indices***

