OK_FORMAT = True

test = {   'name': 'Task3',
    'points': 3,
    'suites': [   {   'cases': [   {   'code': '>>> clf = DecisionTreeClassifier()\n'
                                               '>>> node = Node()\n'
                                               '>>> clf._make_leaf(node, np.array([4, 2, 2, 2, 3, 1, 0, 0]))\n'
                                               '>>> assert node.value == 2\n'
                                               '>>> assert np.isclose(clf._impurity(np.array([1, 1, 1, 1])), 0.0)\n'
                                               '>>> assert np.isclose(clf._impurity(np.array([0, 0, 1, 1])), 0.5)\n'
                                               '>>> assert accuracy_score(y_test, y_pred) > 0.9\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
