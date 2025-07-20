# Welcome to the physical oceanography model of the Ocean Margins Initiative at COESSING 2025! 
We're going to be looking at **real** data from the ocean (pretty cool) to investigate the interaction between biological and physical processes off the coast of Ghana. There are two Jupyter notebooks in this repository we'll be using: 
- `data_analysis.ipynb`: An introduction to using Python for physical oceanographic data analysis, including tools like **xarray** and the Gibbs Seawater Toolbox, **gsw**.
- `biophysical_modeling.ipynb`: A simplified model that we'll use to explore nutrient-phytoplankton dynamics and make comparisons to observational data. 

There are two ways to access the notebooks. Feel free to choose whichever method you feel most comfortable with—we’ll be available to help at the start of the workshop no matter what.

---
## Option 1: Access the notebooks **online** (easiest)

No installation required! Just click the link below and the repository will launch in an external browswer window with all packages pre-installed.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jvynn/coessing-2025/HEAD?urlpath=%2Fdoc%2Ftree%2Fdata_analysis.ipynb)

Note this options requires a stable internet connection.


## Option 2: Install python and setup the **Conda environment** locally (intermediate)

This method may be preferable if you're familiar with Python and the terminal interface since it gives you the most control. It also more closely aligns with the workflows we commonly use in scientific computing! It requires you to install Anaconda, which includes Python and a package manager in one download.

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
   conda env create -f environment.yml
   conda activate coessing-2025
   ```
   You should see your environment change from `(base)` to `(coessing-2025)`

1. **Launch JupyterLab**
    
    Once the environment is activated, run:
    ```bash
    jupyter lab
    ```
    This will launch the JupyterLab server locally and open your web browser automatically at ``http://localhost:8888/lab``. If it doesn't automatically open, you can paste it in. 

1. **Choose the right kernal and open the notebooks** 

    Explore the JupyterLab interface - it's takes a moment to get used to but is fairly intuitive! Make sure your notebook is using the correct Python kernel.
    - Look at the top right corner of the notebook (shows the current kernel name).
    - Click the kernel name and choose ``"Python (coessing-2025)"`` if it’s not already selected.

    If the kernel doesn’t appear, register it (see below).

1. **(Optional) Register your Conda environment as a kernel**

    If the ``coessing-2025`` environment is not listed, run the following command once and restart JupyterLab
    ```bash
    python -m ipykernel install --user --name coessing-2025 --display-name "Python (coessing-2025)"
    ```