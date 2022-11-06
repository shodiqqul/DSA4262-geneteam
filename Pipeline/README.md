# Using Pipeline for Model Training and Predicting

## 1. Create Virtual Environment
**1. Install/Upgrade _pip_ and _virtualenv_**

```
$ python3 -m pip install --user --upgrade pip

$ python3 -m pip install --user virtualenv
```

If you are running on Ubuntu, you may need to install _pip_ and _virtual_env using the ```sudo``` command.

```

**2. Create a new virtual environment**

```
$ python3 -m venv <environment name>
```

Change ```environment name``` to a name of your choice.
Example: ```$ python3 -m venv geneteam```

**3. Activate virtual environment**

```
$ source <environment name>/bin/activate
```

Example: ```$ source geneteam/bin/activate```

## 2. Setup Virtual Environment
**1. Change to a working directory of your choice**

```
$ cd/<working directory>
```
Set ```working directory``` to a directory of your choice.
Example: ```$ cd/Desktop```

**2. Clone GitHub repository**

```
$ git clone https://github.com/shodiqqul/DSA4262-geneteam.git
```
This entire GitHub repository will appear in your specified working directory.

**3. Go to the _Pipeline_ folder in the working directory**

```
$ cd ./DSA4262-geneteam/Pipeline
```

**4. Install the required dependencies from _requirements.txt_**

```
$ python3 -m pip install -r requirements.txt
```

## 3. Model Training (Optional)
This step may be skipped as the model has already been trained.

To train the model, run:
```
$ python data_preprocessing.py <info file path> <json file path>

$ python feature_engineering.py

$ python model_training.py
```

**Inputs:**
- An ```info``` file and a ```json``` file. Both files should already exists in directory e.g. ```/DSA4262-geneteam/Pipeline/```

**Outputs:**

There will be intermediate ```csv``` files that are created but you may ignore them.
- A ```csv``` file with data that has been preprocessed (intermediate)
- A ```csv``` file with data that has been feature engineered (intermediate)
- A ```ubj``` file that is a saved version of the trained model (final output)


## 4. Model Predicting with XGBoost

```
$ python model.py <json file path>
```

A sample test dataset has been provided - **test_data.json**

Run it with:

```
$ python model.py ./data/test_data.json
```

**Inputs:**
- A ```json``` file containing the test dataset.

**Outputs:**
- A ```csv``` file, ```results.csv``` with the **prediction probabilities**, **transcript ID** and **transcript position**
- Found under a new subdirectory: ```/Pipeline/results/results.csv```


