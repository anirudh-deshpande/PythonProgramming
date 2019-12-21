# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # (TF?, AT/BT, distanceTarget)
    #     def distanceKHelper(self, tup):

    #         if tup[0] is False:      # Target not yet found
    #             if target == tup[3]: # current node is the target
    #                 tupLeft = self.distanceKHelper((True, 'BT', tup[2] + 1, tup[3].left, tup[4], tup[5], tup[6]))
    #                 tupRight = self.distanceKHelper((True, 'BT', tup[2] + 1, tup[3].right, tup[4], tup[5], tup[6]))
    #                 return (True, 'AT', tup[2] + 1, tup[4], tup[5], tup[6])
    #             else:
    #                 tupLeft = self.distanceKHelper((False, None, 0, tup[3].left, tup[4], tup[5], tup[6]))
    #                 # Target found here?
    #                 if tupLeft[0] == True and tupLeft[1] == 'AT':
    #                     self.distanceKHelper((True, None, K - tupLeft[2], tupLeft[3].right, tupLeft[4], tupLeft[5], tupLeft[6]))
    #                     return (True, 'AT', tupLeft[2] + 1, tupLeft[4], tupLeft[5], tupLeft[6])

    #                 tupRight = self.distanceKHelper((False, None, 0, tup[3].right, tup[4], tup[5], tup[6]))
    #                 # Target found here?
    #                 if tupRight[0] == True and tupRight[1] == 'AT':
    #                     self.distanceKHelper((True, None, K - tupRight[2], tupRight[3].left, tupRight[4], tupRight[5], tupRight[6]))
    #                     return (True, 'AT', tupRight[2] + 1, tupRight[4], tupRight[5], tupRight[6])

    #         if tup[0] == True and tup[1] == 'BT':
    #             if tup[2] == K:
    #                 tup[6].append(tup[3])
    #                 return () # What should I return here?

    #         if tup[0] == True and tup[1] == 'AT':
    #             if tup[2] == K:

    def inOrderTraversal(self, root):
        if root != None:
            print root.val
            self.inOrderTraversal(root.left)
            self.inOrderTraversal(root.right)


            # (T/F, distance)
            #     def cloneTree(self, node, target, K, is_target_found, disntance_target):
            #         if node == target:
            #             disntance_target = 0
            #             is_target_found = True

            #         new_node = TreeNode(disntance_target)

            #         if is_target_found:
            #             disntance_target += 1

            #         if node.left != None:
            #             tupLeft = self.cloneTree(node.left, target, K, is_target_found, disntance_target)
            #             if tupLeft[0]:
            #                 new_node.left = tupLeft[1]
            #                 new_node.val = tupLeft[2]
            #                 tupRight = self.cloneTree(node.right, target, K, True, disntance_target)
            #                 new_node.right = tupRight[1]
            #                 return (True, new_node, disntance_target + 1)
            #             else:
            #                 new_node.left = tupLeft[1]

            #         if node.right != None:
            #             tupRight = self.cloneTree(node.right, target, K, is_target_found, disntance_target)
            #             if tupRight[0]:
            #                 new_node.right = tupRight[1]
            #                 new_node.data = tupRight[2]
            #                 tupLeft = self.cloneTree(node.left, target, K, True, disntance_target)
            #                 new_node.left = tupLeft[1]
            #                 return (True, new_node, disntance_target + 1)
            #             else:
            #                 new_node.right = tupRight[1]

            #         return (is_target_found, new_node, disntance_target)

    def cloneTree(self, root, distance, target, target_found):

        if root == target:
            distance = 0
            target_found = True

        new_node = TreeNode(distance)

        if target_found:
            distance += 1

        if root.left is not None:
            tupLeft = self.cloneTree(root.left, distance, target, target_found)
            new_node.left = tupLeft[0]
            if new_node.val == -1 and tupLeft[1] > 0:
                new_node.val = tupLeft[1]
                distance = tupLeft[1]

        if root.right is not None:
            tupRight = self.cloneTree(root.right, distance, target, target_found)
            new_node.right = tupRight[0]
            if new_node.val == -1 and tupRight[1] > 0:
                new_node.val = tupRight[1]

        return (new_node, distance)

    def subTreeAdd(self, node, curDistance, K, ans):
        if node is None:
            return;
        if curDistance == K:
            ans.append(node.val)

        self.subTreeAdd(node.left, curDistance + 1, K, ans)
        self.subTreeAdd(node.right, curDistance + 1, K, ans)

    def distanceKHelper(self, node, target, K, ans):
        if node == None:
            return -1

        if node == target:
            self.subTreeAdd(node, 0, K, ans)
            return 1

        L = self.distanceKHelper(node.left, target, K, ans)

        if L != -1:
            if L == K:
                ans.append(node)
                return -1
            else:
                self.subTreeAdd(node.right, L + 1, K, ans)
                return L + 1

        R = self.distanceKHelper(node.right, target, K, ans)

        if R != -1:
            if R == K:
                ans.append(node)
                return -1
            else:
                self.subTreeAdd(node.left, R + 1, K, ans)
                return R + 1

        return -1

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        # up = self.cloneTree(root, -1, target, False)
        # self.inOrderTraversal(tup[0])

        ans = []
        self.distanceKHelper(root, target, K, ans)
        return ans

        # self.distanceKHelper((False, None, 0, root, target, K, result))
