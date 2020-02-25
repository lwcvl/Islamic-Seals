# Islamic-Seals
We shall use machine learning to identify and classify seals and stamps in ancient manuscripts. Currently, we are focussed on the StaBi collection and building our toolset from the ground up.

This repository is a first step towards the compilation of an Islamic seals database comprising the following components:
- digital photos of pages with seals, retraceable to the original artifact.
- cut-outs of seals.
- scripts for aggregating these resources.
- scripts for automatically identifying similar/same seals.

Pending interest, the project would amass more of these resources and add scripts for identifying seals generally (using machine learning), interfaces for interacting with the generated output, a further classification and refining of the seals themselves.

## Images from the Staatsbibliothek zu Berlin
These images were extracted from the Staatsbibliothek zu Berlin digital collections website. They can be retraced to their origin as follows: the PPN number is an identification for the object. The following number identifies the page.

For a direct verification of the image, use the IIIF server by reconstructing the URL with this formula:  `https://content.staatsbibliothek-berlin.de/dms/` then the PPN number, then `/full/0/` then the page number ending with `.jpg`

The associated catalog page and manuscript viewer can be found by reconstruction the URL with this formula: `https://digital.staatsbibliothek-berlin.de/werkansicht?PPN=` followed by the PPN number.

These images were assumed to be published by the StaBi and/or Stiftung Preußischer Kulturbesitz in the public domain per https://digital.staatsbibliothek-berlin.de/nutzungsbedingungen They have been brought together here strictly for research purposes with no further rights claimed.
