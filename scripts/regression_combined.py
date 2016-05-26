#------------------------------------------------------------------------------
# Copyright (c) 2015, 2016, The University of Manchester, UK.
#
# Licenced under BSD. See LICENCE for details.
#
# Authors: Arturo Wong, Robert Haines
#------------------------------------------------------------------------------

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def regression(file_name, second_index_quality, order):

    COLUMN_SEPARATOR = ','
    metrics_data = pd.DataFrame.from_csv(file_name, sep=COLUMN_SEPARATOR, header=None)
    labels = ['',
              'Test Coverage',
              'Branch Coverage',
              'McCabe\'s Cyclomatic Complexity (CC)',
              'Lines of Code (LOC)',
              'Number of local Methods (NOM)',
              'Improvement of Lack of Cohesion in Methods (ILCOM)',
              'Lack of Documentation (LOD)',
              'Depth of Inheritance Tree (DIT)',
              'Coupling Between Objects (CBO)'
             ]

    x = [0,0]
    ys = [0,0]
    for i in range(0, 2):
        x[i] = metrics_data[i + 1]
        y = metrics_data[second_index_quality]

        coeffs = np.polyfit(x[i], y, order)
        polynomial = np.poly1d(coeffs)
        ys[i] = polynomial(x[i])

    plt.figure(second_index_quality - 2)
    plt.xlabel("Coverage")
    plt.ylabel(labels[second_index_quality])
    plt.title(labels[second_index_quality])
    plt.plot(x[0], ys[0])
    plt.plot(x[1], ys[1])
    plt.legend([labels[1], labels[2]], loc='upper right')


file_path = '../data/combined/Merge/Merge all projects.csv'
for x in range(3,10):
    regression(file_path, x, 1)
    plt.show()
