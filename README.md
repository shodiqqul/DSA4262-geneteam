**DSA4262 Project**

1. Open your Command Line Interface (CLI) in the Python folder directory

2. Create new folder for project `project-name` using the following command:

`mkdir project-name`

3. Within the newly created project folder `project-name`, create two subfolders named `data` and `results`:

`cd project-name`

`mkdir data`

`mkdir results`

3. Download python file `model.py` and save file in `project-name`

4. Download the test file `test_data.json` and save it within the `data` subfolder

5. Run the following commands in CLI to install the relevant dependencies needed:

`pip install category_encoders`

`pip install joblib`

`pip install xgboost`

`pip install -U imbalanced-learn`

6. Change your directory to your project folder `project-name`

7. Run the following code in CLI to get the probabilities of an m6A modification at each transcript with the test data set:

`python model.py ./data/test_data.json`

8. If executed correctly, CLI prints "Done!"

9. The results of the model will be in the `results` subfolder

**Authors**

Group GeneTeam:

- AHMAD AS-SHODIQQUL AMIN B M T
- DIONE LIM YEE SZE
- KEITH TAY XIANG RUI
- MADHU BHARATHI ELANGO
- Database: Python
