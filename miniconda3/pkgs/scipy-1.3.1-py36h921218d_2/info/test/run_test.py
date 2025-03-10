#  tests for scipy-1.3.1-py36h921218d_2 (this is a generated file);
print('===== testing package: scipy-1.3.1-py36h921218d_2 =====');
print('running run_test.py');
#  --- run_test.py (begin) ---
import sys
import os

# Use OpenBLAS with 1 thread only as it seems to be using too many
# on the CIs apparently.
os.environ["OPENBLAS_NUM_THREADS"] = "1"

import scipy
import scipy.cluster._hierarchy
import scipy.cluster._vq
import scipy.fftpack._fftpack
import scipy.fftpack.convolve
import scipy.integrate._dop
import scipy.integrate._odepack
import scipy.integrate._quadpack
import scipy.integrate._test_multivariate
import scipy.integrate._test_odeint_banded
import scipy.integrate.lsoda
import scipy.integrate.vode
import scipy.interpolate._fitpack
import scipy.interpolate._ppoly
import scipy.interpolate.dfitpack
import scipy.interpolate.interpnd
import scipy.io.matlab.mio5_utils
import scipy.io.matlab.mio_utils
import scipy.io.matlab.streams
import scipy.linalg._decomp_update
import scipy.linalg._fblas
import scipy.linalg._flapack
import scipy.linalg._flinalg
import scipy.linalg._interpolative
import scipy.linalg._solve_toeplitz
import scipy.linalg.cython_blas
import scipy.linalg.cython_lapack
import scipy.ndimage._nd_image
import scipy.ndimage._ni_label
import scipy.odr.__odrpack
import scipy.optimize._cobyla
import scipy.optimize._group_columns
import scipy.optimize._lbfgsb
import scipy.optimize._lsq.givens_elimination
import scipy.optimize._minpack
import scipy.optimize._nnls
import scipy.optimize._slsqp
import scipy.optimize._zeros
import scipy.optimize.minpack2
import scipy.optimize.moduleTNC
import scipy.signal._max_len_seq_inner
import scipy.signal._spectral
import scipy.signal.sigtools
import scipy.signal.spline
import scipy.sparse._csparsetools
import scipy.sparse._sparsetools
import scipy.sparse.csgraph._min_spanning_tree
import scipy.sparse.csgraph._reordering
import scipy.sparse.csgraph._shortest_path
import scipy.sparse.csgraph._tools
import scipy.sparse.csgraph._traversal
import scipy.sparse.linalg.dsolve._superlu
import scipy.sparse.linalg.eigen.arpack._arpack
import scipy.sparse.linalg.isolve._iterative
import scipy.spatial._distance_wrap
import scipy.spatial.ckdtree
import scipy.spatial.qhull
import scipy.special._ellip_harm_2
import scipy.special._ufuncs
import scipy.special._ufuncs_cxx
import scipy.special.specfun
import scipy.stats.mvn
import scipy.stats.statlib

import scipy.stats
import scipy.special


sys.exit(not scipy.test(verbose=2))
#  --- run_test.py (end) ---

print('===== scipy-1.3.1-py36h921218d_2 OK =====');
