"""Script to get json mapping from crowdin language codes to CSU language codes."""

import argparse
import json
from crowdin_bot import api
import yaml
import re


def get_osx_locale_mapping():
    """Get dictionary mapping crowdin language codes to osx_locale_codes.

    See https://support.crowdin.com/api/supported-languages/
    """
    languages_json = api.api_call_json("supported-languages")
    return {
        language["crowdin_code"]: language["osx_locale"] for language in languages_json
    }


def validate_config(config):
    """Validate that this script can be used with the current crowdin config file.

    Requirements:
        - must contain at least one entry under the 'files' key
        - File patterns must contain %osx_locale% and %original_file_name%
          placeholders, and no others.
        - If a language_mapping is used to override certain osx_locale codes,
          this mapping must be the same for all files configurations.
    Args:
        config: Dictionary of config yaml file
    """
    files = config.get("files", [])
    if len(files) == 0:
        raise Exception("Crowdin config must contain at least one file config")
    osx_locale_map_overriide = get_overrides(config)
    translation_regex=re.compile(r"[^%]*%osx_locale%[^%]*%original_file_name%")
    for file in files:
        translation_pattern=file.get("translation", "")
        if not translation_regex.match(translation_pattern):
            raise Exception("Translation patterns in the crowdin config file must "
                            "contain %osx_locale% and %original_file_name% placeholders (and no others). "
                            "The following pattern does not meet this criteria: {}".format(translation_pattern))
        if osx_locale_map_overriide:
            if file.get("languages_mapping", {}).get("osx_locale") != osx_locale_map_overriide:
                raise Exception("All files entries in the crowdin config file must have the same osx_locale language mapping.")


def get_overrides(config):
    """Get the language mapping dictionary for the %osx_locale% code from config file."""
    # This is guaranteed to be the same for all files, so just use the first one.
    return config["files"][0].get("languages_mapping").get("osx_locale", {})

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--crowdin-config', required=True,
                        help='Path to crowdin config yaml file')
    args = parser.parse_args()
    with open(args.crowdin_config) as f:
        config = yaml.load(f)
    validate_config(config)
    osx_locale_mapping = get_osx_locale_mapping()
    overrides = get_overrides(config)
    osx_locale_mapping.update(overrides)
    print(json.dumps(osx_locale_mapping, sort_keys=True, indent=4))
