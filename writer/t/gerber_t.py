#!/usr/bin/python
# encoding: utf-8
#pylint: disable=R0904
""" The gerber writer test class """

# upconvert.py - A universal hardware design file format converter using
# Format:       upverter.com/resources/open-json-format/
# Development:  github.com/upverter/schematic-file-converter
#
# Copyright 2011 Upverter, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from os import path
import unittest

from nose.tools import raises

from core.design import Design
from core.layout import Layout, Layer, Image
from parser.gerber import Gerber as Parser
from writer.gerber import Gerber as Writer
from writer.gerber import MissingLayout, NoLayersFound
from writer.gerber import UnitsNotSpecified, ImageContainsNoData


STRIP_DIRS = path.join('writer', 't')
BASE_DIR = path.dirname(__file__).split(STRIP_DIRS)[0]
TEST_FILES = path.join('test', 'gerber')
DIR = path.join(BASE_DIR, TEST_FILES)


# decorator for tests that use input files

def in_out(infile):
    """ Write gerber file based on design from parser. """
    def wrap_wrap_tm(test_method):
        """ Add params to decorator function. """
        def wrap_tm(self):
            """ Perform meta operations, then method. """
            outfile = 'out-' + infile
            parser = Parser()
            design = parser.parse(path.join(DIR, infile))
            writer = Writer()
            writer.write(design, path.join(DIR, outfile))
            with open(path.join(DIR, outfile), 'r') as f:
                self.output = f.read()
            test_method(self)

        # correctly identify the decorated method
        # (otherwise nose will not run the test)
        wrap_tm.__name__ = test_method.__name__
        wrap_tm.__doc__ = test_method.__doc__
        wrap_tm.__dict__.update(test_method.__dict__)
        wrap_wrap_tm.__name__ = wrap_tm.__name__
        wrap_wrap_tm.__doc__ = wrap_tm.__doc__
        wrap_wrap_tm.__dict__.update(wrap_tm.__dict__)

        return wrap_tm
    return wrap_wrap_tm


class GerberTests(unittest.TestCase):
    """ The tests of the gerber writer """

    def setUp(self):
        """ Setup the test case. """
        self.output = None

    def tearDown(self):
        """ Teardown the test case. """
        pass


    # tests that pass if no errors are raised

    def test_create_new_gerber_writer(self):
        """ Create an empty gerber writer. """
        writer = Writer()
        assert writer != None

    @in_out('simple.ger')
    def test_simple(self):
        """ Generate a simple, correct gerber file. """
        start_second_trace = 'X0Y0*\r\nX60000Y0D02*\r\nX110000Y0D01*'
        assert start_second_trace in self.output

    @in_out('arc_segments.ger')
    def test_arcs(self):
        """ Generate connected arcs and lines - gerber. """
        arc_near_eof = 'G03*\r\nX60000Y-05000I10000J20000*'
        assert arc_near_eof in self.output

    @in_out('fills.ger')
    def test_outline_fills(self):
        """ Generate outline fills - gerber. """
        lines_near_eof = 'G01*\r\nX50000Y05000*\r\nG37*\r\nM02*'
        assert lines_near_eof in self.output

    @in_out('smear.ger')
    def test_smear(self):
        """ Generate a smear - gerber. """
        smear_aperture = '%ADD10R,1.0X1.0*%\r\nD10*'
        assert smear_aperture in self.output

    @in_out('complex.ger')
    def test_complex(self):
        """ Generate aperture macros - gerber. """
        start_subtractive_image = '%LPC*%\r\nG36*\r\nX10000Y25000D02*'
        assert start_subtractive_image in self.output


    # tests that pass if they raise expected errors

    @raises(MissingLayout)
    def test_layout(self):
        """ Capture absence of a layout. """
        design = Design()
        writer = Writer()
        writer.write(design)

    @raises(UnitsNotSpecified)
    def test_units(self):
        """ Capture absence of units. """
        layout = Layout()
        layout.units = None
        layout.layers.append(Layer())
        design = Design()
        design.layout = layout
        writer = Writer()
        writer.write(design)

    @raises(NoLayersFound)
    def test_layers(self):
        """ Capture absence of layers. """
        design = Design()
        design.layout = Layout()
        writer = Writer()
        writer.write(design)

    @raises(ImageContainsNoData)
    def test_images(self):
        """ Capture images with no data. """
        layer = Layer()
        layer.images.append(Image())
        layout = Layout()
        layout.units = 'mm'
        layout.layers.append(layer)
        design = Design()
        design.layout = layout
        writer = Writer()
        writer.write(design)
