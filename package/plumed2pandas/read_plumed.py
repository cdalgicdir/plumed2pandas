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


def read_plumed(filename, time_decimal=2):
    '''Reads a `PLUMED` file, i.e. `COLVAR`, `fes.dat`, `pmf.dat` and converts it to `pandas` dataframe

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
    else:
        raise FileNotFoundError('File {} not found!'.format(filename))

def read_colvar(filename, time_decimal=2):
    '''Reads a `COLVAR` file of `PLUMED` and convert it to `pandas` dataframe

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

    return read_plumed(filename, time_decimal=time_decimal)

def read_hills(filename, time_decimal=2):
    '''Reads a metadynamics bias potential file (`HILLS`) file of `PLUMED` and convert it to `pandas` dataframe

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

    return read_plumed(filename, time_decimal=time_decimal)

def read_fes(filename, time_decimal=2):
    '''Reads a free energy surface (`fes.dat`) file of `PLUMED` and convert it to `pandas` dataframe

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

    return read_plumed(filename, time_decimal=time_decimal)
