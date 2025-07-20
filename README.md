# Welcome to the physical oceanography model of the Ocean Margins Initiative at COESSING 2025! 
We're going to be looking at **real** data from the ocean (pretty cool) to investigate the interaction between biological and physical processes off the coast of Ghana. There are two notebooks in this repository we'll be using: 
- `data_analysis.ipynb`: an introduction to using Python for physical oceanographic data analysis, including tools like **xarray** and the Gibbs Seawater Toolbox, **gsw**.
- `biophysical_modeling.ipynb`: A simplified model that we'll use to explore nutrient-phytoplankton dynamics and make comparisons to observational data. 

There are three ways to access the notebooks - feel free to choose whichever method you feel most comfortable with—we’ll be available to help at the start of the workshop no matter what.

---
## Option 1: Access the notebooks **online** (easiest)

No installation required! Just click the link below and the notebooks will launch in an external browswer window with all packages pre-installed.

[link]

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jvynn/coessing-2025/HEAD?urlpath=%2Fdoc%2Ftree%2Fdata_analysis.ipynb)

Note this options requires a stable internet connection.

## Option 2: Load the notebooks into the JupyterLab desktop application

This repository can be downloaded locally and run in the JupyterLab desktop application. 

### Step-by-step instructions:

1. **Install JupyterLab desktop application**
    Just choose the right installer from the links on this Github

1. **Download the repository**
    If you're not familiar with Git, the easiest way is to [download the ZIP](https://github.com/jvynn/coessing-2025/archive/refs/heads/main.zip) and extract it somewhere on your computer (e.g., your Documents folder)

1. **Open JupyterLab Desktop and launch a terminal**
    - Open the **JupyterLab Desktop App**
    - From the main launcher, click **"Open File..."** and browse for the location you extracted this repository. Open either `data_analysis.ipynb` or `biophysical_modeling.ipynb`. 
    - Click the big blue button on the left with a plus mark in the middle to access the Launcher. If it's not visible, click **"View"** and **"Show Left Sidebar"** and it should appear.
    - From the Launcher, click **"Terminal"** under the "Other" section

1. **Create and activate the Conda environment**
    The terminal prompt should open in the same folder location as the notebooks. Run the following command:
   ```bash
   conda env create -f environment.yaml
   ```
   It will take a few minutes! Then activate the environment with will command:
   ```bash
   conda activate coessing-2025
   ```

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

1. **Launch JupyterLab**
    ```bash
    jupyter lab