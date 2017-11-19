#!/usr/bin/env bash

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
