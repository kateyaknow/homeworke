OK_FORMAT = True

test = {   'name': 'Task1',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> XA = np.array([[3.6, 4.7, 4.3], [4.9, 3.5, 3.6]])\n'
                                               '>>> XB = np.array([[0.8, 2.7, 1.2], [2.6, 1.2, 4.5], [0.8, 4.9, 1.8]])\n'
                                               '>>> D = cdist(XA, XB)\n'
                                               '>>> assert D.shape == (2, 3)\n'
                                               '>>> assert np.allclose(cdist(XA, XB), np.array([[4.631, 3.646, 3.759], [4.818, 3.375, 4.691]]), atol=0.001)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
