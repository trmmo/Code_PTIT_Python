# from pycallgraph2 import PyCallGraph
# from pycallgraph2 import Config
# from pycallgraph2 import GlobbingFilter
# from pycallgraph2.output import GraphvizOutput as GvO
#
#
# def call_graph_filtered(
#         function_,
#         output_png="call_graph_png",
#         custom_include=None
#     ):
#     """A call graph generator filtered"""
#     config = Config()
#     config.trace_filter = GlobbingFilter(
#         include=custom_include)
#     graphviz = GvO(output_file=output_png)
#
#     with PyCallGraph(output=graphviz, config=config):
#         function_()
#

nOT = int(input())


def encode_string(s):
    encoded_str = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded_str += str(count) + s[i - 1]
            count = 1
    encoded_str += str(count) + s[-1]
    return encoded_str


for i in range(nOT):
    s = str(input())
    print(encode_string(s))
    #
    # j = 0
    # res = ""
    # while j < len(s):
    #     k = j + 1
    #     cnt = 1
    #     if k <= len(s) - 1:
    #         while s[j] == s[k]:
    #             cnt += 1
    #             k += 1
    #             if k == len(s):
    #                 break
    #         res += str(cnt) + s[j]
    #         j = k
    #     elif s[len(s) - 1] != s[len(s) - 2]:
    #         res += "1" + s[len(s) - 1]
    #         j = k
    # print(res)
