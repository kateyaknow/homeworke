OK_FORMAT = True

test = {   'name': 'Task2',
    'points': 5,
    'suites': [   {   'cases': [   {   'code': '>>> class TestDecisionTreeModel(DecisionTreeModel):\n'
                                               '...     """Решающее дерево для тестирования базового класса."""\n'
                                               '...     def _make_leaf(self, node, y):\n'
                                               '...         node.value = int(y.min())\n'
                                               '...     def _impurity(self, y):\n'
                                               '...         return float(len(y))\n'
                                               '>>> X = np.array([[0.1, 0.1], [0.2, 0.9], [0.3, 0.2], [0.4, 0.8], [0.6, 0.2], [0.7, 0.7], [0.8, 0.3], [0.9, 0.9]], dtype=float)\n'
                                               '>>> y = np.array([0, 0, 0, 0, 1, 1, 1, 1], dtype=int)\n'
                                               '>>> model = TestDecisionTreeModel(max_depth=2, min_leaf_size=1).fit(X, y)\n'
                                               '>>> root = model.root\n'
                                               '>>> assert root.feature is not None and root.threshold is not None\n'
                                               '>>> assert root.lchild is not None and root.rchild is not None\n',
                                       'hidden': False,
                                       'locked': False},
                                   {   'code': '>>> class TestDecisionTreeModel(DecisionTreeModel):\n'
                                               '...     """Решающее дерево для тестирования базового класса."""\n'
                                               '...     def _make_leaf(self, node, y):\n'
                                               '...         node.value = int(y.min())\n'
                                               '...     def _impurity(self, y):\n'
                                               '...         return float(len(y))\n'
                                               '>>> X = np.array([[0.1, 0.1], [0.2, 0.9], [0.3, 0.2], [0.4, 0.8], [0.6, 0.2], [0.7, 0.7], [0.8, 0.3], [0.9, 0.9]])\n'
                                               '>>> y = np.array([0, 0, 0, 0, 1, 1, 1, 1])\n'
                                               '>>> model = TestDecisionTreeModel().fit(X, y)\n'
                                               '>>> root = model.root\n'
                                               '>>> assert root.feature is not None and root.threshold is not None\n'
                                               '>>> assert root.lchild is not None and root.rchild is not None\n'
                                               '>>> assert root.lchild.lchild is None and root.lchild.rchild is None\n'
                                               '>>> assert root.rchild.lchild is None and root.rchild.rchild is None\n'
                                               '>>> assert model._predict_node(root, np.array([0.2, 0.5])) == 0\n'
                                               '>>> assert model._predict_node(root, np.array([0.8, 0.5])) == 1\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
