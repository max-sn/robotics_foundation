Configuration space representation
==================================

.. raw:: html

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/PPgJPjCUIXU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

For 'flat' spaces, e.g. lines, planes, or more familiar our own 3D Euclidean space, the velocity of a position, is simply its time-derivative. For curved spaces, that is not the case. For curved spaces, we can choose two methods to describe positions in the space:

* implicit parameterization, which uses the minimal amount of parameters necessary to describe a position, but might be subject to discontinuities and infinite values in configuration singularities; or
* explicit representation, where we embed the space in a Euclidean space with more coordinates, which are subject to constraints (such as the constant radius constraint :math:`x^2+y^2+z^2=1` for a sphere), but give us a smooth and continuous representation.

One important explicit representation we use in this course is the rotation matrix, which is a singularity free representation of the curved space of rigid body orientations. It consists of 9 variables, where any implicit parameterization only uses three variables, but the latter is susceptible to representation singularities, e.g. `Gimbal Lock <https://en.wikipedia.org/wiki/Gimbal_lock>`__.

An alternative explicit representation for rigid body orientations is the `unit quaternion <https://en.wikipedia.org/wiki/Versor>`__ or *versor*, which only uses four variables, but is less intuitive to use and will not be treated in this course.