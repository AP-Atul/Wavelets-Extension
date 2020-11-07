""" Daubechies 20 wavelet """


class Daubechies20:
    """
    Properties
    ----------
    asymmetric, orthogonal, bi-orthogonal

    All values are from http://wavelets.pybytes.com/wavelet/db20/
    """
    __name__ = "Daubechies Wavelet 20"
    __motherWaveletLength__ = 40  # length of the mother wavelet
    __transformWaveletLength__ = 2  # minimum wavelength of input signal

    # decomposition filter
    # low-pass
    decompositionLowFilter = [
        -2.998836489615753e-10,
        4.05612705554717e-09,
        -1.814843248297622e-08,
        2.0143220235374613e-10,
        2.633924226266962e-07,
        -6.847079596993149e-07,
        -1.0119940100181473e-06,
        7.241248287663791e-06,
        -4.376143862182197e-06,
        -3.710586183390615e-05,
        6.774280828373048e-05,
        0.00010153288973669777,
        -0.0003851047486990061,
        -5.349759844340453e-05,
        0.0013925596193045254,
        -0.0008315621728772474,
        -0.003581494259744107,
        0.00442054238676635,
        0.0067216273018096935,
        -0.013810526137727442,
        -0.008789324924555765,
        0.03229429953011916,
        0.0058746818113949465,
        -0.061722899624668884,
        0.005632246857685454,
        0.10229171917513397,
        -0.024716827337521424,
        -0.1554587507060453,
        0.039850246458519104,
        0.22829105082013823,
        -0.016727088308801888,
        -0.3267868004335376,
        -0.13921208801128787,
        0.36150229873889705,
        0.6104932389378558,
        0.4726961853103315,
        0.21994211355113222,
        0.06342378045900529,
        0.010549394624937735,
        0.0007799536136659112
    ]

    # high-pass
    decompositionHighFilter = [
        -0.0007799536136659112,
        0.010549394624937735,
        -0.06342378045900529,
        0.21994211355113222,
        -0.4726961853103315,
        0.6104932389378558,
        -0.36150229873889705,
        -0.13921208801128787,
        0.3267868004335376,
        -0.016727088308801888,
        -0.22829105082013823,
        0.039850246458519104,
        0.1554587507060453,
        -0.024716827337521424,
        -0.10229171917513397,
        0.005632246857685454,
        0.061722899624668884,
        0.0058746818113949465,
        -0.03229429953011916,
        -0.008789324924555765,
        0.013810526137727442,
        0.0067216273018096935,
        -0.00442054238676635,
        -0.003581494259744107,
        0.0008315621728772474,
        0.0013925596193045254,
        5.349759844340453e-05,
        -0.0003851047486990061,
        -0.00010153288973669777,
        6.774280828373048e-05,
        3.710586183390615e-05,
        -4.376143862182197e-06,
        -7.241248287663791e-06,
        -1.0119940100181473e-06,
        6.847079596993149e-07,
        2.633924226266962e-07,
        -2.0143220235374613e-10,
        -1.814843248297622e-08,
        -4.05612705554717e-09,
        -2.998836489615753e-10
    ]

    # reconstruction filters
    # low pass
    reconstructionLowFilter = [
        0.0007799536136659112,
        0.010549394624937735,
        0.06342378045900529,
        0.21994211355113222,
        0.4726961853103315,
        0.6104932389378558,
        0.36150229873889705,
        -0.13921208801128787,
        -0.3267868004335376,
        -0.016727088308801888,
        0.22829105082013823,
        0.039850246458519104,
        -0.1554587507060453,
        -0.024716827337521424,
        0.10229171917513397,
        0.005632246857685454,
        -0.061722899624668884,
        0.0058746818113949465,
        0.03229429953011916,
        -0.008789324924555765,
        -0.013810526137727442,
        0.0067216273018096935,
        0.00442054238676635,
        -0.003581494259744107,
        -0.0008315621728772474,
        0.0013925596193045254,
        -5.349759844340453e-05,
        -0.0003851047486990061,
        0.00010153288973669777,
        6.774280828373048e-05,
        -3.710586183390615e-05,
        -4.376143862182197e-06,
        7.241248287663791e-06,
        -1.0119940100181473e-06,
        -6.847079596993149e-07,
        2.633924226266962e-07,
        2.0143220235374613e-10,
        -1.814843248297622e-08,
        4.05612705554717e-09,
        -2.998836489615753e-10
    ]

    # high-pass
    reconstructionHighFilter = [
        -2.998836489615753e-10,
        -4.05612705554717e-09,
        -1.814843248297622e-08,
        -2.0143220235374613e-10,
        2.633924226266962e-07,
        6.847079596993149e-07,
        -1.0119940100181473e-06,
        -7.241248287663791e-06,
        -4.376143862182197e-06,
        3.710586183390615e-05,
        6.774280828373048e-05,
        -0.00010153288973669777,
        -0.0003851047486990061,
        5.349759844340453e-05,
        0.0013925596193045254,
        0.0008315621728772474,
        -0.003581494259744107,
        -0.00442054238676635,
        0.0067216273018096935,
        0.013810526137727442,
        -0.008789324924555765,
        -0.03229429953011916,
        0.0058746818113949465,
        0.061722899624668884,
        0.005632246857685454,
        -0.10229171917513397,
        -0.024716827337521424,
        0.1554587507060453,
        0.039850246458519104,
        -0.22829105082013823,
        -0.016727088308801888,
        0.3267868004335376,
        -0.13921208801128787,
        -0.36150229873889705,
        0.6104932389378558,
        -0.4726961853103315,
        0.21994211355113222,
        -0.06342378045900529,
        0.010549394624937735,
        -0.0007799536136659112
    ]