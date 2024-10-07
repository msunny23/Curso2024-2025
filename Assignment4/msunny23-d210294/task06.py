# -*- coding: utf-8 -*-
"""Task06.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nyR-tTtqy8h8yv5vyeslI7oljBQElfoi

**Task 06: Modifying RDF(s)**
"""

!pip install rdflib
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2024-2025/master/Assignment4/course_materials"

"""Read the RDF file as shown in class"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create new classes for "School" and "University. Add an rdfs:label in Spanish"**

"""

# TO DO
g.add((ns.University, RDF.type, RDFS.Class))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

# TO DO
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smithers"**"""

# TO DO
janeSmithersURI = ns.JaneSmithers
g.add((janeSmithersURI, RDF.type, ns.Researcher))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.4: Add to the individual JaneSmithers the email address, fullName, given and family names. Use the https://schema.org vocabulary**"""

# TO DO
SCHEMA = Namespace("http://schema.org/")
g.add((ns.JaneSmithers, SCHEMA.fullName, Literal("Jane Smithers")))
g.add((ns.JaneSmithers, SCHEMA.email, Literal("jane_smithers@example.org")))
g.add((ns.JaneSmithers, SCHEMA.givenName, Literal("Jane")))
g.add((ns.JaneSmithers, SCHEMA.familyName, Literal("Smithers")))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.5: Add UPM as the university where John Smith works. Use the "https://example.org/ namespace**"""

# TO DO
EX = Namespace("http://example.org/")
johnUri = EX.JohnSmith
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
g.add((ns.UPM, RDF.type, ns.University))
g.add((johnUri, EX.worksAt, ns.UPM))
# Visualize the results
for s, p, o in g:
  print(s,p,o)

"""**Task 6.6: Add that Jown knows Jane using the FOAF vocabulary. Make sure the relationship exists.**"""

# TO DO
from rdflib import FOAF
g.add((EX.JohnSmith, FOAF.knows, EX.JaneSmithers))
# Visualize the results
for s, p, o in g:
    print(s, p, o)