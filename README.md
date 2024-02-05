# Matrix Calculator

## Environment Preparation

you would need to make sure you have python 3.9+ installed

### Create a Virtual Environment for the project(Optional):
Inside the project folder run the following command:
```commandline
python -m venv .venv
```

To activate the virtual environment, open a command line in the project folder and execute the following:

Windows:
```commandline
.venv\Scripts\activate.bat
```

Mac/Linux:
```commandline
source .venv/bin/activate
```

To deactivate the virtual environment
```commandline
deactivate
```

### Install dependencies using pip
if you chose to use a virtual environment, please *activate* it before proceeding

Install the project dependencies from requirements.txt using the following command:
```commandline
pip install -r requirements.txt
```

Note for linux users:
You may need to install xclip(outside venv)

fedora:
```commandline
sudo dnf install xclip
```

debian:
```commandline
sudo apt install xclip
```

please see:
https://pyperclip.readthedocs.io/en/latest/#not-implemented-error
for more info

## Running the project
if you are using virtual environment, please activate it first. then run:
```commandline
python main.py
```