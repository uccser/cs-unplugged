#!/usr/bin/env bash

# Function to reset a repo to a like-checkout state
# End result similar to 'git clone -b <branch> <remote_repo>'
# Usage: reset_repo <repo_dir> <branch>
#   repo_dir: path to repository to reset
#   branch: The branch to be on after the reset.
#           This branch must exist on origin, and will be checked out to the
#           current origin state.
#           All other local branches will be deleted.
reset_repo() {
    repo_dir=$1
    branch=$2

    git -C "${repo_dir}" fetch --prune
    git -C "${repo_dir}" reset --hard
    git -C "${repo_dir}" clean -d --force

    # Either create branch, or reset existing branch to origin state
    git -C "${repo_dir}" checkout -B "${branch}" "origin/${branch}"

    # Delete all local branches except for current branch
    if git -C "${repo_dir}" branch | grep -v "^*"; then
        git -C "${repo_dir}" branch | grep -v "^*" | xargs git -C "${repo_dir}" branch -D
    fi
}
