"""
Link: https://www.youtube.com/watch?v=AFVN1As_tqc&embeds_referring_euri=https%3A%2F%2Fleetcode.com%2F&source_ve_path=MjM4NTE
Question: LC 71 Simplify Path, Variation
Ref: Meta
TC: O(n)
SC: O(n)
"""

PARENT_DIR = "PARENT_DIR"
CURRENT_DIR = "CURRENT_DIR"
ROOT_DIR = "ROOT_DIR"


class Solution:
    def simplify_path(self, cwd: str, cd: str):
        """
        cwd: absolute path
        cd: relative path
        returns: canoncial path. absolute path with no extraneous symbols.
        """
        if cd == "":
            cd = "."
        path_tree, cur_node = self._get_path_tree_from_path_str(cwd + "/")
        path_tree, cur_node = self._get_path_tree_from_path_str(
            cd + "/", cur_node, path_tree
        )
        return self._get_absolute_path_str(cur_node, path_tree)

    def _get_path_tree_from_path_str(
        self, path_str: str, cur_node=None, path_tree=None
    ):
        if not path_tree:
            path_tree = {ROOT_DIR: {"name": ROOT_DIR, "parent": None, "children": {}}}
        if not cur_node:
            cur_node = path_tree[ROOT_DIR]
        dir_name = ""
        i = 0
        while i < len(path_str):
            if path_str[i] not in "/.":
                dir_name += path_str[i]
                i += 1
                continue
            dot_ct, i = self._get_dot_ct(path_str, i)
            # If action is CURRENT_DIR, no change needed. Parent dir - go to parent of cur_node.
            if self._get_dot_action(dot_ct) == PARENT_DIR:
                cur_node = cur_node["parent"]
                dir_name = ""
                continue
            # If starting at 0, go to ROOT if there is a slash.
            if i == 0:
                if self._get_slash_ct(path_str, i)[1]:
                    cur_node = path_tree[ROOT_DIR]
            # If slash, then act on dir_name if present.
            slash_ct, i = self._get_slash_ct(path_str, i)
            if slash_ct and dir_name:
                child = cur_node["children"].get(dir_name, False)
                if not child:
                    cur_node["children"][dir_name] = {
                        "name": dir_name,
                        "parent": cur_node,
                        "children": {},
                    }
                cur_node = cur_node["children"][dir_name]
                dir_name = ""
                continue

        return path_tree, cur_node

    def _get_absolute_path_str(self, node: dict, path_tree: dict) -> str:
        res = []
        cur = node
        while cur["name"] != ROOT_DIR:
            res += [cur["name"]]
            cur = cur["parent"]
        return "/" + "/".join(res[::-1])

    def _get_dot_action(self, dot_ct: int):
        if dot_ct == 2:
            return PARENT_DIR
        return CURRENT_DIR

    def _get_dot_ct(self, path_str: str, i: int) -> tuple[int, int]:
        return self._get_ch_ct(path_str, i, ".")

    def _get_slash_ct(self, path_str: str, i: int) -> tuple[int, int]:
        return self._get_ch_ct(path_str, i, "/")

    def _get_ch_ct(self, path_str: str, i: int, ch: str) -> tuple[int, int]:
        ch_ct = 0
        j = i
        while j < len(path_str) and path_str[j] == ch:
            ch_ct += 1
            j += 1
        return ch_ct, j
