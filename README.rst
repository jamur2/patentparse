Patentparse
===========

A parsing library for patents.

This library is a shallow wrapper around ElementTree to provide easy access to
Google's patent data archive
(http://www.google.com/googlebooks/uspto-patents-grants-text.html)

This is currently only expected to parse patents granted after 2001.


Usage
=====

A patent takes a raw XML string::

    >>> import patentparse.patent
    >>> patent = patent.patentparse.Patent(xml_contents)

It has some attributes to get at commonly-used information:

    >>> patent.invention_title
    "Method and system for preventing copying of information from previews of webpages"
    >>> patent.doc_number
    "08615810"
    >>> patent.claims
    ['\n1. A method of providing a copy prevention feature...]

It also gives access to the ElementTree itself, for any information not
available by the Patent API.

    >>> patent.tree.find('.//invention-title').text
    "Method and system for preventing copying of information from previews of webpages"

And a JSON serialization::

    >>> patent.json
    '{"claims": ["\\n1. A method of providing a copy prevention feature...,
    "doc_number": "08615810",
    "invention_title": "Method and system for preventing copying of information from previews of webpages"}'


Bulk parsing
============

Google provides weekly dumps of all patent grants in a single XML file.
```patentparse.parse``` can be used to get an efficient Patent generator for
all patents in the file.::

    >>> import patentparse.parse
    >>> patents = patentparse.parse('file.xml')
