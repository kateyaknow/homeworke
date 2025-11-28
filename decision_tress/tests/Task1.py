OK_FORMAT = True

test = {   'name': 'Task1',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> assert np.isclose(gini(np.array([0.5, 0.5])), 0.5)\n'
                                               '>>> assert np.isclose(entropy(np.array([0.5, 0.5])), 1.0, atol=0.001)\n'
                                               '>>> assert np.isclose(gini(np.array([0.1, 0.2, 0.3, 0.4])), 0.7)\n'
                                               '>>> assert np.isclose(entropy(np.array([0.1, 0.2, 0.3, 0.4])), 1.846, atol=0.001)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
