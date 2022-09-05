# Overview
**NOTE: This repository is a work in progress.**


The Composer Model is an AI model that will (eventually) be able to write a song.  It will use generative adversarial networks (GANs) to generate the song's data. This data will build a new wav file.

It accomplishes this by first taking in mp3 files and converting them into wav format.  We can then parse the wav files and obtain a numpy array representing the sound wave.  This can then be inputted into the model at train time, along with some other metadata about the song.

We will primarily be using public domain music to avoid any copyright infringement.

# Features
#### Current Features
- Frame rate
- Sample width
- Song length
- Mono vs stereo
- Sound wave (represented as a numpy array)


