# Lab 2 - Working with Compute Instances

One of the most useful aspects of an Azure ML studio is its ability to do logging of measures of interest which will be covered in the next lab. Through this, for example, it is  ossible to log how a model's performance metrics develop iteration by iteration.

Before taking advantage of this capability, however, we will set up a Compute Instnace to run our python code in. Even though all the features of Azure ML could be worked with from a local python runtime on your machine, for the purpose of this series of labs we will work with the Compute Instance to ensure all participant run the same version of python and the libraries required. 

## Setting up a Compute Instance

For the purpose of this lab, we will work with the Azure ML's [Compute Instance](https://docs.microsoft.com/en-us/azure/machine-learning/concept-compute-instance). Compute Instances are fully managed cloud based data science workstations that include Jupyter Notebook, JupyterLab as well as RStudio to write code in. On top of that, they offers a simple setup, integration with Active Directory for single sign-on (SSO) and the azureml python libraries already pre-installed. 

To set up a Compute Instance, click “Compute” in the “Manage” section of the Azure ML studio.

<img src = "/images/manage-compute.jpg" width = 150>

Ensure you are in the “Compute instances” tab. Then, click the New button to add a new Compute Instance to your workspace.

<img src = "/images/new-ci.jpg" width = 300>

Specify a name for your Compute Instance and choose a VM size that is suitable for the volume and complexity of your dataset as well as your models. Please **note that the name of the Compute Instance must be unique within an Azure region.** Hence, you may not use the same names shown in this document or that is used by your neighbor.

<img src = "/images/ci-details.jpg" width = 700>

Click the VM type drop-down to browse the list of all available VM sizes and select a VM size different from the default. In general, consider the data volume available for training and compare it to the amount of memory (RAM) the VM has available as python will attempt to hold the entire dataset in memory to speed up computations. Also, consider using VM types that include GPUs when expecting to train large deep neural networks to speed up training times. 

Note that bigger VMs with more memory and CPUs will result in higher charges to your Azure subscription. More information on VM pricing can be found here. The default VM size STANDARD_D3_V2 with 4 vCPUs and 14 GB of RAM will suffice for our lab. Please also ensure that you choose a VM size for which you still have quota left. In case you choose a VM type with 0 quota left, the provisioning will fail.

<img src = "/images/ci-vm-sizes.jpg" width = 700>

Once an appropriate VM type has been selected, click the blue Create button to start the deployment process for the Compute Instance. 

<img src = "/images/create-ci.jpg" width = 75>

When the status has changed from *Creating* to *Running*, you may proceed to the next paragraph. If for whatever reason the status shows as *Stopped*, you can start the Compute Instance by selecting it to the left of the name column and then clicking **Start** from the menu bar above. 

Lastly, when the status of the Notebook VM has changed to Running, click the Jupyter hyperlink that has now appeared. This will launch a separate browser tab or window that will bring you directly to the Jupyter Notebook environment of your Compute Instance.

<img src = "/images/jupyter-link.jpg" width = 600>

This should bring you to the Jupyter Notebook home page. Note that the Notebook VM also features an instance of R Studio. For this series of labs the focus will remain on python. 

<img src = "/images/jupyter-home.jpg" width = 600>

## Adding required content to Jupyter Notebooks

Whilst you may also upload content manually via the Jupyter Notebook home page, the fastest way load all required content for this lab is by cloning this very git repository. 

To do so, click the *New* button in the top right corner of the Jupyter home page and then select *Terminal*. This will open a separate tab in your browser with a terminal window. Once the terminal is ready, type in the following command and hit the *Enter* key on your keyboard to start the process:

```
git clone https://github.com/marcscho/amllab
```

## Next Steps

From your Jupyter Notebook home page, please open the notebook entitled 3_Training_and_Logging.ipynb and follow the instructions provided therein to build your first python based ML model of the day.

Please go through all the notebooks cell by cell and don’t run everything at once – your learning experience will be orders of magnitude greater. 

If this is your first time working with Jupyter Notebooks, note that you can run the code within an individual cell and advance the cursor to the next cell with Shift + Enter on your keyboard. A cell can contain multiple lines of code, all of which will be executed when Shift + Enter are pressed. Alternatively, you can press Ctrl + Enter to also run a cell but not advance the cursor.