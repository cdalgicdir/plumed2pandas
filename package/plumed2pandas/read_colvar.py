# -*- Mode: python; tab-width: 4; indent-tabs-mode:nil; coding:utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
# plumed2pandas --- https://github.com/cdalgicdir/plumed2pandas

r''' plumed2pandas
=================================================================================
'''

import os
import numpy as np
import pandas as pd


def read_colvar(filename, time_decimal=2):
    '''Read a `COLVAR` file of `PLUMED` and convert it to `pandas` dataframe

    Parameters
    ----------
    filename : string
    time_decimal : integer
                   number of decimals for time values (default=2)

    Returns
    -------
    df : pandas dataframe
       returns the pandas dataframe
    '''

    if os.path.exists(filename):
        with open(filename, "r") as f:
            line = f.readline()
            line_elements = line.split()
            assert ''.join(line_elements[0:2]) == '#!FIELDS', \
                    'Missing header "#! FIELDS" in {}!'.format(filename)
            columns = line_elements[2:]
            df = pd.read_csv(filename, comment='#', header=None, \
                             names=columns, delim_whitespace=True)
        if 'time' in df.columns:
            df['time'] = df['time'].round(decimals=time_decimal)
    return df
