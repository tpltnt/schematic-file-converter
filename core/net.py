#!/usr/bin/env python2
""" The net class """

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


from core.shape import Point


class Net:
    """ a Net with metadata and a list of points (with connections)
    Internal representation of a net, closely matches JSON net """

    def __init__(self, net_id):
        self.net_id = net_id
        self.points = dict()
        self.attributes = dict()
        self.annotations = list()


    def bounds(self):
        """ Return the min and max points of the bounding box """
        x_values = [p.x for p in self.points.values()]
        y_values = [p.y for p in self.points.values()]
        # get a list of all the bounding points for annotations
        bounds = sum([ann.bounds() for ann in self.annotations], [])
        x_values.extend([pt.x for pt in bounds])
        y_values.extend([pt.y for pt in bounds])
        return [Point(min(x_values), min(y_values)),
                Point(max(x_values), max(y_values))]


    def add_annotation(self, annotation):
        """ Add an annotation """
        self.annotations.append(annotation)


    def add_attribute(self, key, value):
        """ Add an attribute """
        self.attributes[key] = value


    def add_point(self, point):
        """ Add a point p to the net """
        self.points[point.point_id] = point

    def conn_point(self, point_a, point_b):
        """ connect point b to point a """
        self.points[point_a.point_id].connected_points.append(point_b.point_id)


    def connected(self, seg):
        """ is segment connected to this net """
        point_a, point_b = seg
        return point_a.point_id in self.points or point_b.point_id in self.points


    def connect(self, seg):
        """ connect segment to this net """
        point_a, point_b = seg
        if point_a.point_id not in self.points:
            self.add_point(point_a)
        self.conn_point(point_a, point_b)
        if point_b.point_id not in self.points:
            self.add_point(point_b)
        self.conn_point(point_b, point_a)

    def json(self):
        """ Return a net as JSON """
        return {
            "net_id":self.net_id,
            "attributes":self.attributes,
            "annotations":[ann.json() for ann in self.annotations],
            "points":[point.json() for point in self.points.values()]
            }


class NetPoint:
    """ A point, basic element in a net """

    def __init__(self, point_id, x, y):
        self.point_id = point_id
        self.x = x
        self.y = y
        self.connected_points = list()
        self.connected_components = list()


    def add_connected_point(self, point_id):
        """ Add a connected point """
        self.connected_points.append(point_id)


    def add_connected_component(self, connected_component):
        """ Add a connected component """
        self.connected_components.append(connected_component)


    def json(self):
        """ Return a netpoint as JSON """
        return {
            "point_id" : self.point_id,
            "x" : self.x,
            "y" : self.y,
            "connected_points" : self.connected_points,
            "connected_components" :
                [comp.json() for comp in self.connected_components]
            }


class ConnectedComponent:
    """ Object representing a component connected to a net """

    def __init__(self, instance_id, pin_number):
        self.instance_id = instance_id
        self.pin_number = pin_number


    def json(self):
        """ Return a connected component as JSON """
        return {
            "instance_id" : self.instance_id,
            "pin_number" : self.pin_number
            }
