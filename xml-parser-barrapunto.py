#!/usr/bin/python
# -*- coding: utf-8 -*-

import string
from xml.sax.handler import ContentHandler
from xml.sax import make_parser
import sys


def normalize_whitespace(texto):
    return string.join(string.split(texto), ' ')

def Title(contador):
    if contador == 1:
        titulo = "Primer"
    elif contador == 2:
        titulo = "Segundo"
    elif contador == 3:
        titulo = "Tercer"
    elif contador == 4:
        titulo = "Cuarto"
    elif contador == 5:
        titulo = "Quinto"
    elif contador == 6:
        titulo = "Sexto"
    elif contador == 7:
        titulo = "Septimo"
    elif contador == 8:
        titulo = "Octavo"
    elif contador == 9:
        titulo = "Noveno"
    elif contador == 10:
        titulo = "Décimo"
    return titulo


class CounterHandler(ContentHandler):

    def __init__(self):
        self.titulo = ""
        self.theContent = ""
        self.numeroTitulo = 1
        self.inContent = False
        self.salida = ""
        self.fichero = open("fichero.html", "w")
        

    def startElement(self, name, attrs):
        if name == 'item':
            self.inContent = True
            self.link = normalize_whitespace(attrs.get('rdf:about'))

    def endElement(self, name):
        if self.inContent:
            self.theContent = normalize_whitespace(self.theContent)
        if name == 'title' and self.inContent:
            self.titulo = Title(self.numeroTitulo) 
            self.salida = ("<li><a href=" + self.link + ">" +
                            self.theContent + "</a></li>\n")
            self.fichero.write(self.salida.encode('utf-8'))
            print "El " + self.titulo +\
            " titulo se ha copiado a XML correctamente"
            self.theContent = ""
            self.inContent = False
            if self.numeroTitulo < 10:
                self.numeroTitulo = self.numeroTitulo + 1
            

    def characters(self, chars):
        if self.inContent:
            self.theContent = self.theContent + chars


# --- Main prog

if len(sys.argv) < 2:
    print "Usage: python xml-parser-barrapunto.py <document>"
    print
    print " <document>: file name of the document to parse"
    sys.exit(1)

# Load parser and driver

JokeParser = make_parser()
JokeHandler = CounterHandler()
JokeParser.setContentHandler(JokeHandler)

# Ready, set, go!

ficheroXML = open(sys.argv[1], "r")
JokeParser.parse(ficheroXML)

print "Parse finalizado"
