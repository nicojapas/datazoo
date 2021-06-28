# Applicant Task: Forecast Visualization 

## Directory Layout

- The `notebooks` folder includes a Jupyter notebook where the three small tasks reside.
- The `visualization` forder is an empty directory. In this directory you should later generate the widgets plugin.
- The `data` folder contains the example data as starting point of our tasks.

We have added a class `ArtificialDatasets`. The method `create_multiple_timeseriesset` in this class will create the artificial dataset for this task.

## What to do?

#### Step 1: Create Conda Environment

Create the `conda` environment. We recommend to install [miniconda](https://docs.conda.io/en/latest/miniconda.html), if you do not have an existing conda installation.

```
conda env create -f environment.yaml
```

Activate the installed `conda` environment.
```
conda activate visualization_task
```

Start Jupyter lab and examine the given time series (Optional):
```
jupyter lab
```

#### Step 2: Implement data merging in notebook `01_data_preparation`
In the notebook use pandas to fill cell no. 5. with suitable code. The `asserts` in the following cells should pass and the data look like at the end of the notebook.


#### Step 3: Visualize the merged data with plotly in `02_visualization`
In the second notebook you should visualize the data we prepared in the first notebook. In case we had problems with the first task you find a combined example in `"data/test.parquet"`. 
[Plotly](https://plotly.com/python/) to visualize the data. In the interview you explain a little bit your thoughts about technology, but also user experience. 


#### Step 4: Create a custom Jupyter widget in `03_widget`
We highly depend our frontend development on the Jupyter environment. This environment is highly extensible via extensions and widgets. In your task you should create a customer
[Jupyter widget](https://github.com/jupyter-widgets/ipywidgets) in the `visualization` directory. You don't have to start from scratch, and rather use the [Typescript cookiecutter](https://github.com/jupyter-widgets/widget-ts-cookiecutter)
the project provides.

You finished the task, when in the notebook `03_widget` your widget is rendered correctly. 
**If this was way too easy for you, could you change the widget, such that it renders a link instead of a "Hello World" text?**. In the interview we will ask you to explain the functionality of the widget with regards to web technology 
a little bit.

#### Step 5: Push your solution to your favorite repository
The original repository is used as the base repository for applicant tasks and no solutions should be pushed there. 
Therefore, please create an own repository (on e.g. [GitHub](https://github.com), [Bitbucket](https://bitbucket.org) or [Gitlab](https://gitlab.com)) for your solution and push it there. 

#### Step 6: Clean your environment (optional)
```
conda remove -n visualization_task --all
```


