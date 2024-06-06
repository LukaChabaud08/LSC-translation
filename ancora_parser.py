"""
MIT License

English

Copyright (c) 2019 Orlando Montenegro

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Spanish

Copyright (c) 2019 Orlando Montenegro

Se concede permiso por la presente, libre de cargos, a cualquier persona que obtenga 
una copia de este software y de los archivos de documentación asociados (el "Software"), 
a utilizar el Software sin restricción, incluyendo sin limitación los derechos a usar, 
copiar, modificar, fusionar, publicar, distribuir, sublicenciar, y/o vender copias del 
Software, y a permitir a las personas a las que se les proporcione el Software a hacer 
lo mismo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o 
partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "COMO ESTÁ", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, 
INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN PROPÓSITO 
PARTICULAR E INCUMPLIMIENTO. EN NINGÚN CASO LOS AUTORES O PROPIETARIOS DE LOS DERECHOS DE 
AUTOR SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA 
EN UNA ACCIÓN DE CONTRATO, AGRAVIO O CUALQUIER OTRO MOTIVO, DERIVADAS DE, FUERA DE O EN 
CONEXIÓN CON EL SOFTWARE O SU USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE.
"""

import xml.dom.minidom
import os
from tqdm import tqdm

path = os.getcwd() + "/data/ancora-2.0"

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        if ".xml" in file:
            files.append(os.path.join(r, file))


def getWord(node):
    oracion = ""
    for parent in node.childNodes:
        if parent.nodeType != parent.TEXT_NODE:
            if parent.getAttribute("wd") != "":
                oracion += parent.getAttribute("wd").replace("_", " ") + " "
            else:
                oracion += getWord(parent)

    return oracion


output_file = path.replace("ancora-2.0", "ancora-raw") + "/ancora-cat.txt"

if not os.path.exists(os.path.dirname(output_file)):
    os.makedirs(os.path.dirname(output_file))

with open(output_file, "w+") as fp:
    for f in tqdm(files):
        doc = xml.dom.minidom.parse(f)
        sentence = doc.getElementsByTagName("sentence")
        for tag in sentence:
            # print getWord(tag)
            fp.write(getWord(tag) + "\n")
