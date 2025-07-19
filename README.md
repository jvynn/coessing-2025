# Welcome to the physical oceanography model of the Ocean Margins Initiative at COESSING 2025! 
We're going to be looking at **real** data from the ocean (pretty cool) to interrogate biophysical processes at play off the coast of Ghana. There are two notebooks in this repository we'll be using: `data_analysis.ipynb` and `biophysical_modeling.ipynb`. The former includes an introduction to using phython for physical oceanographic data analysis while the latter is a modeling of phytoplankton-nutrient dynamics that we'll compare to observational data. 

There are three ways to access the notebooks - feel free to choose whichever method you feel most comfortable with—we’ll be available to help at the start of the workshop no matter what.

---

## Option 1: Access the notebooks **online** (easiest)

No installation required! Just click the link below and the notebooks will launch in an external browswer window - all packages pre-installed.

[link]

## Option 2: Load the notebooks into the Jupyter Lab desktop application

This repository can be downloaded locally and run in the Jupyter lab desktop application.

## Option 3: Install python and setup the **Conda environment** locally (for intermediate/advanced users)

This method may be preferable if you're familiar with Python and the terminal interface since it gives you the most control. It requires you to install Anaconda, which includes Python and a package manager in one download.

### Step-by-step instructions:

1. **Install Anaconda**  
   Download and install Anaconda for your system:  
   🔗 [https://www.anaconda.com/download](https://www.anaconda.com/download)

   If you're new you can check out these video walkthroughs:  
   - [Windows installation](https://www.youtube.com/watch?v=4DQGBQMvwZo&t=606s)  
   - [Mac installation](https://www.youtube.com/watch?v=0Hhqf8L-b_0)

1. **Download the repository**  
   - Either [download the ZIP](https://github.com/jvynn/coessing-2025/archive/refs/heads/main.zip) and unzip it,  
   - Or clone the repo using Git:
     ```bash
     git clone https://github.com/jvynn/coessing-2025.git
     ```

1. **Open a terminal (or Anaconda Prompt)** and navigate to the folder with the environment file.

1. **Create and activate the Conda environment**  
   Run the following commands:
   ```bash
   conda env create -f environment.yaml
   conda activate coessing-2025
   ```
   You should see your environment change from `(base)` to `(coessing-2025)`

1. **Launch Jupyter Lab**
    ```bash
    jupyter lab