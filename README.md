# Boids Algorithm

An implementation and simulation of Boids Algorithm (a.k.a Reynolds Flocking) in Python

### Installing Dependencies

* pip install numpy pygame
* brew install ffmpeg

### Executing Program

To run simulation with default arguments
```
python main.py
```
main.py takes arguments for the number of agents, whether to save frames, and simulation length.
Run with ```--help``` flag for more information.

If main.py is run with ```--save_frames True``` frames will be saved as .png files to a ```frames/```
directory.

To convert these frames into .mp4 and .gif files, run
```
bash convert_frames.sh
```

## Notes
* On my M2 Macbook Air >~150 agents makes the pygame window choppy. However, with greater numbers of agents you can save the frames and convert to a smooth .mp4/.gif file afterwards (see sim of 250 agents below)
* ```convert_frames.sh``` deletes individual frames after creating a video, and will overwrite existing boids.mp4/.gif files. I did this since the simulations are very random, however if an individual run has
sentimental value treat it with care.

## Authors
Ralph Quartiano (https://ralphq.github.io/)