[<<Back](index.md)
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

#### Create and manage local git repository

```bash
# Initialize a git repository on current dir
git init
# Or to a new dir to be created and initialized
git init repo_dir_name

# Create & switch to the new branch (by default 'master' branch is created when you initialize a repository)
# Use checkout to switch among local branches
git checkout -b my_new_branch_name

# Up-stream newly created branch to remote origin
git push --set-upstream origin my_new_branch_name
```
get local branches including current branch  
![image](https://user-images.githubusercontent.com/13016162/66890642-682fa880-f004-11e9-833f-314311408ec9.png)

#### Work on your content

```bash
# Get git status to observe
git status

# Add new files to stage to track changes
git add name_of_file
# or all files including sub dirs
git add .

# Commit the changes
git commit -m "my commit message"

# Push the changes to remote origin
git push origin my_branch
# or simply
git push

# Pull the changes from remote origin typically changes by others
git pull origin my_branch
```


#### Hosted Remote Repositories 

```bash
# Clone an existing hosted repository
git clone https://github.com/hclpandv/devops-training-material.git

# Clone a specific branch to a specified directory path
git clone --single-branch --branch my_target_branch https://github.com/hclpandv/devops-training-material.git my_target_dir_path

# Get all the branches including the ones on remote origin 
git branch --all

# Fetch all the remote branches
git fetch --all
```
#### Git logs

```bash
# Get logs of all commits within repository
git log

# Create an Alias for nicely decorated graphed Log
alias git-graph="git log --all --decorate --oneline --graph"
```

#### File permission with git

```bash
# check the existing permissions by the file using the following command, permissions like 100644
git ls-files --stage 
# Modify as below
git update-index --chmod=+x 'name-of-shell-script'
```
