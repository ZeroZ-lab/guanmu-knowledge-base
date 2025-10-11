# Version Control with Git

## 📋 Overview

**Topic**: Version Control with Git  
**Category**: Development Tools  
**Level**: Beginner to Intermediate  
**Prerequisites**: Basic command line knowledge  
**Estimated Time**: 2-3 hours

---

## 🎯 What You'll Learn

- What version control is and why it matters
- Basic Git concepts and workflow
- Essential Git commands
- Working with GitHub
- Best practices for commits

---

## 1. What is Version Control?

Version control is a system that records changes to files over time so you can recall specific versions later.

### Why Use Version Control?

✅ **Track Changes**: See what changed, when, and by whom  
✅ **Collaboration**: Multiple people can work on the same project  
✅ **Backup**: Your code is safely stored  
✅ **Experimentation**: Try new ideas without breaking working code  
✅ **Rollback**: Undo mistakes easily  

### Real-World Analogy

Think of it like:
- **Google Docs version history** - but for code
- **Video game save points** - you can go back
- **Time machine** - for your project

---

## 2. Git Basics

### What is Git?

Git is a distributed version control system. Created by Linus Torvalds in 2005.

### Key Concepts

#### Repository (Repo)
A folder that contains your project and its entire history.

#### Commit
A snapshot of your project at a specific point in time.

#### Branch
A parallel version of your code. The main branch is usually called `main` or `master`.

#### Remote
A version of your repository hosted on the internet (like GitHub).

---

## 3. Installation

### Windows
Download from [git-scm.com](https://git-scm.com/)

### macOS
```bash
# Using Homebrew
brew install git

# Or download from git-scm.com
```

### Linux
```bash
# Ubuntu/Debian
sudo apt-get install git

# Fedora
sudo dnf install git
```

### Verify Installation
```bash
git --version
```

---

## 4. Initial Setup

### Configure Your Identity

```bash
# Set your name
git config --global user.name "Your Name"

# Set your email
git config --global user.email "your.email@example.com"

# Check configuration
git config --list
```

---

## 5. Basic Git Workflow

### Step 1: Create a Repository

```bash
# Navigate to your project folder
cd my-project

# Initialize Git
git init
```

### Step 2: Check Status

```bash
# See what files have changed
git status
```

### Step 3: Stage Changes

```bash
# Stage a specific file
git add filename.py

# Stage all changes
git add .

# Stage multiple files
git add file1.py file2.py
```

### Step 4: Commit Changes

```bash
# Commit with a message
git commit -m "Add initial project files"
```

### Step 5: View History

```bash
# See commit history
git log

# Compact view
git log --oneline
```

---

## 6. Essential Git Commands

### Checking Status
```bash
git status              # See current state
git diff                # See unstaged changes
git diff --staged       # See staged changes
```

### Staging and Committing
```bash
git add <file>          # Stage specific file
git add .               # Stage all changes
git commit -m "message" # Commit with message
git commit -am "msg"    # Stage and commit (tracked files only)
```

### Viewing History
```bash
git log                 # Full history
git log --oneline       # Compact history
git log --graph         # Visual branch history
git show <commit-hash>  # Show specific commit
```

### Undoing Changes
```bash
git restore <file>      # Discard changes in file
git restore --staged <file>  # Unstage file
git reset HEAD~1        # Undo last commit (keep changes)
git reset --hard HEAD~1 # Undo last commit (discard changes) ⚠️
```

### Branching
```bash
git branch              # List branches
git branch <name>       # Create branch
git checkout <name>     # Switch to branch
git checkout -b <name>  # Create and switch
git merge <branch>      # Merge branch into current
git branch -d <name>    # Delete branch
```

---

## 7. Working with GitHub

### Create a Repository on GitHub

1. Go to [github.com](https://github.com)
2. Click "New repository"
3. Name your repo
4. Choose public or private
5. Click "Create repository"

### Connect Local Repo to GitHub

```bash
# Add remote
git remote add origin https://github.com/username/repo-name.git

# Verify remote
git remote -v

# Push to GitHub
git push -u origin main
```

### Clone a Repository

```bash
# Clone someone else's repo
git clone https://github.com/username/repo-name.git

# Clone to specific folder
git clone https://github.com/username/repo-name.git my-folder
```

### Push and Pull

```bash
# Push your changes
git push

# Pull latest changes
git pull

# Fetch without merging
git fetch
```

---

## 8. Common Workflows

### Daily Workflow

```bash
# 1. Start your day - get latest changes
git pull

# 2. Make changes to your files
# ... edit code ...

# 3. Check what changed
git status
git diff

# 4. Stage and commit
git add .
git commit -m "Describe your changes"

# 5. Push to remote
git push
```

### Feature Branch Workflow

```bash
# 1. Create a new branch for your feature
git checkout -b feature-login

# 2. Make changes and commit
git add .
git commit -m "Add login functionality"

# 3. Push feature branch
git push -u origin feature-login

# 4. Create Pull Request on GitHub

# 5. After merge, switch back and update
git checkout main
git pull
git branch -d feature-login
```

---

## 9. Best Practices

### Commit Messages

✅ **Good Commit Messages**:
```bash
git commit -m "Add user authentication"
git commit -m "Fix navbar overflow on mobile"
git commit -m "Update README with installation instructions"
```

❌ **Bad Commit Messages**:
```bash
git commit -m "changes"
git commit -m "fixed stuff"
git commit -m "asdf"
```

### Commit Message Guidelines

1. **Use the imperative mood**: "Add feature" not "Added feature"
2. **Be specific**: What did you actually change?
3. **Keep it concise**: Under 50 characters for first line
4. **Capitalize first letter**: "Add" not "add"

### When to Commit

- ✅ After completing a logical unit of work
- ✅ When the code works
- ✅ Before switching tasks
- ❌ Not after every single line
- ❌ Not when code is broken

### What to Commit

✅ **DO commit**:
- Source code
- Configuration files
- Documentation
- Scripts

❌ **DON'T commit**:
- Compiled binaries
- Dependencies (node_modules, venv)
- IDE-specific files
- Sensitive data (passwords, API keys)
- Large binary files

Use `.gitignore` to exclude these!

---

## 10. The .gitignore File

Create a `.gitignore` file to exclude files from Git:

### Python .gitignore Example
```
# Virtual environments
venv/
env/
.venv/

# Python cache
__pycache__/
*.pyc
*.pyo

# IDE
.vscode/
.idea/

# OS files
.DS_Store
Thumbs.db

# Environment variables
.env
```

### Where to Get .gitignore Templates

- [github.com/github/gitignore](https://github.com/github/gitignore)
- GitHub automatically suggests .gitignore when creating a repo

---

## 11. Common Problems and Solutions

### Problem: Forgot to Add .gitignore

```bash
# If you already committed files you shouldn't have:
git rm --cached <file>
git commit -m "Remove sensitive file"
```

### Problem: Wrong Commit Message

```bash
# Change the last commit message
git commit --amend -m "New message"
```

### Problem: Committed to Wrong Branch

```bash
# Move last commit to a new branch
git branch new-branch
git reset --hard HEAD~1
git checkout new-branch
```

### Problem: Need to Undo Last Commit

```bash
# Keep changes, undo commit
git reset --soft HEAD~1

# Keep changes, unstage them
git reset HEAD~1

# Discard everything (careful!)
git reset --hard HEAD~1
```

---

## 12. Useful Aliases

Add these to `~/.gitconfig` or use `git config --global alias.<name> <command>`:

```bash
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.cm "commit -m"
git config --global alias.last "log -1 HEAD"
git config --global alias.unstage "restore --staged"
```

Now you can use:
```bash
git st          # Instead of git status
git co main     # Instead of git checkout main
git cm "message" # Instead of git commit -m "message"
```

---

## 13. Quick Reference

### Most Used Commands

```bash
git init                    # Initialize repo
git clone <url>             # Clone repo
git status                  # Check status
git add <file>              # Stage file
git add .                   # Stage all
git commit -m "message"     # Commit
git push                    # Push to remote
git pull                    # Pull from remote
git log                     # View history
git branch                  # List branches
git checkout <branch>       # Switch branch
git checkout -b <branch>    # Create & switch
git merge <branch>          # Merge branch
```

---

## 📚 Learning Resources

### Interactive Tutorials
- [learngitbranching.js.org](https://learngitbranching.js.org/) - Visual, interactive
- [try.github.io](https://try.github.io/) - 15-minute tutorial

### Documentation
- [Git Official Documentation](https://git-scm.com/doc)
- [GitHub Guides](https://guides.github.com/)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

### Books
- **Pro Git** by Scott Chacon (Free online)
- **Git Pocket Guide** by Richard Silverman

### Videos
- Git Tutorial for Beginners - Corey Schafer
- Git and GitHub for Beginners - freeCodeCamp

### Cheat Sheets
- [GitHub Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [Atlassian Git Cheat Sheet](https://www.atlassian.com/git/tutorials/atlassian-git-cheatsheet)

---

## 🎯 Practice Project

### Mini Project: Personal Portfolio Repo

1. Create a new folder for your portfolio
2. Initialize Git
3. Create an HTML file (index.html)
4. Commit your changes
5. Create a GitHub account
6. Push to GitHub
7. Make changes locally
8. Commit and push again

This gives you:
- A Git repository to practice with
- A portfolio website hosted on GitHub Pages
- Real experience with the Git workflow

---

## 🔗 Related Topics

- [Clean Code Principles](./Clean-Code-Principles.md)
- [GitHub Actions and CI/CD](./GitHub-Actions-CICD.md)
- [Collaborative Development Workflow](./Collaborative-Development.md)

---

**Remember**: Git seems complex at first, but you'll use the same 10 commands 90% of the time. Practice regularly, and it becomes second nature!

