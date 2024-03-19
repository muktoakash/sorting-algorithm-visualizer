# Sorting Algorithm Visualizer

This is something that I have thought of building for a while. i have created animations in MATLAB and coded sorting algorithms in C, but this time I am using python to combine both ideas.

**Table of Contents**
* [Using Pygame](#pygame)
  - [Setting up](#pygame-setting-up)
  - [Classes](#pygame-classes)
  - [Requirements](#pygame-requirements)
  - [Files](#pygame-files)

<a id="pygame"></a>
## Using Pygame

 Following along a [youtube video from tech with Tim](https://www.youtube.com/watch?v=twRidO-_vqQ&amp;t=3975s). The same coding structure is used, but with some major modifications to make the code more versatile. Each line of code is being carefully considered before being used.

The objective is to learn pygame, specially on creating animations using pygame.

<a id="pygame-setting-up"></a>
### Setting up
The program generates a random list. The members of the list are then visualized using a pygame window.
![Visualization of the Initial list](./Pygame/assets/visualize_initial_list_with_title.png)
The user would then select the sorting algorithm to visualize, as well as whether to sort in an ascending or descending order. The sorting is then animated on the screen, with colors used to indicate list members being swapped for sorting.
[Snapshot of sorting visualization](./Pygame/assets/visualize_while_sorting.png)
Once the entire list is sorted, the final list is seen to be in ascending or descending order as chosed earlier by the user.
[Visualization of Sorted List](./Pygame/assets/visualize_sorted_list.png)


<a id="pygame-classes"></a>
### Classes:
- DrawInformation : sets up initial pygame window for drawing the bars.

<a id="pygame-requirements"></a>
### Requirements:
[requirements.txt](requirements.txt)

<a id="pygame-files"></a>
### Files:
[Files used in this part](./Pygame/pygame_files.md)
