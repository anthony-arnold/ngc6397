import numpy as np 
from astropy.table import Table

def load(src):
    data = np.loadtxt(src)
    return Table(data, names=(
        'R', 'sig', 'esig_u', 'e_sigl', 'type'
    ))

    

odata = load(
"""6.20   5.39    0.42    0.42  2
   13.50   4.71    0.27    0.25  1
   20.34   5.14    0.27    0.27  2
   31.91   4.86    0.28    0.25  1
   37.04   5.24    0.28    0.28  2
   48.06   4.36    0.25    0.23  1
   50.63   5.25    0.28    0.28  2
   63.60   4.49    0.24    0.24  2
   70.13   4.54    0.26    0.24  1
   80.97   5.42    0.28    0.28  2
   95.99   4.58    0.26    0.23  1
   98.86   4.17    0.24    0.24  2
  119.11   4.54    0.16    0.15  4
  124.07   4.29    0.24    0.22  1
  146.40   4.01    0.23    0.21  1
  175.42   3.95    0.22    0.20  1
  175.71   4.23    0.15    0.14  4
  210.29   3.97    0.22    0.20  1
  215.16   4.13    0.18    0.19  6
  223.82   4.05    0.15    0.14  4
  245.46   3.95    0.18    0.19  6
  250.25   3.63    0.20    0.19  1
  267.36   3.82    0.20    0.22  6
  272.82   3.79    0.14    0.13  4
  288.18   4.05    0.20    0.18  6
  295.45   3.72    0.20    0.19  1
  304.92   3.83    0.17    0.16  6
  323.04   3.51    0.13    0.12  4
  337.20   3.79    0.18    0.19  6
  343.41   3.50    0.19    0.18  1
  353.94   3.59    0.19    0.19  6
  376.74   3.64    0.17    0.16  6
  379.31   3.27    0.12    0.12  4
  392.89   3.45    0.19    0.17  1
  410.70   3.58    0.23    0.26  6
  448.95   3.43    0.13    0.12  4
  453.61   3.44    0.19    0.17  1
  525.00   2.94    0.16    0.15  1
  529.80   3.20    0.12    0.11  4
  595.60   3.17    0.36    0.31  1
  655.22   2.34    0.27    0.24  1
  675.77   2.94    0.16    0.15  4
  962.41   2.38    0.30    0.25  1
 1821.18   2.48    1.13    0.67  1
""".split('\n'))

