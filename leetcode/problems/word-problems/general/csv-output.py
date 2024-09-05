"""
TC: O(n) people
SC: O(n) people

[A]
1. Given a CSV containing data, then output the data in the corresponding format
Given a flat file CSV, which denotes an Organization Structure as so:
  employee_id, first_name, last_name, reports_to
  mfly, Marty, McFly, jblogs
  jblogs, Joe, Blogs, rboss
  nmuller, Nicolas, Muller, jblogs
  rboss, Robert, Boss,
  trice, Travis, Rice, rboss
Print out the organization structure:
1. Robert Boss (rboss)
  2. Joe Blogs (jblogs)
    3. Nicolas Muller (nmuller)
    3. Marty McFly (mfly)
  2. Travice Rice (trice)
"""

import unittest


def csv_to_org_chart_output(csv: str):
    res = ""
    org_tree = {}
    employee_dic = {}
    # find sources (top bosses) and apply, add rest to employee_dic.
    for i, line in enumerate(csv.split("\n")):
        if line.find("employee_id") != -1 or line.find(",") == -1:
            continue
        split = line.split(",")
        if len(split) != 4:
            continue
        employee_id, first_name, last_name, reports_to = split
        employee_id, first_name, last_name, reports_to = (
            employee_id.strip(),
            first_name.strip(),
            last_name.strip(),
            reports_to.strip(),
        )
        employee_dic[employee_id] = employee_dic.get(
            employee_id,
            {
                "first_name": first_name,
                "last_name": last_name,
                "reports_to": reports_to if reports_to else False,
                "manages": [],
            },
        )
        if not reports_to:
            # top level boss.
            org_tree[employee_id] = org_tree.get(employee_id, [])
    # apply reports_to
    for employee_id in employee_dic:
        employee_details = employee_dic[employee_id]
        reports_to = employee_details["reports_to"]
        if not reports_to:
            continue
        employee_dic[reports_to]["manages"].append(employee_id)
    # traverse tree
    que = [(employee_id, 0) for employee_id in org_tree]

    print("org_tree", org_tree)
    while que:
        employee_id, level = que.pop()
        employee_details = employee_dic[employee_id]
        first_name = employee_details["first_name"]
        last_name = employee_details["last_name"]
        res += f"{level * '  '}{level + 1}. {first_name} {last_name} ({employee_id})\n"
        for child in employee_details["manages"]:
            que.append((child, level + 1))
    res = res.strip()
    return res


class TestCSVOutput(unittest.TestCase):
    def test_csv_example_1(self):
        csv = """
        employee_id, first_name, last_name, reports_to
        mfly, Marty, McFly, jblogs
        jblogs, Joe, Blogs, rboss
        nmuller, Nicolas, Muller, jblogs
        rboss, Robert, Boss,
        trice, Travis, Rice, rboss
        """
        expected = """1. Robert Boss (rboss)
  2. Travis Rice (trice)
  2. Joe Blogs (jblogs)
    3. Nicolas Muller (nmuller)
    3. Marty McFly (mfly)"""
        actual = csv_to_org_chart_output(csv)
        print("expected:\n", expected, "actual:\n", actual)
        self.assertEqual(expected, actual)


unittest.main()
