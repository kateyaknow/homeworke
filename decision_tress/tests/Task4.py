OK_FORMAT = True

test = {   'name': 'Task4',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> reg = DecisionTreeRegressor()\n'
                                               '>>> node = Node()\n'
                                               '>>> reg._make_leaf(node, np.array([1.0, 2.0, 3.0, 4.0, 5.0]))\n'
                                               '>>> assert np.isclose(node.value, 3.0)\n'
                                               '>>> assert np.isclose(reg._impurity(np.array([1.0, 1.0, 1.0, 1.0])), 0.0)\n'
                                               '>>> assert np.isclose(reg._impurity(np.array([1.0, 2.0, 3.0, 4.0, 5.0])), 2.0, atol=0.001)\n'
                                               '>>> assert mean_absolute_error(y_test, y_pred) < 0.25\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
