# Introduction to Azure Machine Learning Service

Azure Machine Learning service provides SDKs and services to quickly train and deploy machine learning models, improve productivity and costs with autoscaling compute & pipelines. Use these capabilities with open-source Python frameworks, such as PyTorch, TensorFlow, and scikit-learn.

Full documentation is available at https://docs.microsoft.com/en-us/azure/machine-learning/.

In order to take advantage of the wide array of functionalities that Azure ML Service provides, first the service must be provisioned in Azure.

## Provisioning Azure ML Service

To provision the Azure ML Service, navigate to the following URL and log in using your company or personal account: http://portal.azure.com.
**Note that in order to be able to follow the steps outlined below, you need to have sufficient permission in an Azure subscription of your choice to deploy new resources.** If you don't know whether you have the required permissions or not - you are about to find out ... :wink:

1. In the Azure Portal, click the "Create a resource" button located in the top left corner.

<img src = "/images/create-resource.jpg" width = 150>

2. In the search box that appears, search for "machine learning"

3. Select the "Machine Learning" tile

<img src = "/images/create-aml.jpg" width = 300>

4. Click the blue "Create" button

<img src = "/images/create-aml2.jpg" width = 300>

5. You will now need to fill in some information to configure your Azure ML Service.

<img src = "/images/aml-details.jpg" width = 600>

* Type in a workspace name for your workspace. This name you will use in later stages of the labs when interacting with components from the Azure ML Service.

* A Resource group combines various Azure assets into a logical container. This will facilitate clean-up activities once the lab is completed. It is recommended to create a new resource group for this purpose. To do so, click the Create New link and name the resource group.

* Location simply specifies in which Azure data center will be provisioned. Unless otherwise instructed by the lab proctors, please select West Europe in order to reduce network latency.

* To initiate the deployment process, click the blue Create and Review button followed by Create. The provisioning will now start and the Azure ML Service will be deployed as per your specification.

* Ensure that you specify Enterprise for the workspace edition to benefit from the full set of functionality. More information on which features are available in basic vs. enterprise edition can be found [here](https://azure.microsoft.com/en-us/pricing/details/machine-learning/).

<img src = "/images/create-button.jpg" width = 75>

You can now click the bell icon in the navigation bar across the top of the Azure portal where you will see that the deployment is under way.

<img src = "/images/notification-deployment.jpg" width = 400>

This process will typically only take 2-3 minutes to complete. Once completed, you will be able to click the blue **Go to Resource** button as shown below which will take you to the main site of the Azure ML Service.

<img src = "/images/deploy-complete.jpg" width = 400>

On the Overview page of the newly provisioned Azure ML Service, now click the following button to be taken the Azure ML studio environment:

<img src = "/images/launch-now.jpg" width = 600>

## Navigating Azure ML Studio

Over the course of the following labs, you will use various aspects of the Azure ML studio. The main navigation elements are displayed on the left. Please note that in your environment the lower middle part of the screen will be empty since you have just now created your Azure ML studio.

<img src = "/images/aml-studio-home.jpg" width = 700>

This is the top-level resource for Azure Machine Learning service, also referred to as the Azure ML workspace, providing a centralized place to work with all the artifacts you create when you use Azure Machine Learning.
The taxonomy of the workspace is best explained in the following screenshot and more information can be found in [this article](https://docs.microsoft.com/en-us/azure/machine-learning/concept-workspace).

### Author

In the **Author section**, which is currently still in preview, you will find 3 utilities to author new machine learning experiments.

#### 1 Automated ML

Automated machine learning, also referred to as autoML, is the process of automating the time consuming, iterative tasks of machine learning model development. It allows data scientists, analysts, and developers to build ML models with high scale, efficiency, and productivity all while sustaining model quality. Automated ML is based on a breakthrough from Microsoft Research.

Traditional machine learning model development is resource-intensive, requiring significant domain knowledge and time to produce and compare dozens of models. Apply automated ML when  you want Azure Machine Learning to train and tune a model for you using the target metric you specify. The service then iterates through ML algorithms paired with feature selections, where each iteration produces a model with a training score. The higher the score, the better the model is considered to "fit" your data. With automated machine learning, you'll accelerate the time it takes to get production-ready ML models with great ease and efficiency.

#### 2 Noteboks

In this section you will find all Notebook files created in any of the Compute Instances that are hosted in an Azure ML Compute Instances. The Compute Instance itself can be created and managed in the “Manage” Section under “Compute” – “Compute Instance”

#### 3 Designer

This is a graphical, drag-and-drop UI that allows people unfamiliar with ML programming languages such as python to develop machine learning models in a visual manner, without writing any code. This functionality has long been available under the name of Azure ML Studio (classic) and is currently being ported into the Azure ML Service. Once feature complete, it will have all the capabilities of its predecessor but without any limitations on the size of datasets that can be processed plus full control over where the computation/processing should happen. 

For more information on the visual interface, please refer to [this article](https://docs.microsoft.com/en-us/azure/machine-learning/concept-designer).

### Assets

This is where the workspace keeps – among other things – a history of all training runs, including logs, metrics, output, and a snapshot of your scripts. You can use this information to determine which training run produces the best model. 

A machine learning  project within your company will usually bring with it at least one experiment in which data scientists will try to train a suitable machine learning algorithm for a given problem. Typically, this requires multiple runs during which various outputs can be tracked such as the model’s performance metrics. Logging these metrics will enable the data scientist to never lose track of which combination of features and algorithms has yielded the best performance.

Metrics of interest can be logged from experiments being run in python code but also for experiments that are run in the Visual Interface are the Automated Machine Learning UI.

## Conclusion

In this lab you have set up your own Azure ML studio which provides the fundament for the future labs. We have also provided a brief overview of some of the most important components and concepts in Azure ML. Feel free to review this document at a later point in time in case of conceptual questions. 

## Next steps

You may now close this document and navigate back to the [main page](README.md) and open the next document for lab #1 in which you will explore Azure ML Designer. Alternatively, you can navigate directly to [Lab 1 - Creating a first experiment with Azure ML Designer](1_Designer.md)