import sys
import os

def main():
    global arcpy

    if len(sys.argv) !=4:
        print('Usage:  data_prep.py <in_gdbs_base_folder> <out_gdb> <out_feature_dataset>')
        sys.exit()

    in_gdbs_base_folder = sys.argv[1]
    out_gdb = sys.argv[2]
    out_feature_dataset = sys.argv[3]

    if not os.path.exists(in_gdbs_base_folder):
        print(f'{in_gdbs_base_folder} folder does not exist')
        sys.exit()
    if not os.path.exists(out_feature_dataset):
        print(f'{out_feature_dataset} feature dataset does not exist')
        sys.exit()
    
    import arcpy

    gdbs_to_fds(in_gdbs_base_folder, out_gdb, out_feature_dataset)    


def gdbs_to_fds(in_gdbs_base_folder, out_gdb, out_feature_dataset):
    arcpy.env.workspace = out_gdb
    arcpy.env.overwriteOutput = True
    os.path.dirname






if __name__ == '__main__':
    main()