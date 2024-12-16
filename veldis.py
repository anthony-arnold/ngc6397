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


odata_martens = load(
"""6.20   5.39    0.42    0.42  2
    7.17   5.74    0.33    0.30  1
   15.11   5.51    0.32    0.29  1
   20.34   5.14    0.27    0.27  2
   21.11   5.50    0.32    0.29  1
   28.51   5.48    0.31    0.29  1
   37.04   5.24    0.28    0.28  2
   37.09   5.01    0.29    0.27  1
   50.63   5.25    0.28    0.28  2
   51.54   4.71    0.27    0.25  1
   63.60   4.49    0.24    0.24  2
   76.22   4.73    0.26    0.25  1
   80.97   5.42    0.28    0.28  2
   98.86   4.17    0.24    0.24  2
  101.69   4.44    0.25    0.23  1
  119.11   4.54    0.16    0.15  4
  127.03   4.27    0.24    0.23  1
  149.85   3.94    0.23    0.21  1
  175.71   4.23    0.15    0.14  4
  180.69   3.92    0.22    0.19  1
  219.77   3.90    0.21    0.20  1
  223.82   4.05    0.15    0.14  4
  262.18   3.63    0.20    0.18  1
  272.82   3.79    0.14    0.13  4
  309.12   3.62    0.19    0.19  1
  323.04   3.51    0.13    0.12  4
  356.55   3.42    0.19    0.17  1
  379.31   3.27    0.12    0.12  4
  393.79   3.33    0.27    0.23  1
  423.44   3.42    0.27    0.24  1
  448.95   3.43    0.13    0.12  4
  455.91   3.68    0.29    0.26  1
  486.83   2.68    0.22    0.20  1
  525.23   3.01    0.24    0.22  1
  529.80   3.20    0.12    0.11  4
  581.24   2.92    0.23    0.21  1
  675.77   2.94    0.16    0.15  4
  868.11   2.39    0.20    0.18  1
""".split("\n"))

odata_latest= load(
"""6.20   5.39    0.42    0.42  2
    7.22   5.81    0.33    0.31  1
   15.31   5.29    0.30    0.28  1
   20.34   5.14    0.27    0.27  2
   21.56   5.53    0.31    0.29  1
   29.40   5.30    0.31    0.28  1
   37.04   5.24    0.28    0.28  2
   39.20   4.83    0.28    0.26  1
   50.63   5.25    0.28    0.28  2
   60.42   4.96    0.28    0.26  1
   63.60   4.49    0.24    0.24  2
   80.97   5.42    0.28    0.28  2
   92.52   4.54    0.25    0.23  1
   98.86   4.17    0.24    0.24  2
  119.11   4.54    0.16    0.15  4
  124.71   4.13    0.24    0.21  1
  155.45   3.97    0.22    0.21  1
  175.71   4.23    0.15    0.14  4
  192.73   3.90    0.22    0.19  1
  223.82   4.05    0.15    0.14  4
  234.58   3.78    0.20    0.19  1
  272.82   3.79    0.14    0.13  4
  277.66   3.65    0.20    0.19  1
  323.04   3.51    0.13    0.12  4
  325.86   3.58    0.20    0.18  1
  373.33   3.29    0.18    0.17  1
  379.31   3.27    0.12    0.12  4
  412.60   3.42    0.27    0.24  1
  446.15   3.43    0.27    0.24  1
  448.95   3.43    0.13    0.12  4
  476.82   3.10    0.25    0.22  1
  510.96   3.03    0.24    0.22  1
  529.80   3.20    0.12    0.11  4
  561.27   2.94    0.23    0.21  1
  667.05   2.54    0.21    0.18  1
  675.77   2.94    0.16    0.15  4
 1188.33   2.35    0.36    0.29  1
""".split("\n"))

data_update = load(
"""6.20   5.39    0.42    0.42  2
    7.22   5.81    0.33    0.31  1
   15.31   5.29    0.30    0.28  1
   20.34   5.14    0.27    0.27  2
   21.56   5.53    0.31    0.29  1
   29.40   5.30    0.31    0.28  1
   37.04   5.24    0.28    0.28  2
   39.20   4.83    0.28    0.26  1
   50.63   5.25    0.28    0.28  2
   60.42   4.96    0.28    0.26  1
   63.60   4.49    0.24    0.24  2
   80.97   5.42    0.28    0.28  2
   92.52   4.54    0.25    0.23  1
   98.86   4.17    0.24    0.24  2
  124.71   4.13    0.24    0.21  1
  155.45   3.97    0.22    0.21  1
  192.73   3.90    0.22    0.19  1
  234.58   3.78    0.20    0.19  1
  277.66   3.65    0.20    0.19  1
  325.86   3.58    0.20    0.18  1
  373.33   3.29    0.18    0.17  1
  412.60   3.42    0.27    0.24  1
  446.15   3.43    0.27    0.24  1
  476.82   3.10    0.25    0.22  1
  510.96   3.03    0.24    0.22  1
  561.27   2.94    0.23    0.21  1
  667.05   2.54    0.21    0.18  1
 1188.33   2.35    0.36    0.29  1   
   41.63   5.21    0.24    0.22  4
   71.60   4.94    0.22    0.21  4
  119.24   4.18    0.19    0.17  4
  150.78   4.20    0.19    0.17  4
  187.73   4.35    0.19    0.18  4
  231.34   4.24    0.19    0.18  4
  284.47   4.23    0.19    0.17  4
  355.12   3.71    0.16    0.16  4
  486.84   3.74    0.17    0.16  4
  672.59   2.90    0.13    0.12  4
  846.78   2.59    0.12    0.11  4
 1174.64   2.22    0.10    0.10  4
 1785.18   2.27    0.16    0.14  4
""".split("\n"))
