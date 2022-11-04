**DSA4262 Project**

1. Open your Command Line Interface (CLI) in the Python folder directory

2. Create new folder for project `project-name` using the following command:
> `mkdir project-name`

3. Within the newly created project folder `project-name`, create a `data` subfolder:
> `cd project-name`

> `mkdir data`

3. Download python file `model.py` and save file in `project-name/data`

4. Save all `data.json` files within same directory

5. Run the following commands in CLI to install the relevant dependencies needed:
> `pip install category_encoders`
> `pip install joblib`
> `pip install xgboost`

6. Run the following code in CLI to get the probabilities of an m6a modification at each transcript where `file-name` is the name of the data.json file you wish to attain the scores for:
> `python model.py file-name`

**Authors**

Group GeneTeam:

- AHMAD AS-SHODIQQUL AMIN B M T
- DIONE LIM YEE SZE
- KEITH TAY XIANG RUI
- MADHU BHARATHI ELANGO
- Database: Python
