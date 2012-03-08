# gEDA/gaf File Format Document #

by: Ales V. Hvezda, ahvezda@geda.seul.org
This document is released under [GFDL](http://www.gnu.org/copyleft/fdl.html)
December 31st, 2003

slight changes for readability by tpltnt, November 2011

Updated with some details that came up during implementation of the upconverter
parser for gEDA by elbaschid, December 2011

## Overview ##

This file is the official documentation for the file formats in gEDA/gaf
(gschem And Friends). The primary file format used in gEDA/gaf is the
schematic/symbol format. Files which end with .sch or .sym are schematics
or symbol files. Until there is another file type in gEDA/gaf, then this
document will only cover the symbol/schematic file format.
This file format document is current as of gEDA/gaf version 20040111.
This document covers file format version 1 and 2.
Note, this file format and any other file formats associated with gEDA
are placed under the General Public License (GPL) version 2.0. The
gEDA/gaf symbol and schematic file format is Copyright (C) 1998-2004
Ales Hvezda.

## Coordinate Space ##

All coordinates are in mils (1/1000 of an inch). This is an arbitrary decision. 
Remember in there is no concept of physical lengths/dimensions in schematics and 
symbols (for schematic capture only).

 * Origin is in lower left hand corner. 
 * The size of the coordinate space is unlimited, but it is recommended that all objects stay within (120.0, 90.0) (x, y inches).
 * It is generally advisable to have positive x and y coordinates, however, negative coordinates work too, but not recommended.
 * A grid segment is of 100 x 100 mils size.
 * The blueprint frame of a schematic is usually not in the origin but translated to (40000, 4000) in mils.

The following figure shows how the coordinate space is setup: 
TODO: insert image

X axis increases going to the right. Y axis increase going up. Coordinate system is landscape and corresponds to a sheet of paper turned on its side.

## Filenames ##

Symbols end in .sym. The only symbol filename convention that is used in gEDA/gaf is that if there are multiple instances of a symbol with the same name (like a 7400), then a -1, -2, -3, … -N suffix is added to the end of the filename. Example: 7400-1.sym, 7400-2.sym, 7400-3.sym…
Schematics end in .sch. There used to be a schematic filename convention (adding a -1 .. -N to the end of the basename), but this convention is now obsolete. Schematic filenames can be anything that makes sense to the creator.

## Object types ##

A schematic/symbol file for gEDA/gaf consists of:

 * A version (v) as the first item in the file. This is required.
 * Any number of objects and the correct data. Objects are specified by an “object type”
 * Most objects are a single line, however text objects are two lines long.
 * No blank lines at the end of the file (these are ignored by the tools)
 * For all enumerated types in the gEDA/gaf file formats, the field takes on the numeric value.

The “object type” id is a single letter and this id must start in the
first column. The object type id is case sensitive. The schematic and
symbol files share the same file layout. A symbol is nothing more than
a collection of primitive objects (lines, boxes, circles, arcs, text,
and pins). A schematic is a collection of symbols (components), nets,
and buses.
The following sections describe the specifics of each recognized object
type. Each section has the name of the object, which file type (sch/sym)
the object can appear in, the format of the data, a description of each
individual field, details and caveats of the fields, and finally an
example with description.
For information on the color index (which is used in practically all
objects), see the Color section.

### version ###

Valid in: Schematic and Symbol files

Format: <pre>type version fileformat_version</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>v</td>
	</tr>
	<tr>
		<td>1</td>
		<td>version</td>
		<td>int</td>
		<td>version of gEDA/gaf that wrote this file</td>
	</tr>
	<tr>
		<td>2</td>
		<td>fileformat_version</td>
		<td>int</td>
		<td>gEDA/gaf file format version number</td>
	</tr>
</table>

 * The type is a lower case “v” (as in Victor).
 * This object must be in every file used or created by the gEDA/gaf tools.
 * The format of the first version field is YYYYMMDD.
 * The version number is not an arbitrary timestamp. Do not make up a version number and expect the tools to behave properly.
 * The “version of gEDA/gaf that wrote this file” was used in all versions of gEDA/gaf up to 20030921 as the file formats version. This field should no longer be used to determine the file format. It is used for information purposes only now.
 * Starting at and after gEDA/gaf version 20031004, the fileformat version field is used to determine the file format version. All file format code should key off of this field.
 * fileformat version increases when the file format changes.
 * The starting point for fileformat version was 1. The current fileformat is 2.
 * fileformat version is just an integer with no minor number.
 * Development versions include: 19990601, 19990610, 19990705, 19990829, 19990919, 19991011, 20000220, 20000704, 20001006, 20001217, 20010304, 20010708, 20010722, 20020209, 20020414, 20020527, 20020825, 20021103, 20030223, 20030525, 20030901, 20040111, 20040710, 20041228, 20050313, 20050820, 20060123, 20060824, 20060906, 20061020, 20070216, 20070705, 20070708, 20070818, 20071229, 20080110, 20080127, 20080706, 20081220, 20081221, 20090328, 20090829, 20090830, 20110116, 20110619
 * Stable versions include: 20070526, 20070626, 20070902, 20071231, 20080127, 20080929, 20081220, 20081231, 20091004, 20100214, 20110115
 * CVS or test versions (should not be used): 20030921, 20031004, 20031019, 20031231, 20050814
 * Keep in mind that each of the above listed versions might have had file format variations. This document only covers the last version's file format.

Example:
<pre>v 20040111 1</pre>

### line ###

Valid in: Schematic and Symbol files

Format: <pre>type x1 y1 x2 y2 color width capstyle dashstyle dashlength dashspace</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>L</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x1</td>
		<td>int/mils</td>
		<td>First X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y1</td>
		<td>int/mils</td>
		<td>First Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>x2</td>
		<td>int/mils</td>
		<td>Second X coordinate</td>
	</tr>
	<tr>
		<td>4</td>
		<td>y2</td>
		<td>int/mils</td>
		<td>Second Y coordinate</td>
	</tr>
	<tr>
		<td>5</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>
	<tr>
		<td>6</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of line</td>
	</tr>
	<tr>
		<td>7</td>
		<td>capstyle</td>
		<td>int</td>
		<td>Line cap style</td>
	</tr>
	<tr>
		<td>8</td>
		<td>dashstyle</td>
		<td>int</td>
		<td>Type of dash style</td>
	</tr>
	<tr>
		<td>9</td>
		<td>dashlength</td>
		<td>int/mils</td>
		<td>Length of dash</td>
	</tr>
	<tr>
		<td>10</td>
		<td>dashspace</td>
		<td>int/mils</td>
		<td>Space inbetween dashes</td>
	</tr>
</table>

 * The capstyle is an enumerated type:
  * END NONE = 0
  * END SQUARE = 1
  * END ROUND = 2
 * The dashstyle is an enumerated type:
  * TYPE SOLID = 0
  * TYPE DOTTED = 1
  * TYPE DASHED = 2
  * TYPE CENTER = 3
  * TYPE PHANTOM = 4
 * The dashlength parameter is not used for TYPE SOLID and TYPE DOTTED. This parameter should take on a value of -1 in these cases.
 * The dashspace parameter is not used for TYPE SOLID. This parameter should take on a value of -1 in these case.

Example: <pre>L 23000 69000 28000 69000 3 40 0 1 -1 75</pre>

A line segment from (23000, 69000) to (28000, 69000) with color index 3, 40 mils thick, no cap, dotted line style, and with a spacing of 75 mils in between each dot.


### picture ###

Valid in: Schematic and Symbol files

Format:<pre>type x1 y1 width height angle mirrored embedded
filename
[encoded picture data
encoded picture end]
</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>G</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x</td>
		<td>int/mils</td>
		<td>Lower left X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y</td>
		<td>int/mils</td>
		<td>Lower left Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of the picture</td>
	</tr>
	<tr>
		<td>4</td>
		<td>height</td>
		<td>int/mils</td>
		<td>Height of the picture</td>
	</tr>
	<tr>
		<td>5</td>
		<td>angle</td>
		<td>int/degrees</td>
		<td>Angle of the picture</td>
	</tr>
	<tr>
		<td>6</td>
		<td>mirrored</td>
		<td>char</td>
		<td>Mirrored or normal picture</td>
	</tr>
	<tr>
		<td>7</td>
		<td>embedded</td>
		<td>char</td>
		<td>Embedded or link to the picture file</td>
	</tr>
	<tr>
		<td>8</td>
		<td>filename</td>
		<td>string</td>
		<td>path and filename of a not embedded picture</td>
	</tr>
	<tr>
		<td>9</td>
		<td>encoded picture data</td>
		<td>string</td>
		<td>Serialized picture encoded using base64</td>
	</tr>
	<tr>
		<td>10</td>
		<td>encoded picture end</td>
		<td>string</td>
		<td>A line containing only a dot character</td>
	</tr>
	</tr>
</table>

 * This object is a picture object. The first line contains all the picture parameters, and the second line is the path and filename of the picture. The filename is not used if the picture is embedded.
 * The angle of the picture can only take on one of the following values: 0, 90, 180, 270.
 * The mirrored field is an enumerated type:
  * NOT MIRRORED = 0
  * MIRRORED = 1
 * The embedded field is an enumerated type:
  * NOT EMBEDDED = 0
  * EMBEDDED = 1 (not yet supported)
 * The encoded picture and encoded picture end fields are only in the file if the picture is embedded in the schematic:
  * encoded picture data: This is a multiple line field. The picture is serialized and then encoded using base64. This way the encoded data uses only printable characters. This field is the result of these two operations.
  * encoded picture end : A line containing only a single dot '.' character marks the end of the encoded picture data.

Example:
<pre>
G 16900 35800 1400 2175 0 0 0
../bitmaps/logo.jpg
</pre>

A picture object with the lower left corner at (16900, 35800). The width of the image is 1400 mils, and its height is 2175 mils. The picture rotation is 0 degrees and the picture is not mirrored, neither embedded.
The picture path and filename is showed in the second line.

Example:
<pre>
G 16900 35800 1400 2175 0 0 1
../bitmaps/logo.jpg
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB
.
</pre>

A picture object with the lower left corner at (16900, 35800). The width of the image is 1400 mils, and its height is 2175 mils.
The picture rotation is 0 degrees, it is not mirrored, and it is embedded.
The picture path and filename is showed in the second line. Since this is an embedded picture, the filename and path are not used.
The encoded picture data is only an example (it is not real data). The last line containing a single dot '.' character marks the end of the encoded picture data. 

### box ###

Valid in: Schematic and Symbol files

Format: <pre>type x y width height color width capstyle dashstyle dashlength dashspace filltype fillwidth angle1 pitch1 angle2 pitch2</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>B</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x</td>
		<td>int/mils</td>
		<td>Lower left hand X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y</td>
		<td>int/mils</td>
		<td>Lower left hand Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of the box (x direction)</td>
	</tr>
	<tr>
		<td>4</td>
		<td>height</td>
		<td>int/mils</td>
		<td>Height of the box (y direction)</td>
	</tr>
	<tr>
		<td>5</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>
	<tr>
		<td>6</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of lines</td>
	</tr>
	<tr>
		<td>7</td>
		<td>capstyle</td>
		<td>int/mils</td>
		<td>Line cap style</td>
	</tr>
	<tr>
		<td>8</td>
		<td>dashstyle</td>
		<td>int</td>
		<td>Type of dash style</td>
	</tr>
	<tr>
		<td>9</td>
		<td>dashlength</td>
		<td>int/mils</td>
		<td>Length of dash</td>
	</tr>
	<tr>
		<td>10</td>
		<td>dashspace</td>
		<td>int/mils</td>
		<td>Space inbetween dashes</td>
	</tr>
	<tr>
		<td>11</td>
		<td>filltype</td>
		<td>int</td>
		<td>Type of fill</td>
	</tr>
	<tr>
		<td>12</td>
		<td>fillwidth</td>
		<td>int/mils</td>
		<td>Width of the fill lines</td>
	</tr>
	<tr>
		<td>13</td>
		<td>angle1</td>
		<td>int/degrees</td>
		<td>First angle of fill</td>
	</tr>
	<tr>
		<td>14</td>
		<td>pitch1</td>
		<td>int/mils</td>
		<td>First pitch/spacing of fill</td>
	</tr>
	<tr>
		<td>15</td>
		<td>angle2</td>
		<td>int/degrees</td>
		<td>Second angle of fill</td>
	</tr>
	<tr>
		<td>16</td>
		<td>pitch2</td>
		<td>int/mils</td>
		<td>Second pitch/spacing of fill</td>
	</tr>
</table>

 * The capstyle is an enumerated type:
  * END NONE = 0
  * END SQUARE = 1
  * END ROUND = 2
 * The dashstyle is an enumerated type:
  * TYPE SOLID = 0
  * TYPE DOTTED = 1
  * TYPE DASHED = 2
  * TYPE CENTER = 3
  * TYPE PHANTOM = 4
 * The dashlength parameter is not used for TYPE SOLID and TYPE DOTTED. This parameter should take on a value of -1 in these cases.
 * The dashspace parameter is not used for TYPE SOLID. This parameter should take on a value of -1 in these case.
 * The filltype parameter is an enumerated type:
  * FILLING HOLLOW = 0
  * FILLING FILL = 1
  * FILLING MESH = 2
  * FILLING HATCH = 3
  * FILLING VOID = 4 unused
 * If the filltype is 0 (FILLING HOLLOW), then all the fill parameters should take on a value of -1.
 * The fill type FILLING FILL is a solid color fill.
 * The two pairs of pitch and spacing control the fill or hatch if the fill type is FILLING MESH.
 * Only the first pair of pitch and spacing are used if the fill type is FILLING HATCH.

Example:
<pre>B 33000 67300 2000 2000 3 60 0 2 75 50 0 -1 -1 -1 -1 -1</pre>

A box with the lower left hand corner at (33000, 67300) and a width and
height of (2000, 2000), color index 3, line width of 60 mils, no cap,
dashed line type, dash length of 75 mils, dash spacing of 50 mils, no
fill, rest parameters unset. 

### circle ###

Valid in: Schematic and Symbol files

Format: <pre>type x y radius color width capstyle dashstyle dashlength dashspace filltype fillwidth angle1 pitch1 angle2 pitch2</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>V</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x</td>
		<td>int/mils</td>
		<td>Center X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y</td>
		<td>int/mils</td>
		<td>Center Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>radius</td>
		<td>int/mils</td>
		<td>Radius of the circle</td>
	</tr>
	<tr>
		<td>4</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>
	<tr>
		<td>5</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of circle line</td>
	</tr>
	<tr>
		<td>6</td>
		<td>capstyle</td>
		<td>int/mils</td>
		<td>0 unused</td>
	</tr>
	<tr>
		<td>7</td>
		<td>dashstyle</td>
		<td>int</td>
		<td>Type of dash style</td>
	</tr>
	<tr>
		<td>8</td>
		<td>dashlength</td>
		<td>int/mils</td>
		<td>Length of dash</td>
	</tr>
	<tr>
		<td>9</td>
		<td>dashspace</td>
		<td>int/mils</td>
		<td>Space inbetween dashes</td>
	</tr>
	<tr>
		<td>10</td>
		<td>filltype</td>
		<td>int</td>
		<td>Type of fill</td>
	</tr>
	<tr>
		<td>11</td>
		<td>fillwidth</td>
		<td>int/mils</td>
		<td>Width of the fill lines</td>
	</tr>
	<tr>
		<td>12</td>
		<td>angle1</td>
		<td>int/degrees</td>
		<td>First angle of fill</td>
	</tr>
	<tr>
		<td>13</td>
		<td>pitch1</td>
		<td>int/mils</td>
		<td>First pitch/spacing of fill</td>
	</tr>
	<tr>
		<td>14</td>
		<td>angle2</td>
		<td>int/degrees</td>
		<td>Second angle of fill</td>
	</tr>
	<tr>
		<td>15</td>
		<td>pitch2</td>
		<td>int/mils</td>
		<td>Second pitch/spacing of fill</td>
	</tr>
</table>

 * The dashstyle is an enumerated type:
  * TYPE SOLID = 0
  * TYPE DOTTED = 1
  * TYPE DASHED = 2
  * TYPE CENTER = 3
  * TYPE PHANTOM = 4
 * The dashlength parameter is not used for TYPE SOLID and TYPE DOTTED. This parameter should take on a value of -1 in these cases.
 * The dashspace parameter is not used for TYPE SOLID. This parameter should take on a value of -1 in these case.
 * The filltype parameter is an enumerated type:
  * FILLING HOLLOW = 0
  * FILLING FILL = 1
  * FILLING MESH = 2
  * FILLING HATCH = 3
  * FILLING VOID = 4 unused
 * If the filltype is 0 (FILLING HOLLOW), then all the fill parameters should take on a value of -1.
 * The fill type FILLING FILL is a solid color fill.
 * The two pairs of pitch and spacing control the fill or hatch if the fill type is FILLING MESH.
 * Only the first pair of pitch and spacing are used if the fill type is FILLING HATCH.

Example:
<pre>V 38000 67000 900 3 0 0 2 75 50 2 10 20 30 90 50</pre>

A circle with the center at (38000, 67000) and a radius of 900 mils,
color index 3, line width of 0 mils (smallest size), no cap, dashed line
type, dash length of 75 mils, dash spacing of 50 mils, mesh fill, 10
mils thick mesh lines, first mesh line: 20 degrees, with a spacing of
30 mils, second mesh line: 90 degrees, with a spacing of 50 mils.

### arc ###

Valid in: Schematic and Symbol files

Format: <pre>type x y radius startangle sweepangle color width capstyle dashstyle dashlength dashspace</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>A</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x</td>
		<td>int/mils</td>
		<td>Center X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y</td>
		<td>int/mils</td>
		<td>Center Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>radius</td>
		<td>int/mils</td>
		<td>Radius of the arc</td>
	</tr>
	<tr>
		<td>4</td>
		<td>startangle</td>
		<td>int/degrees</td>
		<td>Starting angle of the arc</td>
	</tr>
	<tr>
		<td>5</td>
		<td>sweepangle</td>
		<td>int/degrees</td>
		<td>Amount the arc sweeps</td>
	</tr>	
	<tr>
		<td>6</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>
	<tr>
		<td>7</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of circle line</td>
	</tr>
	<tr>
		<td>8</td>
		<td>capstyle</td>
		<td>int</td>
		<td>Cap style</td>
	</tr>	
	<tr>
		<td>9</td>
		<td>dashstyle</td>
		<td>int</td>
		<td>Type of dash style</td>
	</tr>
	<tr>
		<td>10</td>
		<td>dashlength</td>
		<td>int/mils</td>
		<td>Length of dash</td>
	</tr>
	<tr>
		<td>11</td>
		<td>dashspace</td>
		<td>int/mils</td>
		<td>Space inbetween dashes</td>
	</tr>	
</table>

 * The startangle can be negative, but not recommended.
 * The sweepangle can be negative, but not recommended.
 * The capstyle is an enumerated type:
  * END NONE = 0
  * END SQUARE = 1
  * END ROUND = 2
 * The dashstyle is an enumerated type:
  * TYPE SOLID = 0
  * TYPE DOTTED = 1
  * TYPE DASHED = 2
  * TYPE CENTER = 3
  * TYPE PHANTOM = 4
 * The dashlength parameter is not used for TYPE SOLID and TYPE DOTTED. This parameter should take on a value of -1 in these cases.
 * The dashspace parameter is not used for TYPE SOLID. This parameter should take on a value of -1 in these case.

Example:<pre>A 30600 75000 2000 0 45 3 0 0 3 75 50</pre>

An arc with the center at (30600, 75000) and a radius of 2000 mils, a
starting angle of 0, sweeping 45 degrees, color index 3, line width of
0 mils (smallest size), no cap, center line type, dash length of 75
mils, dash spacing of 50 mils.

### text and attributes ###

Depending on context, text objects can play different roles. Outside any
environment, they represent informative lines of text. When enclosed by
curly braces, they are interpreted as attributes. See the attributes
section.

Valid in: Schematic and Symbol files

Format: <pre>type x y color size visibility show_name_value angle alignment num_lines
string line 1
string line 2
string line 3
…
string line N
</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>T</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x</td>
		<td>int/mils</td>
		<td>First X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y</td>
		<td>int/mils</td>
		<td>First Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>	
	<tr>
		<td>4</td>
		<td>size</td>
		<td>int/points</td>
		<td>Size of text</td>
	</tr>
	<tr>
		<td>5</td>
		<td>visibility</td>
		<td>int</td>
		<td>Visibility of text</td>
	</tr>
	<tr>
		<td>6</td>
		<td>show_name_value</td>
		<td>int</td>
		<td>Attribute visibility control</td>
	</tr>	
	<tr>
		<td>7</td>
		<td>angle</td>
		<td>int/degrees</td>
		<td>Angle of the text</td>
	</tr>
	<tr>
		<td>8</td>
		<td>alignment</td>
		<td>int</td>
		<td>Alignment/origin of the text</td>
	</tr>
	<tr>
		<td>9</td>
		<td>num_lines</td>
		<td>int</td>
		<td>Number of lines of text (1 based)</td>
	</tr>		
	<tr>
		<td>10</td>
		<td>string line 1 … N</td>
		<td>string</td>
		<td>The text strings, on a separate line</td>
	</tr>
</table>

 * This object is a multi line object. The first line contains all the text parameters and the subsequent lines are the text strings.
 * There must be exactly num lines of text following the T … string.
 * The maximum length of any single text string is 1024, however there is no limit to the number of text string lines.
 * The minimum size is 2 points (1/72 of an inch).
 * There is no maximum size.
 * The coordinate pair is the origin of the text item.
 * The visibility field is an enumerated type:
  * INVISIBLE = 0
  * VISIBLE = 1
 * The show_name_value is an enumerated type:
  * SHOW NAME VALUE = 0 (show both name and value of an attribute)
  * SHOW VALUE = 1 (show only the value of an attribute)
  * SHOW NAME = 2 (show only the name of an attribute)
 * The show_name_value field is only valid if the string is an attribute (string has to be in the form: name=value to be considered an attribute).
 * The angle of the text can only take on one of the following values: 0, 90, 180, 270. A value of 270 will always generate upright text.
 * The alignment/origin field controls the relative location of the origin.
 * The alignment field can take a value from 0 to 8.
 * The following diagram shows what the values for the alignment field mean:
  * TODO: fileformat_textgraphic.jpg
 * The num_lines field always starts at 1.
 * The num_lines field was added starting with file format version 1. Past versions (0 or earlier) only supported single line text objects.
 * The text strings of the string line(s) can have overbars if the text is embedded in two overbar markers “\_”. A single backslash needs to be written as “\\”.

Example 1:
<pre>
T 16900 35800 3 10 1 0 0 0 1
Text string!
</pre>

A text object with the origin at (16900, 35800), color index 3, 10
points in size, visible, attribute flags not valid (not an attribute),
origin at lower left, not rotated, string: Text string!

Example 2:
<pre>
T 16900 35800 3 10 1 0 0 0 5
Text string line 1
Text string line 2
Text string line 3
Text string line 4
Text string line 5
</pre>

This is a similar text object as the above example, however here there
are five lines of text.

Example 3:
<pre>
T 10000 20000 3 10 1 1 8 90 1
pinlabel=R/\_W\_
</pre>

A text object with the origin at (10000, 20000), color index 3, 10
points in size, visible, only the value of the attribute is visible,
text origin at upper right, the text is rotated by 90 degree, the
string: “R/W” has an overbar over the “W”.

### net ###

Valid in: Schematic files ONLY

Format: <pre>type x1 y1 x2 y2 color</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>N</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x1</td>
		<td>int/mils</td>
		<td>First X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y1</td>
		<td>int/mils</td>
		<td>First Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>x2</td>
		<td>int/mils</td>
		<td>Second X coordinate</td>
	</tr>
	<tr>
		<td>4</td>
		<td>y2</td>
		<td>int/mils</td>
		<td>Second Y coordinate</td>
	</tr>
	<tr>
		<td>5</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>
</table>

 * Nets can only appear in schematic files.
 * You cannot have a zero length net (the tools will throw them away).

Example:
<pre>
N 12700 29400 32900 29400 4
</pre>
A net segment from (12700, 29400) to (32900, 29400) with color index 4.

### bus ###

Valid in: Schematic files ONLY

Format: <pre>type x1 y1 x2 y2 color ripperdir</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>U</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x1</td>
		<td>int/mils</td>
		<td>First X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y1</td>
		<td>int/mils</td>
		<td>First Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>x2</td>
		<td>int/mils</td>
		<td>Second X coordinate</td>
	</tr>		
	<tr>
		<td>4</td>
		<td>y2</td>
		<td>int/mils</td>
		<td>Second Y coordinate</td>
	</tr>
	<tr>
		<td>5</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>
	<tr>
		<td>6</td>
		<td>ripperdir</td>
		<td>int</td>
		<td>Direction of bus rippers</td>
	</tr>
</table>

 * The ripperdir field for an brand new bus is 0.
 * The ripperdir field takes on a value of 1 or -1 when a net is connected to the bus for the first time. This value indicates the direction of the ripper symbol. The ripper direction is set to the same value for the entire life of the bus object.
 * Buses can only appear in schematic files.
 * You cannot have a zero length bus (the tools will throw them away).

Example: <pre>U 27300 37400 27300 35300 3 0</pre>

A bus segment from (27300, 37400) to (27300, 35300) with color index 3
and no nets have been connected to this bus segment.

### pin ###

Valid in: Symbol files ONLY

Format: <pre>type x1 y1 x2 y2 color pintype whichend</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>P</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x1</td>
		<td>int/mils</td>
		<td>First X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y1</td>
		<td>int/mils</td>
		<td>First Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>x2</td>
		<td>int/mils</td>
		<td>Second X coordinate</td>
	</tr>		
	<tr>
		<td>4</td>
		<td>y2</td>
		<td>int/mils</td>
		<td>Second Y coordinate</td>
	</tr>
	<tr>
		<td>5</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>
	<tr>
		<td>6</td>
		<td>pintype</td>
		<td>int</td>
		<td>Type of pin</td>
	</tr>		
	<tr>
		<td>7</td>
		<td>whichend</td>
		<td>int</td>
		<td>Specifies the active end</td>
	</tr>	
</table>

 * The pintype is an enumerated type:
  * NORMAL PIN = 0
  * BUS PIN = 1 unused
 * The whichend specifies which end point of the pin is the active connection port. Only this end point can have other pins or nets connected to it.
 * To make the first end point active, whichend should be 0, else to specify the other end, whichend should be 1.
 * Pins can only appear in symbol files.
 * Zero length pins are allowed

Example: <pre>P 0 200 200 200 1 0 0</pre>

A pin from (0, 200) to (200, 200) with color index 1, a regular pin, and
the first point being the active connection end.

### component ###

Valid in: Schematic files ONLY

Format: <pre>type x y selectable angle mirror basename</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>C</td>
	</tr>
	<tr>
		<td>1</td>
		<td>x</td>
		<td>int/mils</td>
		<td>Origin X coordinate</td>
	</tr>
	<tr>
		<td>2</td>
		<td>y</td>
		<td>int/mils</td>
		<td>Origin Y coordinate</td>
	</tr>
	<tr>
		<td>3</td>
		<td>selectable</td>
		<td>int</td>
		<td>Selectable flag</td>
	</tr>	
	<tr>
		<td>4</td>
		<td>angle</td>
		<td>int/degrees</td>
		<td>Angle of the component</td>
	</tr>
	<tr>
		<td>5</td>
		<td>mirror</td>
		<td>int</td>
		<td>Mirror around Y axis</td>
	</tr>
	<tr>
		<td>6</td>
		<td>basename</td>
		<td>string</td>
		<td>The filename of the component</td>
	</tr>
</table>

The selectable field is either 1 for selectable or 0 if not selectable.

 * The angle field can only take on the following values: 0, 90, 180, 270.
 * The angle field can only be positive.
 * The mirror flag is 0 if the component is not mirrored (around the Y axis).
 * The mirror flag is 1 if the component is mirrored (around the Y axis).
 * The just basename is the filename of the component. This filename is not the full path.

Example:
<pre>C 18600 19900 1 0 0 7400-1.sym</pre>

A component who's origin is at (18600,19900), is selectable, not rotated,
not mirrored, and the basename of the component is 7400-1.sym.

### path ###

Valid in: Schematic and Symbol files

Valid since: Fileformat version 2 (release 1.5.1)

Format: <pre>type color width capstyle dashstyle dashlength dashspace filltype fillwidth angle1 pitch1 angle2 pitch2 numlines
path data line 1
path data line 2
path data line 3
…
path data line N
</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>H</td>
	</tr>
	<tr>
		<td>1</td>
		<td>color</td>
		<td>int</td>
		<td>Color index</td>
	</tr>
	<tr>
		<td>2</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of line</td>
	</tr>
	<tr>
		<td>3</td>
		<td>capstyle</td>
		<td>int</td>
		<td>Line cap style</td>
	</tr>	
	<tr>
		<td>4</td>
		<td>dashstyle</td>
		<td>int</td>
		<td>Type of dash style</td>
	</tr>
	<tr>
		<td>5</td>
		<td>dashlength</td>
		<td>int/mils</td>
		<td>Length of dash</td>
	</tr>
	<tr>
		<td>6</td>
		<td>dashspace</td>
		<td>int/mils</td>
		<td>Space inbetween dashes</td>
	</tr>	
	<tr>
		<td>7</td>
		<td>filltype</td>
		<td>int</td>
		<td>Type of fill</td>
	</tr>
	<tr>
		<td>8</td>
		<td>fillwidth</td>
		<td>int/mils</td>
		<td>Width of the fill lines</td>
	</tr>
	<tr>
		<td>9</td>
		<td>angle1</td>
		<td>int/degrees</td>
		<td>First angle of fill</td>
	</tr>		
	<tr>
		<td>10</td>
		<td>pitch1</td>
		<td>int/mils</td>
		<td>First pitch/spacing of fill</td>
	</tr>
	<tr>
		<td>11</td>
		<td>angle2</td>
		<td>int/degrees</td>
		<td>Second angle of fill</td>
	</tr>
	<tr>
		<td>12</td>
		<td>pitch2</td>
		<td>int/mils</td>
		<td>Second pitch/spacing of fill</td>
	</tr>
	<tr>
		<td>13</td>
		<td>num_lines</td>
		<td>int</td>
		<td>Number of lines of path data (1 based)</td>
	</tr>
	<tr>
		<td>14</td>
		<td>path data line 1 … N</td>
		<td>path data</td>
		<td>The path data, on separate lines</td>
	</tr>		
</table>

 * The capstyle is an enumerated type:
  * END NONE = 0
  * END SQUARE = 1
  * END ROUND = 2
 * The dashstyle is an enumerated type:
  * TYPE SOLID = 0
  * TYPE DOTTED = 1
  * TYPE DASHED = 2
  * TYPE CENTER = 3
  * TYPE PHANTOM = 4
 * The dashlength parameter is not used for TYPE SOLID and TYPE DOTTED. This parameter should take on a value of -1 in these cases.
 * The dashspace parameter is not used for TYPE SOLID. This parameter should take on a value of -1 in these case.
 * The filltype parameter is an enumerated type:
  * FILLING HOLLOW = 0
  * FILLING FILL = 1
  * FILLING MESH = 2
  * FILLING HATCH = 3
  * FILLING VOID = 4 unused
 * If the filltype is 0 (FILLING HOLLOW), then all the fill parameters should take on a value of -1.
 * The fill type FILLING FILL is a solid color fill.
 * The two pairs of pitch and spacing control the fill or hatch if the fill type is FILLING MESH.
 * Only the first pair of pitch and spacing are used if the fill type is FILLING HATCH.
 * The format of path data is deliberately similar to that of paths in the W3C SVG standard.
 * The subset of the SVG path syntax emitted by gEDA is documented below in section Path Data.
 * As an implementation detail; libgeda takes code from librsvg, an SVG parsing library. As a result, the majority of SVG path syntax is read correctly, however this is always normalised to absolute move, line, Bézier curve and close-path commands internally (and is saved as such).
 * Coordinates along the path are specified in the standard gschem coordinate space.

Example:
<pre>
H 3 10 0 0 -1 -1 0 -1 -1 -1 -1 -1 5
M 410,240
L 501,200
L 455,295
L 435,265
z
</pre>
A path starting at (410,240) with lines drawn from there, and joining
points (501,200), (455,295), (435,265), closing back to its origin. It
has color index 3, is 10 mils thick, no cap, solid style. There are 5
lines of path data.

### font ###

Valid in: Special font files ONLY

Format: <pre>type character width flag</pre>

<table>
	<tr>
		<th>Pos.</th>
		<th>Field</th>
		<th>Type/unit</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>#</td>
		<td>type</td>
		<td>char</td>
		<td>F</td>
	</tr>
	<tr>
		<td>1</td>
		<td>character</td>
		<td>char</td>
		<td>The character being defined</td>
	</tr>
	<tr>
		<td>2</td>
		<td>width</td>
		<td>int/mils</td>
		<td>Width of the character (mils)</td>
	</tr>
	<tr>
		<td>3</td>
		<td>flag</td>
		<td>int</td>
		<td>Special space flag</td>
	</tr>
</table>			

 * This is a special tag and should ONLY show up in font definition files.
 * If the font character being defined is the space character (32) then flag should be 1, otherwise 0.

Example:
<pre>
F 11 1
</pre>

The above font definition is for the space character.

## Colors ##

In the gEDA/gaf schematic and symbol file format colors are specified
via an integer index. The relationship between integer and color is
based on object type. Each object type typically has one or more colors.
Here is a table of color index to object type:

<table>
	<tr>
		<th>Index</th>
		<th>Object type</th>
	</tr>
	<tr>
		<td>0</td>
		<td>BACKGROUND_COLOR</td>
	</tr>
	<tr>
		<td>1</td>
		<td>PIN_COLOR</td>
	</tr>
	<tr>
		<td>2</td>
		<td>NET_ENDPOINT_COLOR</td>
	</tr>	
	<tr>
		<td>3</td>
		<td>GRAPHIC_COLOR</td>
	</tr>
	<tr>
		<td>4</td>
		<td>NET_COLOR</td>
	</tr>
	<tr>
		<td>5</td>
		<td>ATTRIBUTE_COLOR</td>
	</tr>
	<tr>
		<td>6</td>
		<td>LOGIC_BUBBLE_COLOR</td>
	</tr>
	<tr>
		<td>7</td>
		<td>DOTS_GRID_COLOR</td>
	</tr>
	<tr>
		<td>8</td>
		<td>DETACHED_ATTRIBUTE_COLOR</td>
	</tr>
	<tr>
		<td>9</td>
		<td>TEXT_COLOR</td>
	</tr>
	<tr>
		<td>10</td>
		<td>BUS_COLOR</td>
	</tr>
	<tr>
		<td>11</td>
		<td>SELECT_COLOR</td>
	</tr>
	<tr>
		<td>12</td>
		<td>BOUNDINGBOX_COLOR</td>
	</tr>
	<tr>
		<td>13</td>
		<td>ZOOM_BOX_COLOR</td>
	</tr>
	<tr>
		<td>14</td>
		<td>STROKE_COLOR</td>
	</tr>
	<tr>
		<td>15</td>
		<td>LOCK_COLOR</td>
	</tr>
	<tr>
		<td>16</td>
		<td>OUTPUT_BACKGROUND_COLOR</td>
	</tr>
	<tr>
		<td>17</td>
		<td>FREESTYLE1_COLOR</td>
	</tr>
	<tr>
		<td>18</td>
		<td>FREESTYLE2_COLOR</td>
	</tr>
	<tr>
		<td>19</td>
		<td>FREESTYLE3_COLOR</td>
	</tr>
	<tr>
		<td>20</td>
		<td>FREESTYLE4_COLOR</td>
	</tr>
	<tr>
		<td>21</td>
		<td>JUNCTION_COLOR</td>
	</tr>
	<tr>
		<td>22</td>
		<td>MESH_GRID_MAJOR_COLOR</td>
	</tr>
	<tr>
		<td>23</td>
		<td>MESH_GRID_MINOR_COLOR</td>
	</tr>
</table>

The actual color associated with the color index is defined on a per
tool bases. Objects are typically assigned their corresponding color
index, but it is permissible (sometimes) to assign other color index
values to different object types. 

## Attributes ###

Attributes are enclosed in braces {} and can only be text. Attributes
are text items which take on the form name=value. If it doesn't have
name=value, it's not an attribute. Attributes are attached to the
previous object. Here's an example:
<pre>
P 988 500 1300 500 1
{
T 1000 570 5 8 1 1 0
pinseq=3
T 1000 550 5 8 1 1 0
pinnumber=3
}
</pre>
The object is a pin which has an attribute pinnumber=3 and pinseq=3
(name=value). You can have multiple text objects (both the T … and text
string are required) in between the braces {}. As of 20021103, you can
only attached text items as attributes. Attaching other object types as
attributes is unsupported.
You can also have “toplevel” attributes. These attributes are not
attached to any object, but instead are just text objects that take on
the form name=value.
These attributes are useful when you need to convey some info about a
schematic page or symbol and need the netlister to have access to this
info.


## Embedded Components

Embedded components are components which have all of their definition
stored within the schematic file. When a users place a component onto a
schematic page, they have the option of making the component embedded.
Other than storing all the symbol information inside of the schematic,
an embedded component is just any other component. Embedded components
are defined as:
<pre>
C 18600 21500 1 0 0 EMBEDDD555-1.sym
[
...
... Embedded primitive objects
...
]
</pre>
In the example above, **555-1.sym** is the component. The EMBEDDED tag and
the [ ] are the distinguishing characteristics of embedded components.
**componentname.sym** must exist in one of the specified component-libraries
if you want to unembed the component.

## Path data ##

The gEDA/gaf path data format has been deliberately specified to match
a subset of that in the W3C SVG standard..

 * As an implementation detail; libgeda takes code from librsvg, an SVG parsing library. As a result, the majority of SVG path syntax is read correctly, however this is always normalised to absolute move, line, Bézier curve and close-path commands internally (and is saved as such).
 * Coordinates along the path are specified in the standard gschem coordinate space.
 * Those path commands which gEDA emits, and will guarantee to parse, are listed in the table below:
(Text taken from the above SVG specification). 
 * In the table below, the following notation is used:
  * (): grouping of parameters
  * +: 1 or more of the given parameter(s) is required
<table>
	<tr>
		<th>Command</th>
		<th>Name</th>
		<th>Parameters</th>
		<th>Description</th>
	</tr>
	<tr>
		<td>M (absolute)</td>
		<td>moveto</td>
		<td>(x,y)+</td>
		<td>Start a new sub-path at the given (x,y) coordinate. M (uppercase) indicates that absolute coordinates will follow; m (lowercase) indicates that relative coordinates will follow. If a relative moveto (m) appears as the first element of the path, then it is treated as a pair of absolute coordinates. If a moveto is followed by multiple pairs of coordinates, the subsequent pairs are treated as implicit lineto commands.</td>
	</tr>
	<tr>
		<td>L (absolute)</td>
		<td>lineto</td>
		<td>(x,y)+</td>
		<td>Draw a line from the current point to the given (x,y) coordinate which becomes the new current point. L (uppercase) indicates that absolute coordinates will follow; l (lowercase) indicates that relative coordinates will follow. A number of coordinates pairs may be specified to draw a polyline. At the end of the command, the new current point is set to the final set of coordinates provided.</td>
	</tr>
	<tr>
		<td>C (absolute)</td>
		<td>curveto</td>
		<td>(x1,y1 x2,y2 x,y)+</td>
		<td>Draws a cubic Bézier curve from the current point to (x,y) using (x1,y1) as the control point at the beginning of the curve and (x2,y2) as the control point at the end of the curve. C (uppercase) indicates that absolute coordinates will follow; c (lowercase) indicates that relative coordinates will follow. Multiple sets of coordinates may be specified to draw a polybézier. At the end of the command, the new current point becomes the final (x,y) coordinate pair used in the polybézier.</td>
	</tr>
	<tr>
		<td>Z or z</td>
		<td>closepath</td>
		<td>(none)</td>
		<td>Close the current subpath by drawing a straight line from the current point to current subpath's initial point.</td>
	</tr>
</table>

As example, lets draw the outline of an AND gate. The path data is: 
<pre>
M 100,100 L 500,100 C 700,100 800,275 800,400
C 800,525 700,700 500,700 L 100,700 z
</pre>

And a complete schematic:

<pre>
v 20080706 1
H 3 0 0 0 -1 -1 0 2 20 100 -1 -1 6
M 100,100
L 500,100
C 700,100 800,275 800,400
C 800,525 700,700 500,700
L 100,700
z
</pre>
The resulting path (with control points drawn on to illustrate their positions) is shown here:
TODO: image

## Document Revision History
November 30th, 2002	Created fleformats.tex from fleformats.html.
December 1st, 2002	Continued work on this document.
October 4th, 2003	Added new file format version flag info.
October 19th, 2003	Added num lines text field.
November 2nd, 2008	Added path object, bumping file format version to 2
May 26th, 2011	Added a column for the position of parameters in the tables
