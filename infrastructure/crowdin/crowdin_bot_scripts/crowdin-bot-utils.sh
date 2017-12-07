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

# Function to unstage any staged .po files that only have trivial changes
# to timestamp metadata.
# This is achieved by checking the diff with HEAD, excluding any lines starting
# with PO-Revision-Date or POT-Creation-Date
# NB: Must be run from the repo root directory
reset_po_files_timestamp_only() {

  if ! [[ $(git rev-parse --show-toplevel 2>/dev/null) = "$PWD" ]]; then
    echo "Error: reset_po_files_timestamp_only must be run from the repository root directory"
    echo "Root:    $(git rev-parse --show-toplevel 2>/dev/null)"
    echo "Current: $(pwd)"
    echo "Aborting...."
    return 1
  fi

  # Loop through each .po file:
  while read path; do
    # Diff check to see whether staged .po file only has trivial changes to timestamp metadata
    diff -I '^\"\(PO-Revision-Date\)\|\(POT-Creation-Date\)' <(git show :${path}) <(git show HEAD:${path}) >/dev/null 2>&1 && result=$? || result=$?
    if [[ $result -eq 0 ]]; then
      echo "File ${path} only has timestamp changes, unstaging"
      git reset HEAD ${path}
    elif [[ $result -eq 1 ]]; then
      echo "File ${path} has non-trivial changes, so it will remain staged"
    else
      echo "Diff command failed, aborting..."
      return 1
    fi
  done < <(git diff --cached --name-only | grep django.po)
}
