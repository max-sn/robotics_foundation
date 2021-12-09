Degrees of freedom of a rigid body
==================================

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/z29hYlagOYM" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The position of all points of a rigid body are known or can be determined, if we know the location and orientation of the rigid body itself. Therefore, the configuration of a single rigid body is defined with six degrees of freedom (DoFs).

.. table::
  :widths: 20 20 5 30 5 20

  +--------+--------+-----------+-------------+-----------+---------------+
  | point  | coords |           | independent |           | real freedoms |
  |        |        |           | constraints |           |               |
  +========+========+===========+=============+===========+===============+
  | A      | 3      | :math:`-` | 0           | :math:`=` | 3             |
  +--------+--------+-----------+-------------+-----------+---------------+
  | B      | 3      | :math:`-` | 1           | :math:`=` | 2             |
  +--------+--------+-----------+-------------+-----------+---------------+
  | C      | 3      | :math:`-` | 2           | :math:`=` | 1             |
  +--------+--------+-----------+-------------+-----------+---------------+
  | D, etc.| 3      | :math:`-` | 3           | :math:`=` | 0             |
  +--------+--------+-----------+-------------+-----------+---------------+
  | total  |        |           |             |           | 6             |
  +--------+--------+-----------+-------------+-----------+---------------+
