OK_FORMAT = True

test = {   'name': 'Task3',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> neighbors = np.array([[0.4, 0.3, 0.2, 0.1, 0.1]])\n'
                                               '>>> weights = 1 / np.array([[1.0, 1.0, 1.0, 3.0, 4.0]])\n'
                                               '>>> assert np.isclose(KNeighborsRegressor()._aggregate_uniform(neighbors), 0.22)\n'
                                               ">>> assert np.isclose(KNeighborsRegressor(weights='distance')._aggregate_weighted(neighbors, weights), 0.267, atol=0.001)\n",
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
