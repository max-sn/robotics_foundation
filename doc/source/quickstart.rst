Quickstart
==========

First clone the latest version of the repository to a location on your PC.

.. code-block:: bash

  cd {location}
  git clone https://github.com/max-sn/robotics_foundation.git

The scripts are bundled in packages, one for |matlab| (``MR``) and one for |python| (``modern_robotics``). The quickest way to be able to find the functions is to include the packages in the search path of your preferred scripting language. Use the location that you cloned the git repository to for ``{location}``.

.. tab-set::

  .. tab-item:: Python
    :sync: PYTHON

    .. code-block:: python

      >>> import sys
      >>> sys.path.append('{location}/robotics_foundation/python')

  .. tab-item:: Matlab
    :sync: MATLAB

    .. code-block:: matlab
      
      >> addpath('{location}/robotics_foundation/matlab')

Note that these commands will only keep the directory on the search path for the current session. For |python| that means until you close the shell (with ``exit()`` or :kbd:`Ctrl-z`), and for |matlab| that means until you restart the GUI.

Using them can be done as follows.

.. tab-set::
  
  .. tab-item:: Python
    :sync: PYTHON

    .. tab-set:: 

      .. tab-item:: Symbolic
        :sync: PYTHON-SYM

        .. code-block:: python

          >>> import sympy as sp
          >>> import modern_robotics.sym as mr
          >>> v = sp.Matrix([1, 2, 3])
          >>> mr.vec_to_so3(v)
          Matrix([
          [ 0, -3,  2],
          [ 3,  0, -1],
          [-2,  1,  0]])

      .. tab-item:: Numeric
        :sync: PYTHON-NUM

        .. code-block:: python

          >>> import numpy as np
          >>> import modern_robotics as mr
          >>> v = np.array([[1], [2], [3]])
          >>> mr.vec_to_so3(v)
          array([[ 0, -3,  2],
                [ 3,  0, -1],
                [-2,  1,  0]])

  .. tab-item:: Matlab
    :sync: MATLAB
    
    .. code-block:: matlab

      >> v = [1; 2; 3];
      >> MR.vec_to_little_so3(v)

      ans =

          0    -3     2
          3     0    -1
          -2     1     0

