# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 10:08:28 2017

@author: sajid

Based on the MATLAB code by Michael Wojcik

"""

#importing required libraries
import numpy as np 


def spinavej(x):
    '''
    read the shape and dimensions of the input image
    '''
    shape = np.shape(x)     
    dim = np.size(shape)
    '''
    Depending on the dimension of the image 2D/3D, create an array of integers 
    which increase with distance from the center of the array
    '''
    if dim == 2 :
        nr,nc = shape
        nrdc = np.floor(nr/2)+1
        ncdc = np.floor(nc/2)+1
        r = np.arange(nr)-nrdc + 1
        c = np.arange(nc)-ncdc + 1 
        [R,C] = np.meshgrid(r,c)
        index = np.round(np.sqrt(R**2+C**2))+1    
    
    elif dim == 3 :
        nr,nc,nz = shape
        nrdc = np.floor(nr/2)+1
        ncdc = np.floor(nc/2)+1
        nzdc = np.floor(nz/2)+1
        r = np.arange(nr)-nrdc + 1
        c = np.arange(nc)-ncdc + 1 
        z = np.arange(nc)-nzdc + 1 
        [R,C,Z] = np.meshgrid(r,c,z)
        index = np.round(np.sqrt(R**2+C**2+Z**2))+1    
    else :
        print('input is neither a 2d or 3d array')
    '''
    The index array has integers from 1 to maxindex arranged according to distance
    from the center
    '''
    maxindex = np.max(index)
    output = np.zeros(int(maxindex),dtype = complex)

    '''
    In the next step the output is generated. The output is an array of length
    maxindex. The elements in this array corresponds to the sum of all the elements
    in the original array correponding to the integer position of the output array 
    divided by the number of elements in the index array with the same value as the
    integer position. 
    
    Depening on the size of the input array, use either the pixel or index method.
    By-pixel method for large arrays and by-index method for smaller ones.
    '''
    if  nr >= 512:
        print('performed by pixel method')
        sumf = np.zeros(int(maxindex),dtype = complex)
        count = np.zeros(int(maxindex),dtype = complex )
        for ri in range(nr):
            for ci in range(nc):
                sumf[int(index[ri,ci])-1] = sumf[int(index[ri,ci])-1] + x[ri,ci]
                count[int(index[ri,ci])-1] = count[int(index[ri,ci])-1] + 1 
        output = sumf/count
        return output
    else :
        print('performed by index method')
        indices = []
        for i in np.arange(int(maxindex)):
            indices.append(np.where(index == i+1))
        for i in np.arange(int(maxindex)):
            output[i] = sum(x[indices[i]])/len(indices[i][0])
        return output