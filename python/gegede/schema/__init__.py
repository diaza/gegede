#!/usr/bin/env python
'''The module holds the default schema definition for the geometry description elements.

The schema is a dictionary with an item for each major category in the
schema.  The item's value is in a form which is category dependent.  

In general, leaf elements are described by a 2-tuple holding a data
member name and a pro typical value.  This value must be either an
object or a string that can be interpreted into an object in a
category-dependent manner.  

Shapes ("solids") follow the conventions shows in Geant4 and ROOT:

http://geant4.web.cern.ch/geant4/G4UsersDocuments/UsersGuides/ForApplicationDeveloper/html/Detector/geomSolids.html
http://root.cern.ch/root/html534/guides/users-guide/Geometry.html#shapes

 - the naming conventions of Geant4 are taken for the shapes (although we call them "shapes" not solids")

 - where applicable, the dimensions of solids are expressed as "half lengths" an such values are indicated with a "d" in their name (eg, "dx", "dy", "dz", "dphi").

 - all dimensions must be expressed in a quantity with the appropriate unit

'''

Schema = dict(

    shapes = dict(
        Box = (("dx","1m"), ("dy","1m"), ("dz","1m")),
        Tubs = (("rmin", "0m"), ("rmax","1m"), ("dz", "1m"),
               ("sphi","0deg"), ("dphi", "360deg")),
        Sphere = (("rmin", "0m"), ("rmax","1m"),
                    ("sphi","0deg"), ("dphi", "360deg"),
                    ("stheta","0deg"), ("dtheta", "180deg")),
        # fixme: fill in the rest!
        ),

    matter = dict(
        Element = (("symbol",str), ("z",int), ("a","0.0g/mole")),
        Isotope = (("z",int), ("ia",int), ("a","0.0g/mole")),
        Composition = (("symbol",str), ("isotopes", list)),

        # a material with no specific constituents
        Amalgam = (("z", int), ("a","0.0g/mole"), ("density", "0.0g/cc")),

        # A molecule is a Material with a number of elements
        Molecule = (("density", "0.0g/cc"), ("elements", list)),

        # A mixture is a Material that has a number of elements or
        # other materials added by mass fraction.
        Mixture = (("density", "0.0g/cc"), ("components", list)),

        # fixme, these need to also take state, temperature and pressure
        ),

)

