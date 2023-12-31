from searches import *

tests = {
    "Depth 02":  {
        "Inicial": '1 2 3 4 5 6 7 8 9 10 0 11 13 14 15 12'
        ,"Final": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0"}
    ,"Depth 03": {
        "Inicial": '1 2 3 4 5 6 0 7 9 10 11 8 13 14 15 12'
        ,"Final": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0"}
    ,"Depth 04": {
        "Inicial": '1 2 3 4 5 0 7 8 9 6 10 12 13 14 11 15'
        ,"Final": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0"}
    ,"Depth 05": {
        "Inicial": '1 2 3 0 5 6 8 4 9 10 7 12 13 14 11 15'
        ,"Final": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0"}
    ,"Depth 06": {
        "Inicial": '1 2 3 4 5 0 6 8 9 11 7 12 13 10 14 15'
        ,"Final": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0"}
    ,"Depth 07": {
        "Inicial": '1 2 3 4 5 10 6 7 9 0 12 8 13 14 11 15'
        ,"Final": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0"}
    ,"Depth 08": {
        "Inicial": '6 12 0 9 14 2 5 11 7 8 4 13 3 10 1 15'
        ,"Final": "14 6 12 9 7 2 5 11 8 4 13 15 3 10 1 0"}
    ,"Depth 09": {
        "Inicial": '1 0 3 4 6 2 7 8 5 14 10 12 9 13 11 15'
        ,"Final": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0"}
    ,"Depth 10": {
        "Inicial": '1 6 2 4 5 10 3 8 13 9 7 11 14 0 15 12'
        ,"Final": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0"}
    ,"Depth 12": {
        "Inicial": '1 2 3 4 5 6 8 12 13 9 0 7 14 11 10 15'
        ,"Final": "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 0"}
    ,"Depth 13": {
        "Inicial": '9 12 0 7 14 5 13 2 6 1 4 8 10 15 3 11'
        ,"Final": "9 5 12 7 14 13 0 8 1 3 2 4 6 10 15 11"}
}

for depth in tests.keys():
    test = [tests[depth]['Inicial'], tests[depth]['Final']]
    print(f'\n{"=":=^50s}\n\n{depth:^50s}\n\n{"=":=^50s}')
    print('    Algorithm bfs: ', bfs(*test))
    print('    Algorithm depthfirst: ', depthfirst(*test, max_depth=20, max_seconds=10000))
    print('    Algorithm depth_firsti: ', depth_firsti(*test))
    print('    Algorithm greedy_h1: ', greedy_h1(*test))
    print('    Algorithm greedy_h2: ', greedy_h2(*test))
    print('    Algorithm Astar_h1: ', Astar_h1(*test))
    print('    Algorithm Astar_h2: ', Astar_h2(*test))

