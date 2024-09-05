# 1 -možnost

import data
print (data.list) #s tečkovou notací

# 2 -možnost
from data import list
print(list)

# 3 -možnost moc se nepoužívá

from data import * #naimportuje uplně vše :-)
print(list)

# 4 - alias
import data as d
print(d.list)
