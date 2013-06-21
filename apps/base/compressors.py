# coding=utf-8

from pipeline.compressors import CompressorBase


class CSSMinCompressor(CompressorBase):
    def compress_css(self, css):
        from cssmin import cssmin
        return cssmin(css)
