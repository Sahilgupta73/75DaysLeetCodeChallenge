# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution {
#     unordered_map<TreeNode*,int> height;
#     unordered_map<int,int> answer;
# public:
#     vector<int> treeQueries(TreeNode* root, vector<int>& queries) {
#         dfs(root);
#         dfs(root,-1,0);
#         vector<int> ans;
#         // for  (auto it : height) {
#         //     cout << it.first->val << " " << it.second << endl;
#         // }
#         for (int x : queries) {
#             ans.push_back(answer[x]);
#         }
#         return ans;
#     }
#     void dfs(TreeNode* root,int k,int maxi) {
#         if (root == nullptr) return;
#         int l = (root->left != nullptr) ? height[root->left] : 0;
#         int r = (root->right != nullptr) ? height[root->right] : 0;
#         answer[root->val] = maxi;
#         if (root->left != nullptr) {
#             int nH = r + k + 1;
#             dfs(root->left,k+1,max(maxi,nH));
#         } 
#         if (root->right != nullptr) {
#             int nH = l + k + 1;
#             dfs(root->right,k+1,max(maxi,nH));
#         }
#     }
#     int dfs(TreeNode* root) {
#         if (root == nullptr) return 0;
#         int l = dfs(root->left);
#         int r = dfs(root->right);
#         height[root] = max(l,r)+1;
#         return height[root];
#     }
# };
# class Solution:
#     def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
#         def dfs(root: Optional[TreeNode]) -> int:
#             if root is None:
#                 return 0
#             if root.left is None and root.right is None:
#                 return 1
#             l = dfs(root.left)
#             r = dfs(root.right)
#             height[root] = max(l,r)+1
#             return height[root]



class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        self.height = {}
        self.answer = {}

        self.findHeight(root)
        self.dfs(root, -1, 0)

        ans = []
        for x in queries:
            ans.append(self.answer[x])

        return ans

    def findHeight(self, root):
        if root is None:
            return 0

        left = self.findHeight(root.left)
        right = self.findHeight(root.right)

        self.height[root] = max(left, right) + 1
        return self.height[root]

    def dfs(self, root, k, maxi):
        if root is None:
            return

        left_height = self.height[root.left] if root.left else 0
        right_height = self.height[root.right] if root.right else 0

        self.answer[root.val] = maxi

        if root.left:
            new_height = right_height + k + 1
            self.dfs(root.left, k + 1, max(maxi, new_height))

        if root.right:
            new_height = left_height + k + 1
            self.dfs(root.right, k + 1, max(maxi, new_height))
        