'''
Compare two version numbers version1 and version2.
If version1 > version2 return 1; if version1 < version2
return -1;otherwise return 0.

You may assume that the version strings are non-empty
and contain only digits and the . character.

The . character does not represent a decimal point and
is used to separate number sequences.

For instance, 2.5 is not "two and a half" or "half way
to version three", it is the fifth second-level revision
of the second first-level revision.

You may assume the default revision number for each level
of a version number to be 0. For example, version number
3.4 has a revision number of 3 and 4 for its first and
second level revision number. Its third and fourth level
revision number are both 0.
'''


class Solution:
    def compareVersion(self, v1: str, v2: str) -> int:
        v1 = [int(x) for x in v1.split(".")]
        v2 = [int(x) for x in v2.split(".")]
        if len(v1) > len(v2):
            for y in range(len(v2), len(v1)):
                v2.append(0)
        elif len(v2) > len(v1):
            for y in range(len(v1), len(v2)):
                v1.append(0)
        for x in range(len(v1)):
            if v1[x] > v2[x]:
                return 1
            if v1[x] < v2[x]:
                return -1
        return 0