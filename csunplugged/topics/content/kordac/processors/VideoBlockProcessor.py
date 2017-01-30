from markdown.blockprocessors import BlockProcessor
from processors.utils import parse_argument, centre_html
from markdown.util import etree
import re

YOUTUBE_SRC = 'http://www.youtube.com/embed/{0}?rel=0'
VIMEO_SRC = 'http://player.vimeo.com/video/{0}'

class VideoBlockProcessor(BlockProcessor):
    pattern = re.compile('^\{video (?P<args>[^\}]*)\}')

    def __init__(self, ext, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.VIDEO_TEMPLATE = ext.html_templates['video']
        self.pattern = re.compile(ext.tag_patterns['video']['pattern'])

    def test(self, parent, block):
        return self.pattern.match(block) is not None

    def run(self, parent, blocks):
        block = blocks.pop(0)
        match = self.pattern.match(block) # NTS why not search?
        # NTS should panel use this method to get attributes too?
        arguments = match.group('args') # NTS what other arguments will there be?
        url = parse_argument('url', arguments)
        (video_type, video_identifier) = self.extract_video_identifier(url, match)

        if url:
            if video_type:
                if video_type == 'youtube':
                    source_link = YOUTUBE_SRC.format(video_identifier)
                elif video_type == 'vimeo':
                    source_link = VIMEO_SRC.format(video_identifier)
                node = etree.fromstring(self.VIDEO_TEMPLATE.format(source=source_link))
                # add video to dom, centres using 10 columns
                parent.append(centre_html(node, 10))


    def extract_video_identifier(self, video_url, match):
        '''Returns the indentifier from a given URL'''
        if 'youtu.be' in video_url or 'youtube.com/embed' in video_url:
            video_query = video_url.split('/')[-1]
            return ('youtube', video_query)
        elif 'youtube.com' in video_url:
            start_pos = video_url.find('v=') + 2
            end_pos = video_url.find('&');
            if end_pos == -1:
                video_query = video_url[start_pos:]
                return('youtube', video_query)
            else:
                video_query = video_url[start_pos:end_pos]
                identifier = ('youtube', video_query)
        elif 'vimeo' in video_url:
            video_query = video_url.split('/')[-1]
            return ('vimeo', video_query)
        else:
            return (None, '')

