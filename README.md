# Redacto
Developing a lightweight software as a solution for lawyers to quickly redact tax forms.

For a document to be properly redacted according to law, just merely covering the sensitive text with a drawn box doesn't cut it.
Technically, that sensitive text remains in existence in the source code of the pdf file.

I have a few ideas of things I need to do to approach the problems this poses.

First, I need to be able to search the pdf and identify where the sensitive info is, the specific position, IE social security numbers, phone numbers etc
        This may be possible by using a python library like pymupdf to search for the text and get the position
        
Secondly, I need to put a black blox over the top of the sensitive information
        This may be possible by using some sort of built in function from a python library like pymupdf
        or possibly converting the pdf into an image and using a draw function
        
Thirdly, I need to be able to delete the previous information that remains in the source code
        This could be possible by converting the pdf into its source code, searching it for the desired object and deleting it.
        or by taking the pdf image with the black box and reconverting it into a pdf.
        
So maybe what the process could be is,
import the libraries, and the path of the file

use PyMuPDF to search for the sensitive info
use the pymudpdf function to highlight or encircle the info
hjgjgj

use another library to convert the pdf to an image
search the image for the color thats highlighted to get the position
then fill then draw those pixels black on the image and save it

then take the saved image and convert it back into a pdf 
and do it like that
change it again twice or thrice



        
        
        
        
        goredacto.com is available
        redactify potentially
        
