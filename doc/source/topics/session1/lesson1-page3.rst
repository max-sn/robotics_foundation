Degrees of freedom of a robot
=============================

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/zI64DyaRUvQ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

.. rubric:: Grübler's formula

.. math::
  
  \mathrm{dof} = m(N-1 - J) + \sum\limits_{i=1}^{J}f_i

Where :math:`m` is the number of degrees of freedom per body (6 for spatial bodies, 3 for planar bodies), :math:`N` is the number of bodies, including the ground, or base link, :math:`J` is the number of joints, and :math:`f_i` is the number of degrees of freedom of joint :math:`i`. The assumption for this formula to hold, is that all constraints should be independent, which is typically the case for serial links (or kinematics chains).

Typical types of joints are listed in the table below.

.. table::

  +-----------------+-------------+----------+
  | Joint           | Constraints | Freedoms |
  +=================+=============+==========+
  | Revolute (R)    | 5           | 1        |
  +-----------------+-------------+----------+
  | Prismatic (P)   | 5           | 1        |
  +-----------------+-------------+----------+
  | Universal (U)   | 4           | 2        |
  +-----------------+-------------+----------+
  | Spherical (S)   | 3           | 3        |
  +-----------------+-------------+----------+
  | Helical (H)     | 5           | 1        |
  +-----------------+-------------+----------+
  | Cylindrical (C) | 4           | 2        |
  +-----------------+-------------+----------+
