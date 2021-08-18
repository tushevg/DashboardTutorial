## Introduction to MarkDown

We need to use MarkDown to properly document. There are couple of useful features (e.g. adding links to URLs or code lines, integrating code and/or commands). Please go through the following [tutorial](https://www.markdownguide.org/basic-syntax) and try to rewrite some of the previous text.

# Example:

## clone repository from git

```
$ git clone https://github.com/tushevg/DashboardTutorial.git
```

## work on a shared repository
* every time before you start to work you need to **pull** the repository.
* when you introduce new changes you add a **commit** and **push** to the remote version. all other developers can check what you are working on


## create virtual environment

* prepare packages

```
$ sudo apt update
$ sudo apt upgrade
$ sudo apt install virtualenv
```

* work with [virtualenv](https://manpages.ubuntu.com/manpages/focal/man1/virtualenv.1.html)


```
$ cd DashboardTutorial
$ which python3
/usr/bin/python3
$ virtualenv -p /usr/bin/python3 venv
$ source venv/bin/activate
(venv) $ pip install --upgrade pip
(venv) $ pip install numpy
Collecting numpy
  Using cached numpy-1.19.5-cp36-cp36m-manylinux2010_x86_64.whl (14.8 MB)
Installing collected packages: numpy
Successfully installed numpy-1.19.5
(venv) $ pip list
Package       Version
------------- -------
numpy         1.19.5
pip           21.2.4
pkg_resources 0.0.0
setuptools    57.4.0
wheel         0.37.0
(venv) $ pip freeze > requirements.txt
(venv) $ cat requirements.txt
numpy==1.19.5
pkg_resources==0.0.0
(venv) $ deactivate
$
```

## create a gitignore file
[Gitignore](https://git-scm.com/docs/gitignore) is a file that specify which files/folders should not be tracked by git. The virtual environment folder is a good example of something that we don't need to track with Git and we don't need to upload to our repository. However, we need to keep track of the **requirements.txt** file. It contains all packages and versions that we need to recreate our project.

```
$ touch .gitignore
$ echo "venv" >> .gitignore
$ cat .gitignore
venv
$ git status
$ git add .
$ git commit -m "add gitignore file"
$ git push
```


<!-- this is a HTML Block Comment 

Git:
Since Git was already installed on the raspberry pi, I started by adding a username and my e-mail adresse to git.
Then I cloned the repository "https://github.com/tushevg/DashboardTutorial.git"
I continued by looking at the files in the repository and following the tutorial on "projects.raspberrypi.org/en/projects/getting-started-with-git". For Example I created this file, added it and wrote a commit.
I then created the virtual enviroment. After creating the virtual environment I tried to push the documentation file to GitHub with my Personal Access Token.
Virtual Environment:
I created a virtual environment which uses Python 3.7.3
I activated it and installed a package called "numpy" with pip. I also uninstalled it, installed an older version of it and then upgraded it to the newest version again to try out the commands.
-->