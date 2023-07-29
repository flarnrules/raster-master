# raster-master
some code to mess around with images

## File Structure

Here's the basic file structure for this repo:

```bash
raster-master
│   README.md   
│
└───image_to_ascii
│   │   image_to_ascii.py
│   │   requirements.txt
│   │   env (your venv directory for image_to_ascii)
│   
└───image_collage
    │   image_collage.py
    │   requirements.txt
    │   env (your venv directory for image_collage)
```

## Virtual Environments

I still don't remember every time how virtual environments work, so I'm going to create step by step instructions on how to set one up, enter and exit one.

### Setting Up a Virtual Environment

1. Create virtual environments for each sub project. The current `raster-master` repo has two sub projects:

**For the subdirectory `image collage`:**
- `cd image_collage`
- `python3 -m venv image_collage_env`

**For the subdirectory `image_to_ascii`:**
- `cd image_to_ascii`
- `python3 -m venv image_to_ascii_env`

2. Source the setup_env.sh script that makes activating the environments easier:
- `cd ..`
- `source setup_env.sh`

3. Activate the virtual environment in the subdirectory you want to use:
- `cd image_to_ascii`
- `activate_image_to_ascii` 

When the virtual environment is activated, you'll see `(env)` in front of the command prompt.

4. Install all packages for that repo to get the current venv up to speed.

```bash
pip install -r requirements.txt
```

<p style="text-align: center">OR</p>



4. Install new packages and then update the `requirements.txt` file with:

```bash
pip freeze > requirements.txt
```



### Using the Virtual Environment

1. Ensure that the virtual environment is active (you will see the `(env)` in the command prompt).

2. If installing other dependencies while working on the project, make sure to update the `requirements.txt` file with:

```bash
pip freeze > requirements.txt
```


### Deactivating the Virtual Environment

When finished working on the project, deactivate the virtual environment with: `deactivate`


### Other Notes on Virtual Environments for This Repo

The virtual environment names for this project are:
- for the `image_collage` module: `image_collage_env`
- for the `image_to_ascii` module: `image_to_ascii_env`

To activate these virtual environments, first source the `setup_env.sh` file located in the root `raster-master` direcory.

Then, depending on what project we are working on, activate the virtual environment with either:
- `activate_image_to_ascii` OR
- `activate_image_collage`

### Quickly Install the Requirements of the Project

When working on another computer, remember to use the following command to install the requirements once the virtual environment is active and once in the proper directory:

```bash
pip install -r requirements.txt
```