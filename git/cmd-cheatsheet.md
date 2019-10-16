#### Getting started

```bash
# What version you installed
git --version

# Git configurations
git config --list

# Configure the git to add User and remote origin git server
git config user.name "Vikas Pandey"
git config user.email "vikiscripts@gmail.com"
git remote add origin https://github.com/hclpandv/devops-training-material.git
```

Verify if remote is added   

![image](https://user-images.githubusercontent.com/13016162/66889515-68c64000-f000-11e9-8b13-97affdda0c4f.png)

#### Workflow

```bash
# Clone an existing hosted repository
git clone https://github.com/hclpandv/devops-training-material.git

# Clone a specific branch to a specified directory path
git clone --single-branch --branch my_target_branch https://github.com/hclpandv/devops-training-material.git my_target_dir_path

# Initialize a git repository on current dir
git init
# Or to a new dir to be created and initialized
git init repo_dir_name

# Check the current branch (by default 'master' branch is created when you initialize a repository)
git branch
# Get all the branches including the ones on remote origin 
git branch --all

# Create & switch to the new branch
git checkout -b my_new_branch_name

# Up-stream newly created branch to remote origin
git push --set-upstream origin my_new_branch_name

# Fetch all the remote branches
git fetch --all

```
