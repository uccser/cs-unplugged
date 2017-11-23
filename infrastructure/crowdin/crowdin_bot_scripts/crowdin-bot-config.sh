#!/usr/bin/env bash

# Configuration for crowdin-bot

# CS Unplugged repo
REPO="git@github.com:uccser/cs-unplugged.git"

# Branch for upload of source content to crowdin
TRANSLATION_SOURCE_BRANCH="develop"

# Branch that new translations will be merged into
TRANSLATION_TARGET_BRANCH="develop"

# Branch that new metadata for in context localisation will be merged into
IN_CONTEXT_L10N_TARGET_BRANCH="develop"

# Name of crowdin config file
CROWDIN_CONFIG_FILE="crowdin_content.yaml"

# Code for in-context localisation pseudo language on Crowdin
CROWDIN_PSEUDO_LANGUAGE="en-UD"

# Code for in-context localisation pseudo language on CS Unplugged
CSU_PSEUDO_LANGUAGE="xx_LR"

# GitHub Bot Parameters
GITHUB_BOT_EMAIL="33709036+uccser-bot@users.noreply.github.com"
GITHUB_BOT_NAME="UCCSER Bot"

# Paths under which translated content lives
CONTENT_PATHS=(
    "csunplugged/topics/content"
    "csunplugged/locale"
)
