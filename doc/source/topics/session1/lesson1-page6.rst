Task space and workspace
========================

.. raw:: html 

  <iframe style="width: 695px; height: 390px;" src="https://www.youtube-nocookie.com/embed/hTuW51CpUg4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


Task space
----------

For determining the task space, only the task has to be known. No knowledge of the robot is yet required. You can choose the task space as the minimal space in which the complete task can be described, but similar to the configuration space, you can also choose to use an implicit representation with more parameters if that is more convenient. Take for example the task of a train. The train moves on a track and the minimum representation of its location on the track is a single number describing how far the train has travelled since a certain reference. However, often we would like to know the location of the train in GPS coordinates, preferably projected on a map. That is an implicit representation.


Workspace
---------

The workspace of a robot is the subspace of the Euclidean space in which the part of the robot that is meant to do a task, can reach every location. If the orienation of that part, often called the end-effector, is also considered, it is often called the *dexterous workspace* and is no longer a subset of the Euclidean space alone.