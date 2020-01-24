from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
 
doc = SimpleDocTemplate("simple_table2.pdf", pagesize=letter)
# container for the 'Flowable' objects
elements = []
 
data = [['S', 'L', 'O', 'S', 'I', 'R', 'D', 'P', 'U', 'C', 'R', 'E', 'T', 'T', 'U', 'B', 'E', 'A', 'S', 'G'], ['Y', 'R', 'E', 'D', 'N', 'E', 'V', 'A', 'L', 'A', 'L', 'O', 'U', 'L', 'U', 'A', 'N', 'R', 'U', 'N'], ['S', 'E', 'S', 'N', 'L', 'L', 'V', 'E', 'O', 'T', 'E', 'L', 'T', 'S', 'Y', 'L', 'O', 'S', 'I', 'U'], ['U', 'E', 'S', 'M', 'A', 'R', 'T', 'I', 'H', 'E', 'I', 'C', 'O', 'P', 'N', 'I', 'I', 'R', 'G', 'L'], ['Q', 'W', 'F', 'F', 'T', 'V', 'A', 'T', 'D', 'P', 'R', 'N', 'I', 'A', 'E', 'N', 'T', 'H', 'I', 'R'], ['O', 'E', 'I', 'I', 'T', 'E', 'U', 'Q', 'U', 'O', 'B', 'E', 'N', 'I', 'M', 'S', 'A', 'J', 'T', 'T'], ['G', 'N', 'L', 'S', 'N', 'S', 'N', 'A', 'P', 'D', 'R', 'A', 'G', 'O', 'N', 'O', 'N', 'U', 'R', 'A'], ['Z', 'S', 'L', 'K', 'T', 'A', 'T', 'B', 'O', 'F', 'O', 'E', 'K', 'R', 'O', 'I', 'R', 'R', 'T', 'D'], ['A', 'D', 'E', 'E', 'C', 'E', 'A', 'S', 'M', 'D', 'P', 'L', 'A', 'L', 'O', 'C', 'A', 'E', 'I', 'N'], ['I', 'O', 'T', 'U', 'R', 'U', 'R', 'E', 'O', 'S', 'L', 'A', 'I', 'C', 'N', 'R', 'C', 'A', 'Y', 'V'], ['A', 'R', 'M', 'I', 'O', 'U', 'S', 'I', 'I', 'S', 'I', 'Z', 'T', 'O', 'K', 'A', 'D', 'I', 'T', 'E'], ['M', 'N', 'A', 'G', 'D', 'R', 'A', 'Y', 'A', 'U', 'U', 'A', 'T', 'P', 'A', 'U', 'C', 'L', 'N', 'E'], ['N', 'E', 'R', 'R', 'N', 'A', 'G', 'L', 'E', 'L', 'D', 'S', 'E', 'D', 'L', 'E', 'N', 'O', 'Y', 'O'], ['O', 'D', 'I', 'N', 'I', 'L', 'O', 'I', 'E', 'N', 'R', 'D', 'S', 'W', 'I', 'A', 'I', 'N', 'S', 'E'], ['G', 'L', 'G', 'N', 'N', 'N', 'N', 'R', 'Z', 'I', 'O', 'E', 'N', 'I', 'R', 'O', 'M', 'G', 'I', 'D'], ['A', 'O', 'O', 'I', 'E', 'J', 'A', 'E', 'I', 'D', 'E', 'H', 'I', 'L', 'C', 'I', 'C', 'A', 'A', 'N'], ['N', 'G', 'L', 'A', 'A', 'F', 'A', 'L', 'R', 'I', 'L', 'A', 'O', 'U', 'U', 'R', 'N', 'M', 'D', 'A'], ['O', 'D', 'D', 'A', 'F', 'F', 'O', 'D', 'I', 'L', 'R', 'R', 'P', 'N', 'B', 'O', 'A', 'R', 'U', 'C'], ['G', 'P', 'Z', 'I', 'N', 'N', 'I', 'A', 'N', 'S', 'U', 'E', 'H', 'O', 'O', 'D', 'A', 'N', 'N', 'O'], ['D', 'A', 'U', 'S', 'R', 'H', 'O', 'D', 'O', 'D', 'E', 'N', 'D', 'R', 'O', 'N', 'E', 'D', 'S', 'A']]
t=Table(data)
elements.append(t)
# write the document to disk
doc.build(elements)