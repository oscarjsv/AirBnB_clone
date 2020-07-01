#!/usr/bin/python3
""""Module helper"""


class Utils:
    """Toolbox for parsing"""

    @staticmethod
    def split_action(line):
        """Converts a string into a tuple of arguments"""
        argumemts = []

        argumemts.append(line[0].split('.')[0])
        tmp = line[0].split('.')[1]
        tmp = tmp.split('(')

        if tmp[len(tmp) - 1] == ')':
            del tmp[len(tmp) - 1]

        action = tmp[0]
        if len(tmp) == 1:
            return action, tuple(argumemts)

        argumemts.append(tmp[1].strip('",)'))
        line = line[1:]
        for e in line:
            aux = e.strip('",)')
            argumemts.append(aux)

        return action, tuple(argumemts)
