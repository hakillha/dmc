
# How to use dmc.py

1. Decide on a positive distance between 0 and 50. this will be the vertical distance between the moons.
2. Using this distance, run torus_maker.py and generate two image files of the same distance, but one colored as a solution and one colored as black. The pixel densities do not matter, but they help when testing the efficacy of different densities.
3. Run dmc.py. It will use the training file to train itself and color the black pixels in the test file according to its training. Here is an example of what you would put in:
    Training filename : dm25_solution.png
    Test filename (black) : dm25.png
    Output filename (to be created) : dm25_answer.png
Where dm25_solution.png is the pre-colored training set, dm25.png is the black test set, and dm25_answer.png is the file to be outputted.
