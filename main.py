import builder

def main():
    
    #default_maze = builder.build_maze(250, 150, 5, 5, 50, 50, None, seed=1142)
    params = builder.get_maze_parameters()
    print(f"tuple {params}, params[0] {params[0]}, params[1] {params[1]}, params[2] {params[2]}, params[3] {params[3]}, params[4] {params[4]}")
    builder.build_maze(None, None, params[0], params[1], params[2], params[3], None, params[4])

main()
