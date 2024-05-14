from .integer_lattice import IntegerLattice

def Cycle(num_vert, multiedges=None, weights=None):
    r"""
    Cycle graph constructor.

    A cycle graph is a graph that forms a single closed loop, 
    where each vertex is connected to exactly two other vertices, 
    forming a circular structure.

    Parameters
    ----------
    num_vert : int
        The number of vertices in the cycle. 
    multiedges : scipy.sparse.csr_array, optional
        Specifies the number of multiple edges between the same 
        pair of vertices. 
        Defaults to None.
    weights : scipy.sparse.csr_array, optional
        Assigns weights to the edges of the graph. 
        Defaults to None.

    Returns
    -------
    :class:`hiperwalk.Graph`
        Returns an instance of a cycle graph. 
        Refer to :ref:`graph_constructors` for more details.

    See Also
    --------
    :ref:`graph_constructors`
        Further information on graph constructors.

    Notes
    -----
    The cycle is conceptually embedded on a line with cyclic 
    boundary conditions. The **order of neighbors** for any 
    vertex :math:`v` is :math:`[v + 1, v - 1]`, where the right 
    neighbor is listed first, followed by the left neighbor.

    .. testsetup::

        import hiperwalk as hpw

    .. doctest::

        >>> g = hpw.Cycle(10)
        >>> g.neighbors(0)
        array([1, 9])
        >>> g.neighbors(1)
        array([2, 0])
        >>> g.neighbors(8)
        array([9, 7])
        >>> g.neighbors(9)
        array([0, 8])
    """
    basis = [1, -1]
    g = IntegerLattice(num_vert, basis, True, weights, multiedges)
    return g
