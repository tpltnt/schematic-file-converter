#!/usr/bin/python
# encoding: utf-8
""" The eagle writer test class """

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

import unittest

from writer.eagle import Eagle

class EagleTests(unittest.TestCase):
    """ The tests of the eagle writer """

    def setUp(self):
        """ Setup the test case. """
        pass

    def tearDown(self):
        """ Teardown the test case. """
        pass

    def test_create_new_eagle_writer(self):
        """ Test creating an empty writer. """
        writer = Eagle()
        assert writer != None

    def test_header_construct(self):
        """ Test Header block creation """

        _header = Eagle.Header(version="5.11", 
                               numofblocks=12,
                              )

        _chunk = _header.construct()
        
        _valid_chunk = b''.join((b"\x10\x00\x00\x00\x0c\x00\x00\x00", 
                                 b"\x05\x0b\x00\x00\x00\x00\x00\x00",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_settings_construct(self):
        """ Test Settings block creation """
#TODO ...
        pass

    def test_grid_construct(self):
        """ Test Grid block creation """

        _grid = Eagle.Grid(distance=0.1,
                           unitdist="mm",
                           unit="mm",
                           style="dots",
                           multiple=15,
                           display=False,
                           altdistance=0.01,
                           altunitdist="mil",
                           altunit="mil",
                          )

        _chunk = _grid.construct()

        _valid_chunk = b''.join((b"\x12\x00\x02\xa5\x0f\x00\x00\x00",
                                 b"\x9a\x99\x99\x99\x99\x99\xb9\x3f",
                                 b"\x7b\x14\xae\x47\x1e\x7a\x84\x3f"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_layer_construct(self):
        """ Test Layer block creation """

        _layer = Eagle.Layer(number=91,
                             name="Nets",
                             color=2,
                             fill=1,
                             visible=True,
                             active=True,
                             linkedsign=False,
                             linkednumber=91,
                            )

        _chunk = _layer.construct()

        _valid_chunk = b''.join((b"\x13\x00\x0e\x5b\x5b\x01\x02\x00",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x4e",
                                 b"\x65\x74\x73\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_attributeheader_construct(self):
        """ Test AttributeHeader block creation """

# probably no embedded schematic is possible;
        _attrheader = Eagle.AttributeHeader(schematic=''.join((
                                                ":%F%N/%S.%C%R", 
                                                '\t', "/%S.%C%R")),
                                            numofshapes=3,
                                            numofattributes=2, 
                                           )

        _chunk = _attrheader.construct()

        _valid_chunk = b''.join((b"\x14\x00\x00\x00\x00\x00\x00\x00",
                                 b"\x04\x00\x00\x00\x02\x00\x00\x00",
                                 b"\x00\x00\x00\x7f\x00\x00\x00\x09"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_library_construct(self):
        """ Test Library block creation """

# embedded text
        _library = Eagle.Library(name="diode",
                                 numofdevsetblocks=9,
                                 numofsymbolblocks=22,
                                 numofpackageblocks=36,
                                )

        _chunk = _library.construct()

        _valid_chunk = b''.join((b"\x15\x00\x00\x00\x09\x00\x00\x00",
                                 b"\x16\x00\x00\x00\x24\x00\x00\x00",
                                 b"\x64\x69\x6f\x64\x65\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)

# TODO external text
        return

    def test_devicesetheader_construct(self):
        """ Test DeviceSetHeader block creation """

# embedded text
        _deviceset = Eagle.DeviceSetHeader(name="diode",
                                           numofblocks=8,
                                           numofshapesets=2,
                                          )

        _chunk = _deviceset.construct()

        _valid_chunk = b''.join((b"\x17\x00\x00\x00\x08\x00\x00\x00",
                                 b"\x02\x00\x00\x00\x00\x00\x00\x00",
                                 b"\x64\x69\x6f\x64\x65\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)

# TODO external text
        return

    def test_symbolheader_construct(self):
        """ Test SymbolHeader block creation """

# embedded text
        _symbolheader = Eagle.SymbolHeader(name="diode",
                                           numofblocks=21,
                                           numofshapesets=2,
                                          )

        _chunk = _symbolheader.construct()

        _valid_chunk = b''.join((b"\x18\x00\x00\x00\x15\x00\x00\x00",
                                 b"\x02\x00\x00\x00\x00\x00\x00\x00",
                                 b"\x64\x69\x6f\x64\x65\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)

# TODO external text
        return

    def test_packageheader_construct(self):
        """ Test PackageHeader block creation """

# embedded text
        _packageheader = Eagle.PackageHeader(name="diode",
                                             numofblocks=35,
                                             numofshapesets=2,
                                            )

        _chunk = _packageheader.construct()

        _valid_chunk = b''.join((b"\x19\x00\x00\x00\x23\x00\x00\x00",
                                 b"\x02\x00\x00\x00\x00\x00\x00\x00",
                                 b"\x64\x69\x6f\x64\x65\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)

# TODO external text
        return

    def test_symbol_construct(self):
        """ Test Symbol block creation """

# embedded text
        _symbol = Eagle.Symbol(libid=1,
                               name="ZD", 
                               numofshapes=10,
                              )

        _chunk = _symbol.construct()

        _valid_chunk = b''.join((b"\x1d\x00\x0a\x00\x00\x00\x00\x00",
                                 b"\x00\x01\x00\x00\x00\x00\x00\x00",
                                 b"\x5a\x44\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)

# TODO external text
        return

    def test_package_construct(self):
        """ Test Package block creation """

# TODO embedded text

# external text
        _package = Eagle.Package(name="LongName", 
                                 desc="LongDescription",
                                 numofshapes=13,
                                )

        _chunk = _package.construct()

        _valid_chunk = b''.join((b"\x1e\x00\x0d\x00\x00\x00\x00\x00",
                                 b"\x00\x00\x00\x00\x00\x7f\x00\x00",
                                 b"\x00\x09\x7f\x00\x00\x00\x09\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)

        return

    def test_net_construct(self):
        """ Test Net block creation """

        _net = Eagle.Net(name="N$1",
                         nclass=1,
                         numofshapes=5,
                        )

        _chunk = _net.construct()

        _valid_chunk = b''.join((b"\x1f\x00\x05\x00\xff\x7f\xff\x7f",
                                 b"\x00\x80\x00\x80\x00\x01\x00\x00",
                                 b"\x4e\x24\x31\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_part_construct(self):
        """ Test Part block creation """

        _part = Eagle.Part(name="IC9",
                           libid=1,
                           devsetndx=2,
                           symvar=1,
                           techno=1,
                           value="DS3668",
                           numofshapes=2,
                          )

        _chunk = _part.construct()

        _valid_chunk = b''.join((b"\x38\x00\x02\x00\x01\x00\x02\x00",
                                 b"\x01\x01\x01\x49\x43\x39\x00\x00",
                                 b"\x44\x53\x33\x36\x36\x38\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_deviceset_construct(self):
        """ Test DeviceSet block creation """

# embedded names (2 of 3)
        _devset = Eagle.DeviceSet(name="1N5333",
                                  prefix="D",
                                  description="some long long long description",
                                  uservalue=False,
                                  numofshapes=1,
                                  numofconnblocks=2,
                                 )

        _chunk = _devset.construct()

        _valid_chunk = b''.join((b"\x37\x00\x01\x00\x02\x00\x00\x00",
                                 b"\x44\x00\x00\x00\x00\x7f\x00\x00",
                                 b"\x00\x09\x31\x4e\x35\x33\x33\x33"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
# embedded names (2 of 3)
        _devset = Eagle.DeviceSet(name="some long long long name",
                                  prefix="JP",
                                  description="",
                                  uservalue=True,
                                  numofshapes=1,
                                  numofconnblocks=2,
                                 )

        _chunk = _devset.construct()

        _valid_chunk = b''.join((b"\x37\x00\x01\x00\x02\x00\x01\x00",
                                 b"\x4A\x50\x00\x00\x00\x00\x00\x00",
                                 b"\x00\x00\x7f\x00\x00\x00\x09\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)

        return

    def test_bus_construct(self):
        """ Test Bus block creation """

        _bus = Eagle.Bus(name="B$3",
                         numofshapes=4,
                        )

        _chunk = _bus.construct()

        _valid_chunk = b''.join((b"\x3a\x00\x04\x00\x42\x24\x33\x00",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_shapeheader_construct(self):
        """ Test ShapeHeader block creation """

        _shapeheader = Eagle.ShapeHeader(numofshapes=3,
                                         numofpartblocks=4,
                                         numofbusblocks=5,
                                         numofnetblocks=14,
                                        )

        _chunk = _shapeheader.construct()

        _valid_chunk = b''.join((b"\x1a\x00\x03\x00\x00\x00\x00\x00",
                                 b"\x00\x00\x00\x00\x04\x00\x00\x00",
                                 b"\x05\x00\x00\x00\x0e\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_segment_construct(self):
        """ Test Segment block creation """

        _segment = Eagle.Segment(numofshapes=4,
                                 cumulativenumofshapes=19,
                                )

        _chunk = _segment.construct()

        _valid_chunk = b''.join((b"\x20\x00\x04\x00\x00\x00\x00\x00",
                                 b"\x00\x13\x00\x00\x00\x00\x00\x00",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_connectionheader_construct(self):
        """ Test ConnectionHeader block creation """

        _connheader = Eagle.ConnectionHeader(numofshapes=1,
                                             sindex=4,
                                             attributes=None,
                                             technologies=None,
                                             name=None,
                                            )

        _chunk = _connheader.construct()

        _valid_chunk = b''.join((b"\x36\x00\x01\x00\x04\x00\x00\x00",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00",
                                 b"\x00\x00\x00\x27\x27\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
# TODO technology / attributes check, 'name'
        return

    def test_connections_construct(self):
        """ Test Connections block creation """

        _connections = Eagle.Connections(connections = [33, 34, 35, 36, 37, 38, 
                                        39, 40, 41, 42, 43, 44, 45, 46, 47, 48]
                                        )

        _chunk = _connections.construct()

        _valid_chunk = b''.join((b"\x3c\x00\x21\x22\x23\x24\x25\x26",
                                 b"\x27\x28\x29\x2a\x2b\x2c\x2d\x2e",
                                 b"\x2f\x30\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_polygon_construct(self):
        """ Test Polygon block creation """

        _polygon = Eagle.Polygon(numofshapes=3,
                                 width=0.1016,
                                 layer=21,
                                )

        _chunk = _polygon.construct()

        _valid_chunk = b''.join((b"\x21\x00\x03\x00\x00\x00\x00\x00",
                                 b"\x00\x00\x00\x00\xfc\x01\x00\x00",
                                 b"\x00\x00\x15\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_instance_construct(self):
        """ Test Instance block creation """

        _instance = Eagle.Instance(numofshapes=2,
                                   x=218.44,
                                   y=60.96,
                                   smashed=True,
                                   rotate="R90",
                                  )

        _chunk = _instance.construct()

        _valid_chunk = b''.join((b"\x30\x00\x02\x00\xd0\x54\x21\x00",
                                 b"\x40\x4d\x09\x00\xff\xff\x00\x00",
                                 b"\x00\x04\x01\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_wire_construct(self):
        """ Test Wire block creation """

        _wire = Eagle.Wire(x1=33.02,
                           y1=60.96,
                           x2=33.02,
                           y2=50.8,
                           width=0.1524,
                           style="DashDot",
                           layer=91,
                          )

        _chunk = _wire.construct()

        _valid_chunk = b''.join((b"\x22\x00\x00\x5b\xd8\x09\x05\x00",
                                 b"\x40\x4d\x09\x00\xd8\x09\x05\x00",
                                 b"\x60\xc0\x07\x00\xfa\x02\x03\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_hole_construct(self):
        """ Test Hole block creation """

        _hole = Eagle.Hole(x=0.,
                           y=11.176,
                           drill=3.302,
                          )

        _chunk = _hole.construct()

        _valid_chunk = b''.join((b"\x28\x00\x00\x00\x00\x00\x00\x00",
                                 b"\x90\xb4\x01\x00\x7e\x40\x00\x00",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_smd_construct(self):
        """ Test SMD block creation """

        _smd = Eagle.SMD(name="14",
                         x=-1.905,
                         y=3.0734,
                         dx=0.6604,
                         dy=2.032,
                         layer=1,
                        )

        _chunk = _smd.construct()

        _valid_chunk = b''.join((b"\x2b\x00\x00\x01\x96\xb5\xff\xff",
                                 b"\x0e\x78\x00\x00\xe6\x0c\xb0\x27",
                                 b"\x00\x00\x00\x31\x34\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_arc_construct(self):
        """ Test Arc block construction """

        _arc = Eagle.Arc(x1=101.6,
                         y1=38.1,
                         x2=111.76,
                         y2=60.96,
                         width=0.6096,
                         curve=0, # <---- wrong
                         cap="flat",
                         direction="counterclockwise",
                         style="ShortDash",
                         layer=91,
                        )

        _chunk = _arc.construct()

        _valid_chunk = b''.join((b"\x22\x00\x00\x5b\xc0\x80\x0f\x00",
                                 b"\x48\xd0\x05\x00\xa0\x0d\x11\x00",
                                 b"\x40\x4d\x09\x00\xe8\x0b\x32\x81"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_circle_construct(self):
        """ Test Circle block creation """

        _circle = Eagle.Circle(x=119.38,
                               y=66.04,
                               radius=9.1581,
                               width=0.3048,
                               layer=91,
                              )

        _chunk = _circle.construct()

        _valid_chunk = b''.join((b"\x25\x00\x00\x5b\x48\x37\x12\x00",
                                 b"\xb0\x13\x0a\x00\xbd\x65\x01\x00",
                                 b"\xbd\x65\x01\x00\xf4\x05\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_rectangle_construct(self):
        """ Test Rectangle block creation """

        _rectangle = Eagle.Rectangle(x1=15.24,
                                     y1=68.58,
                                     x2=58.42,
                                     y2=111.76,
                                     rotate=None,
                                     layer=92,
                                    )

        _chunk = _rectangle.construct()

        _valid_chunk = b''.join((b"\x26\x00\x00\x5c\x50\x53\x02\x00",
                                 b"\xe8\x76\x0a\x00\x08\xea\x08\x00",
                                 b"\xa0\x0d\x11\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_pad_construct(self):
        """ Test Pad block creation """

        _pad = Eagle.Pad(name="A",
                         x=5.08,
                         y=0.,
                         drill=0.5588,
                        )

        _chunk = _pad.construct()

        _valid_chunk = b''.join((b"\x2a\x00\x00\x00\x70\xc6\x00\x00",
                                 b"\x00\x00\x00\x00\xd4\x15\x00\x00",
                                 b"\x00\x00\x00\x41\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_pin_construct(self):
        """ Test Pin block creation """

        _pin = Eagle.Pin(name="C",
                         x=2.54,
                         y=0.,
                         visible="off",
                         direction="pas",
                         rotate="R180",
                         length="short",
                         function=None,
                         swaplevel=0,
                        )

        _chunk = _pin.construct()

        _valid_chunk = b''.join((b"\x2c\x00\x00\x00\x38\x63\x00\x00",
                                 b"\x00\x00\x00\x00\x96\x00\x43\x00",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)

        _pin = Eagle.Pin(name="IN+",
                         x=-5.08,
                         y=2.54,
                         visible="pad",
                         direction="in",
                         rotate=None,
                         length="short",
                         function="dot",
                         swaplevel=1,
                        )

        _chunk = _pin.construct()

        _valid_chunk = b''.join((b"\x2c\x00\x41\x00\x90\x39\xff\xff",
                                 b"\x38\x63\x00\x00\x11\x01\x49\x4e",
                                 b"\x2b\x00\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_gate_construct(self):
        """ Test Gate block creation """

        _gate = Eagle.Gate(name="P",
                           x=-25.4,
                           y=2.54,
                           sindex=2,
                           addlevel="request",
                          )

        _chunk = _gate.construct()

        _valid_chunk = b''.join((b"\x2d\x00\x00\x00\xd0\x1f\xfc\xff",
                                 b"\x38\x63\x00\x00\x03\x00\x02\x00",
                                 b"\x50\x00\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_text_construct(self):
        """ Test Text block creation """

# embedded text
        _text = Eagle.Text(value="text!",
                           x=121.92,
                           y=20.32,
                           size=6.4516,
                           rotate="R180",
                           font="fixed",
                           ratio=19,
                           layer=91,
                          )

        _chunk = _text.construct()

        _valid_chunk = b''.join((b"\x31\x00\x02\x5b\x80\x9a\x12\x00",
                                 b"\xc0\x19\x03\x00\x02\x7e\x4c\x00",
                                 b"\x00\x08\x74\x65\x78\x74\x21\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)

# external text
        _text = Eagle.Text(value="longlonglonglongtext",
                           x=12.7,
                           y=93.98,
                           size=6.4516,
                           rotate=None,
                           font="fixed",
                           ratio=19,
                           layer=91,
                          )

        _chunk = _text.construct()

        _valid_chunk = b''.join((b"\x31\x00\x02\x5b\x18\xf0\x01\x00",
                                 b"\x18\x57\x0e\x00\x02\x7e\x4c\x00",
                                 b"\x00\x00\x7f\x00\x00\x00\x09\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return
 
    def test_label_construct(self):
        """ Test Label block creation """

        _label = Eagle.Label(x=91.44,
                             y=30.48,
                             size=0.8128,
                             rotate="R270",
                             font="fixed",
                             ratio=3,
                             onoff=True,
                             mirrored=True,
                             layer=95,
                            )

        _chunk = _label.construct()

        _valid_chunk = b''.join((b"\x33\x00\x02\x5f\xe0\xf3\x0d\x00",
                                 b"\xa0\xa6\x04\x00\xe0\x0f\x0c\x00",
                                 b"\x00\x1c\x01\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return
 
    def test_attributenam_construct(self):
        """ Test AttributeNam block creation """

        _attrnam = Eagle.AttributeNam(x=221.615,
                                      y=64.77,
                                      size=1.524,
                                      layer=95,
                                     )

        _chunk = _attrnam.construct()

        _valid_chunk = b''.join((b"\x34\x00\x00\x5f\xd6\xd0\x21\x00",
                                 b"\x14\xe2\x09\x00\xc4\x1d\x00\x00",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return
 
    def test_attributeval_construct(self):
        """ Test AttributeVal block creation """

        _attrval = Eagle.AttributeVal(x=220.345,
                                      y=62.611,
                                      size=1.524,
                                      layer=96,
                                     )

        _chunk = _attrval.construct()

        _valid_chunk = b''.join((b"\x35\x00\x00\x60\x3a\x9f\x21\x00",
                                 b"\xbe\x8d\x09\x00\xc4\x1d\x00\x00",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_pinref_construct(self):
        """ Test PinRef block creation """

        _pinref = Eagle.PinRef(partno=6,
                               gateno=1,
                               pinno=7,
                              )

        _chunk = _pinref.construct()

        _valid_chunk = b''.join((b"\x3d\x00\x00\x00\x06\x00\x01\x00",
                                 b"\x07\x00\x00\x00\x00\x00\x00\x00",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return

    def test_attribute_construct(self):
        """ Test Attribute block creation """

# embedded attribute
        _attr = Eagle.Attribute(name="1234567890",
                                value="qw!rt",
                               )

        _chunk = _attr.construct()

        _valid_chunk = b''.join((b"\x42\x00\x2a\x00\x00\x00\x00\x31",
                                 b"\x32\x33\x34\x35\x36\x37\x38\x39",
                                 b"\x30\x21\x71\x77\x21\x72\x74\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)

# external attribute
        _attr = Eagle.Attribute(name="1234567890",
                                value="longerthanexpected",
                               )

        _chunk = _attr.construct()

        _valid_chunk = b''.join((b"\x42\x00\x2a\x00\x00\x00\x00\x7f",
                                 b"\x00\x00\x00\x09\x00\x00\x00\x00",
                                 b"\x00\x00\x00\x00\x00\x00\x00\x00"))

        self.assertNotEqual(_chunk, None)
        self.assertEqual(_chunk, _valid_chunk)
        return


