import csv
from python_scripts.create_specifications import vnnlib_template_2

# create VNN-LIB 2.0 files given the following:
EPS = 0.05              # size of the input pertubation
VNN_COMP_TIMEOUT = 100  # per-instance verification timeout
ONNX_MODEL_PATH = "onnx/ACASXU_run2a_1_1_batch_2000.onnx"
PRUNED_ONNX_MODEL_PATH = "onnx/ACASXU_run2a_1_1_batch_2000_pruned10.onnx"

instance_data = []

lines = vnnlib_template_2(EPS)

vnnlib_filename = "./vnnlib/instance_1.vnnlib2"
with open(vnnlib_filename, "w") as f:
    f.writelines(line + "\n" for line in lines)

instance = [[("f", ONNX_MODEL_PATH),("g", PRUNED_ONNX_MODEL_PATH)], vnnlib_filename, VNN_COMP_TIMEOUT]
instance_data.append(instance)

# save the ONNX/VNN-LIB instance pairs in the required CSV
with open(f"instances.csv", 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(instance_data)