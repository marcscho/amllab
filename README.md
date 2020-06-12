# Azure ML End-to-end lab

This repository provides the required instructions and code pieces (Jupyter Notebooks) for the Azure ML hands-on labs. 

Feel free to clone or fork as a working head start for training your own model.

## Azure ML labs

The lab includes the following sections:

* [Introduction to Azure ML and setting up workspace](0_Intro_Azure_ML.md)
* [Lab 1 - Creating a first experiment with Azure ML Designer](1_Designer.md)
* [Lab 2 - Creating a Compute Instance](2_Compute_Instance.md)
* [Lab 3 - Creating a dataset](3_Creating_dataset.ipynb)
* [Lab 4 - Model training and experiment logging](4_Model_Training_and_Experiment_Logging.ipynb)
* [Lab 5 - Automated ML on Remote Compute](5_AutoML_Remote_Compute.ipynb)
* [Lab 6 - Model deployment](6_Deploy.ipynb)

Go ahead and click the first link of the list above to start with your first lab! Once you have completed all labs, feel free to come back to this page and try out the optional labs below.

## Optional labs

### Fairlearn

If you are interested in the topic of responsible ML, then check out [Fairlearn on GitHub](https://github.com/fairlearn/fairlearn). To get started, run the following command in a terminal window inside your Compute Instance's Jupyter Notebook:

```
git clone https://github.com/fairlearn/fairlearn
```

To get an understanding of Fairlearn's capabilities, run through the notebook entitled **Grid Search for Binary Classification.ipynb** which includes a similar dataset to the one you have used in prior labs. 

In case you run into issues, consider executing the two following commands in individual notebook cells and afterwards restarting the notebook kernel.

```
!pip install fairlearn --no-dependencies
```

```
!pip install --upgrade sklearn --force
```

## Clean up

**At the end of the lab, please make sure you follow the instructions for [cleaning up your environment](Clean_up.pdf). This will make sure you will not incur any further charges after the lab.**

Note that you may skip the first section of deleting a Databricks cluster if you haven't provisioned one in the previous labs. 

## Disclaimer

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
