# --------------- Import packages --------------- #
from fpdf import FPDF
import pandas as pd

# --------------- Set defaults --------------- #
FILENAME = "topics.csv"

# --------------- Impor data --------------- #
df = pd.read_csv( "topics.csv" )

# --------------- Create pdf object --------------- #
pdf = FPDF( orientation = "P", unit = "mm", format = "A4" )
pdf.set_font( family = "Times", style = "B", size = 24 )
pdf.set_text_color( 100, 100, 100)


# --------------- Add pages --------------- #
for index, row in df.iterrows():
    
    pdf.add_page()
    
    pdf.cell( w = 0, h = 12, 
             txt = row["Topic"], align = "L", 
             ln = 1)
    
    pdf.cell( w = 0, h = 0,
             ln = 1, border = 1 )
    
    for x in range( 1, row["Pages"] ):
        pdf.add_page()


pdf.output( "output.pdf" )



'''
______
   |  |
   |__|
   |  |
\_/|  |

'''