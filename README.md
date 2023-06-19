Data processing workflow
--------------------------

This project contains several scripts:
- data processing workflow for given datasets with `src/data_workflow_main.py` file as entry point
- data fusion with filtering too bright images and images with large relative head size with respect to image size in the `src/data_fusion_main.py` file as entry poiny
- 2 histogram visualizations within jupyter notebook in `src/histograms.ipynb`

## Prerequisites
You need to have installed `python3.10`.
Assure in root folder, you created `data` folder where you placed your data to be processed. E.g. `lfw` dataset placed into `data/lfw/<its content>`

## How to 
### Develop

Go to root directory and type following command in terminal:
```
make venv & source .venv/innovatrics_assignment/bin/activate
```
It will install all necessary dependencies for you into `innovatrics_assignment` virtual environment. Get to  virtual env with executing following command
```
source .venv/innovatrics_assignment/bin/activate
```
and from now on, you can use this virtual env for further developing.


**Note**: If you want to manually install all dependencies, go to project root directory and execute command
```
make reqs
```

### Run script
As first, exec to virtual env as defined above
#### Data workflow pipeline
Go to `src` directory and run `python data_workflow_main.py` with corresponding parameters. To figure out which parameters to use, type 
```
python data_workflow_main.py --help
```

For now, we support following values:
- **dataset type** (str): one of following values: [lfw, celeba]
- **convert to image format** (str): one of following values: [jpg, png]
- **results file path** (str): as suffix of file path, you can define compression type from one of the values [.tar, .tar.gz, .zip]
- **compress quality** (str): any value from range <0;100>

After script finish, you can find your normalized results in the path, you defined for `result_path` argument and randomly selected images can be found in `DEBUG` folder.

#### Data fusion script
Prerequisity for running this script is to execute successfully `Data workflow pipeline` script at least 1 time. Go to `src` directory and run `python data_fusion_main.py` with corresponding parameters. Script requires 2 parameters:
- **input file path** (str): relative path to CSV file from which filtering of data should happen. (E.g. you can point to final `dataset_labels.csv` file). This path must be relative and base starts in project root directory level
- **output file path** (str): relative path to folder where normalized (result images from `data_workflow_pipeline`) filtered images will be placed. Folder will contain **good** folder with good images (not too bright, etc.) and **bad** folder with images filtered out. This path must be relative and base starts in project root directory level

#### Histograms
Prerequisity for running this script is to execute successfully `Data workflow pipeline` script at least 1 time for lfw and celeba dataset. Update relative path for variable `file_path` correspondingly (pointing to `dataset_label.csv` in your folder system), then go to `src` directory and open `histograms.ipynb` jupyter notebook. Run all cells. After that you will see 2 expected histograms
### Run tests
Go to root directory and run command
```
tox tests
```

If you have any questions, contact me on email: zakyz.martin@gmail.com
<3