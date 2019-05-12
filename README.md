# Python scripts for remote sensing
This repository contains some python scripts for working with multispectral raster data (e.g. Sentinel, Landsat, Drone imagery...). Often, running a script is a much faster way to get results, than doing the same steps in a GIS system.
<br />The used modules are all ***OpenSource***.

The purpose and what the single steps do, is documented inline, inside the scripts.

## Getting started
If all the dependencies are installed, the scripts run in any python environment. Just make sure to change the path to the raster files inside the scripts, to match the files on your machine. <br />
If you haven't one, the next section provides some steps to create a python runtime on your own machine.

### Create a local python runtime environment
There are many ways to create a python environment. Therefore, the following one is just one of many options.
* Download [PyCharm](https://www.jetbrains.com/pycharm/) from [https://www.jetbrains.com/pycharm/](https://www.jetbrains.com/pycharm/). <br />Make sure to download the community edition which is free and open-source.
* Run the installer to install PyCharm on your machine.
* If you have a Git installation, you can clone this repository by typing <br />```git clone https://github.com/hkfrei/python_remote_sensing.git``` in your console, <br />
otherwise just download the .zip folder.
* Open PyCharm, create a new project and add the files from this repository.
* Before you can run the scripts, you have to install the dependencies. <br />
You can do this according to [this](https://www.jetbrains.com/help/pycharm/installing-uninstalling-and-upgrading-packages.html) tutorial. 

## Credits
The idea to create his repo came from a [Sentinel](https://www.fowala.ch/) course I visited. We used some R scripts to manipulate the satellite imagery, but because I'm more experienced with python, I decided to rewrite a few of them and add my own. Big thanks go to ***Dominique Weber*** from [HAFL](https://www.bfh.ch/hafl/de) who wrote the R scripts, and was the major head behind the whole Sentinel course.

