
class binary_tree:
	def __init__(self, root_key):
		self.root = root_key

class key:
	def __init__(self, key_value):
		self.value = key_value
		self.left_son = None
		self.right_son = None

	# def __init__(self, key_value, left_son_key):
	# 	self.value = key_value
	# 	self.left_son = left_son_key

	# def __init__(self, key_value, right_son_key):
	# 	self.value = key_value
	# 	self.right_son = right_son_key

	# def __init__(self,key_value,left_son_key,right_son_key):
	# 	self.value = key_value
	# 	self.left_son = left_son_key
	# 	self.right_son = right_son_key

	def add_son_left(self, left_son_key):
		self.left_son=key(left_son_key)

	def add_son_right(self, right_son_key):
		self.right_son=key(right_son_key)


def preorder_traverse(root):
	if root is not None:
		print root.value
		preorder_traverse(root.left_son)
		preorder_traverse(root.right_son)

def postorder_traverse(root):
	if root is not None:
		postorder_traverse(root.left_son)
		postorder_traverse(root.right_son)
		print root.value

def levelorder_traverse(root):
	if root is not None:
		print root.value
		if root.left_son is not None:
			# print root.left_son.value
			levelorder_traverse(root.left_son)
		if root.right_son is not None:
			# print root.right_son.value
			levelorder_traverse(root.right_son)

def inorder_traverse(root):
	if root is not None:
		inorder_traverse(root.left_son)
		print root.value
		inorder_traverse(root.right_son)




root = key('a')
root.add_son_left('b')
root.add_son_right('c')
root.left_son.add_son_left('d')
root.left_son.add_son_right('e')
root.right_son.add_son_left('f')
root.right_son.add_son_right('g')
print 'Preorder'
preorder_traverse(root)
print '\n'
print 'Postorder'
postorder_traverse(root)
print '\n'
print 'Levelorder'
levelorder_traverse(root)
print '\n'
print 'Inorder'
inorder_traverse(root)
print '\n'
print 