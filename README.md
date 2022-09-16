# dsa
This repo contains practice problems for Data Structures and Algorithms. Questions are taken from [here](https://takeuforward.org/strivers-a2z-dsa-course/strivers-a2z-dsa-course-sheet-2/)

## File creation steps in this repo
1. Clone this repo
2. Make a separate branch for each type of problems. e.g. branch 'sorting' for sorting problems.
3. Make a separate folder for subtopics on that branch, e.g. basic-maths
4. Make one more subfolder with name: 01_problem_name, e.g 03_find_second_largest_num
4. Filename should be like this: approach_1.py, approach_2.py etc.

e.g. a problem in binary trees, under subsection traversals, and problem name inorder_traversal, the steps should be:
 1. create branch "binary-trees"
 2. on that create folder traversals
 3. inside that folder create folder 01_inorder_traversal
 4. then create files named approach_1.py, approach_2.py in that

 ## Steps to create a branch
 1. Switch to main branch
    ```bash
    git checkout main
    ```
 2. Get first commit's hash and copy that
    ```bash
    git log --oneline --reverse
    ```
3. Create branch from copied commit's hash
    ```bash
    git branch branch_name commit_hash # create branch
    git checkout branch_name # switch to the branch
    ```
    or
    ```bash
    git checkout -b branch_name commit_hash # create and switch to that branch
    ```
## Steps to push a new branch to remote
1. Create one or more commits on the branch.
2. Push the branch
    ```bash
    git push --set-upstream origin branch_name
    # or
    git push -u origin branch_name
    ```
