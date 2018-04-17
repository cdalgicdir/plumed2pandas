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


def read_pmf(filename, rename_errors=True, drop_inf_nan=False):
    '''Read a potential of mean force (`pmf.dat`) file from `Alan Grossfield`'s `wham` script and convert it to `pandas` dataframe

    Parameters
    ----------
    filename : string
    rename_errors : boolean
                    if True, renames the error columns from +/- to err_Property
                    default False
    drop_inf_nan : boolean
                    if True, drops the infinite and NaN values, default False
                    resets and drops the original index

    Returns
    -------
    df : pandas dataframe
         pandas dataframe of the pmf
    '''

    if os.path.exists(filename):
        with open(filename, "r") as f:
            line = f.readline()
            assert line[0] == '#', 'Missing header "#" in {}!'.format(filename)
            columns = line[1:].split()
            df = pd.read_csv(filename, comment='#', header=None, \
                             names=columns, delim_whitespace=True)

        if rename_errors:
            rename_dict = {}
            for i, c in enumerate(df.columns):
                if '+/-' in c:
                    rename_dict[c] = 'err_{}'.format(df.columns[i-1])
            df = df.rename(rename_dict, axis='columns')

        if drop_inf_nan:
            df = df[~df.isin([np.nan, np.inf, -np.inf]).any(1)]
            df.reset_index(inplace=True, drop=True)
        return df

    else:
        raise FileNotFoundError('File {} not found!'.format(filename))
