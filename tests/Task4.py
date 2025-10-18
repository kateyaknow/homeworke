OK_FORMAT = True

test = {   'name': 'Task4',
    'points': 2,
    'suites': [   {   'cases': [   {   'code': '>>> y_true = np.array([0.7, -1.5, 1.4, -1.1])\n'
                                               '>>> y_pred = np.array([1.0, 1.7, -1.6, 0.2])\n'
                                               '>>> assert np.isclose(root_mean_squared_error(y_true, y_pred), 2.292, atol=0.001)\n'
                                               '>>> assert np.isclose(root_mean_squared_error(y_true, y_true), 0.0)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
