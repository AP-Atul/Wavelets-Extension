"""Base Transform for doing basic calls for dwt & idwt based on the dimensions called"""

from wavelet.extension.wavelet_transform import dwt, idwt
from wavelet.util import getExponent

cimport numpy as np
import numpy as np


cdef class BaseTransform:
    def __init__(self, waveletName):
        print("Using coif1")

    cpdef waveDec1(self, np.ndarray arrTime, int level):
        cdef int length = 0
        cdef np.ndarray arrHilbert = arrTime.copy()
        cdef int dataLength = len(arrHilbert)
        cdef int transformWaveletLength = 2
        cdef np.ndarray arrTemp

        while dataLength >= transformWaveletLength and length < level:
            arrTemp = dwt(arrHilbert, dataLength)
            arrHilbert[: len(arrTemp)] = arrTemp

            dataLength >>= 1
            length += 1

        return arrHilbert

    cpdef waveRec1(self, np.ndarray arrHilbert, int level):
        cdef np.ndarray arrTime = arrHilbert.copy()
        cdef np.ndarray arrTemp
        cdef int dataLength = len(arrTime)
        cdef int transformWaveletLength = 2
        cdef int h = transformWaveletLength

        cdef int steps = getExponent(dataLength)
        for _ in range(level, steps):
            h <<= 1

        while len(arrTime) >= h >= transformWaveletLength:
            arrTemp = idwt(arrTime, h)
            arrTime[: len(arrTemp)] = arrTemp

            h <<= 1

        return arrTime
