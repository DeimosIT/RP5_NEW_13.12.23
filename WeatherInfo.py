import time
import PR5
import threading

dfs_rp5 = []
list_city_name_rp5 = []

def create_rp5():
    global dfs_rp5
    global list_city_name_rp5
    dfs_rp5, list_city_name_rp5 = PR5.main()

def main():
    global dfs_rp5
    global list_city_name_rp5
    t = time.time()
    create_rp5()
    PR5.create_xlsx(dfs_rp5, list_city_name_rp5)
    print('time: ', time.time() - t)

if __name__ == '__main__':
    main()