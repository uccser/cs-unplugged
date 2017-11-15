from verto import Verto
import re
import os
from lxml import etree

CONTENT_ROOT = "csunplugged/topics/content"
EN_DIR = os.path.join(CONTENT_ROOT, 'en')
PSEUDO_LANGUAGE = "xx-lr"
PSEUDO_DIR = os.path.join(CONTENT_ROOT, PSEUDO_LANGUAGE)
XLIFF_DIR = os.path.join(CONTENT_ROOT, 'xliff')

NS_DICT = {
    'ns': "urn:oasis:names:tc:xliff:document:1.2"
}

XLIFF_PARSER = etree.XMLParser()

def get_xliff_trans(path):
    with open(xliff_path, 'r') as f:
        xliff = etree.parse(f, XLIFF_PARSER)
        xliff_trans = xliff.xpath(
            './/ns:file/ns:body',
            namespaces=NS_DICT
        )[0]
        return xliff_trans


def get_verto_block_patterns():
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
    for pattern in patterns:
        if pattern.search(string):
            return True
    return False

def update_markdown_file(md_path, blocks, no_translate):
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
        # new_str = "crwdns{id}:0crwdne{id}:0*\n\n\\1{content}".format(id=url_id, content=url)
        md = re.sub(c, string, md)
        print("{} - {}".format(string_id, string))

    with open(md_path, 'w') as f:
        f.write(md)
    print("Finished updating {}".format(md_path))


if __name__ == "__main__":

    # for root, files in (("csunplugged/topics/content/en/", ("unplugged-programming/programming-challenges/draw-different-types-of-triangles/extra-challenge.md",)),):
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
