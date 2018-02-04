# My Pelican Blog on Github Pages

## Minimal Install

Here are the instructions I followed to get this running:

Note:
* Throughout this guide, substitute `username` with your actual Github username
* I'm assuming you'll be blogging in markdown (\*.md)
* Do not make any commits apart from the ones mentioned here atleast until the blog's finally running. I've messed up my setup multiple times trying out various commits, and had to start over. Ofcourse, if you know what you're doing, you don't need this advice.

### Github setup

1. Create a repo named `blog`
2. Clone that repo to your local machine: `git clone https://github.com/username/blog.git gh-pages`

### Anaconda environment

It's better to use virtual environments for specific use-cases. I'm creating one to use just for this blog. You can do similar things using `virtualenv` too if you prefer but I'm using Anaconda (conda):

```
conda create -n pelican-blog python=3
pip install pelican markdown
pip install ghp-import
```

To activate your conda environment: `source activate pelican-blog`
To deactivate your conda environment: `source deactivate`	

### .gitignore Setup

1. Run `ls -a` to see if there's a `.gitignore` file in your repo directory. If it isn't there, run `touch .gitignore`
2. Use your favorite text editor to edit the `.gitignore` file. Add the following:

```
# python files to be ignored
*.py[cod]

# directories to be ignored
output
```

### pelicanconf.py Setup

Run the following:
`pelican-quickstart`

**Pelican instructions to be added later**


Sources:
* https://gist.github.com/josefjezek/6053301
* http://docs.getpelican.com/en/3.6.3/quickstart.html
* https://github.com/getpelican/pelican/blob/master/docs/tips.rst
