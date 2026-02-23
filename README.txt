This is a simple set of instructions for how to run my project's program:

NOTE: I did attempt some extra credit by doing three operations per chapter, but was unable to do the full
extra credit and add a literature review or discussion section; I'm not sure if that counts for anything.

Format:
I chose to do three morphological operations from Chapter 2 as well as two from Chapter 3, though I am
not sure

Steps:
  -Install the external libraries I used for this project by running the following commands:
        - pip install opencv-python
            - This open-source library is one of the most popular for morphological and
            computer vision algorithms
        - pip install numpy
            - This Numerical Python library is used for many complex mathematical computations,
            but for this project, I used it to develop my matrix kernels for several operations
        - pip install matplotlib
            - This plotting library was used to visualize the results of my operations side-by-side
            within my IDE, it was a very helpful tool set

  -Next, go to the main file and uncomment the desired operations function
  -Run the program to see the results in plotted for side-by-side
    -Note, when you run the program, the resultant image(s) will be written to the Altered_Images folder
        -P.S. I left the folder empty for now so that you could write to it when you run the program
        -You can even run them all at the same time if you wish, the plots are not saved to memory, only the
        resultant image, which is just overwritten
  -Feel free to modify the kernel sizes and alpha/gamma values to test the functions, I left some
  comments on what I found interesting