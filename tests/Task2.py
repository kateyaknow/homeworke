OK_FORMAT = True

test = {   'name': 'Task2',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> reg = KNeighborsModel(n_neighbors=1).fit(np.array([[0.3], [0.4], [0.0]]), np.array([1, 1, 0]))\n'
                                               '>>> neighbors, distances = reg._find_neighbors(np.array([[0.1]]))\n'
                                               '>>> assert neighbors.item() == 0\n'
                                               '>>> assert np.isclose(distances.item(), 0.1)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
