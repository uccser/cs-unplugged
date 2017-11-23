"""Script to modify pseudo translation markdown files to make parseable by Verto.

Crowdin in-context translation works by replacing all strings in the file with
placeholder identifiers. On the front end, these are then substituted with the
translated versions of the strings. However this means that verto tags are not
available at time of deployment (as they are treated as normal source strings).

The current workaround is this script, which identifies all source strings which
are verto block tags, and inserts them back into the markdown file. It also
retains the identifier, to allow for editing of the verto tag on the front end,
although the effects of these changes will not be seen in real time.
"""

from verto import Verto
import re
import os
from lxml import etree

CONTENT_ROOT = "csunplugged/topics/content"
EN_DIR = os.path.join(CONTENT_ROOT, 'en')
PSEUDO_LANGUAGE = "xx_LR"
PSEUDO_DIR = os.path.join(CONTENT_ROOT, PSEUDO_LANGUAGE)
XLIFF_DIR = os.path.join(CONTENT_ROOT, 'xliff')

NS_DICT = {
    'ns': "urn:oasis:names:tc:xliff:document:1.2"
}

XLIFF_PARSER = etree.XMLParser()

def get_xliff_trans(path):
    """Get xml 'body' element for first file node in the xliff file.

    Note that this should be the only file node in the file, as one xliff
    file is downloaded per source file

    Args:
        path (str) path to xliff file
    Returns:
        etree.Element for 'body' element
    """
    with open(xliff_path, 'r') as f:
        xliff = etree.parse(f, XLIFF_PARSER)
        xliff_trans = xliff.xpath(
            './/ns:file/ns:body',
            namespaces=NS_DICT
        )[0]
        return xliff_trans


def get_verto_block_patterns():
    """Get list of compiled regex patterns for verto block tags."""
    convertor = Verto()
    ext = convertor.verto_extension
    block_pattern = ext.processor_info['style']['block_pattern']
    block_strings = ext.processor_info['style']['strings']['block']
    patterns = []
    for block_string in block_strings:
        c = re.compile(block_pattern.format(**{'block': block_string}))
        patterns.append(c)
    return patterns

def is_block(string, patterns):
    """Determine whether the given source string is a verto block tag.

    Args:
        string: (str) source string
        patterns: (list) compiled regex patterns for verto block tags
    Returns:
        bool
    """
    for pattern in patterns:
        if pattern.search(string):
            return True
    return False

def update_markdown_file(md_path, blocks, no_translate):
    """Update given markdown file by replacing certain string identifiers with their source string.

    Args:
        md_path: (str) path to markdown file
        blocks: (dict) {crowdin_string_id: original_verto_tag, ...} mapping of
            all string identifiers to replace with original verto tag
        no_translate: (dict) {crowdin_string_id: source_string, ...} mapping of
            all string identifiers to replace with source string, for strings
            that crowdin has identified should not be translated.
    """
    with open(md_path, 'r') as f:
        md = f.read()

    for block_id, block_content in blocks.items():
        pattern = r'([ \t]*)crwdns{0}:0(.*?)crwdne{0}:0'.format(block_id)
        c = re.compile(pattern)
        new_str = "\\1*BlockTag: crwdns{id}:0crwdne{id}:0*\n\n\\1{content}".format(id=block_id, content=block_content)
        md = re.sub(c, new_str, md)
        print("{} - {}".format(block_id, new_str))

    for string_id, string in no_translate.items():
        pattern = r'crwdns{0}:0(.*?)crwdne{0}:0'.format(string_id)
        c = re.compile(pattern)
        md = re.sub(c, string, md)
        print("{} - {}".format(string_id, string))

    with open(md_path, 'w') as f:
        f.write(md)
    print("Finished updating {}".format(md_path))


if __name__ == "__main__":
    for root, dirs, files in os.walk(EN_DIR):
        for name in files:
            if name.endswith(".md"):
                source_md_path = os.path.join(root, name)
                path_from_language_root = os.path.relpath(source_md_path, start=EN_DIR)
                target_md_path = os.path.join(PSEUDO_DIR, path_from_language_root)
                xliff_path = os.path.join(XLIFF_DIR, path_from_language_root)
                xliff_path = os.path.splitext(xliff_path)[0] + ".xliff"
                xliff_trans = get_xliff_trans(xliff_path)

                blocks = {}
                block_patterns = get_verto_block_patterns()

                no_translate = {}

                for string in xliff_trans:
                    id = string.attrib["id"]
                    untranslated = string.find('ns:source', namespaces=NS_DICT).text
                    if untranslated is not None:
                        if string.attrib.get("translate") == "no":
                            no_translate[id] = untranslated
                        elif is_block(untranslated, block_patterns):
                            blocks[id] = untranslated
                update_markdown_file(target_md_path, blocks, no_translate)
