import os


# user
USER = 1  # 1: Moonjung, 2: Haesung
# work station server
SERVER = 0  # 0, 5, 6, 7, 8, 9, 10, 32, 33

TR_NUM_WORKERS = 5 if SERVER > 0 else 0
VA_NUM_WORKERS = 5 if SERVER > 0 else 0

# root directory
ROOT_DIR = "/data4"
if SERVER == 0:
    ROOT_DIR = "C:\\Users\\Jay\\data_files"
if SERVER == 5:
    ROOT_DIR = "/data3"
if SERVER == 6:
    ROOT_DIR = "/data2"
if SERVER == 7:
    ROOT_DIR = "/data4"
if SERVER == 8:
    ROOT_DIR = "/data4"
if SERVER == 9:
    # ROOT_DIR = "/home/jjamjung/my_data"
    ROOT_DIR = "/data4"
if SERVER == 10:
    ROOT_DIR = "/data2"
if SERVER == 32:
    ROOT_DIR = "/home/student/my_data"
if SERVER == 33:
    ROOT_DIR = "/home/student/my_data"

# home directory
HOME_DIR = os.path.join(ROOT_DIR, "BioSignals")
# result directory
if USER == 1:
    BASE_DIR = HOME_DIR
elif USER == 2:
    BASE_DIR = "/home/seastar87/BioSignals"

DATASET_DIR = os.path.join(BASE_DIR, "datasets")
if not os.path.exists(DATASET_DIR):
    os.mkdir(DATASET_DIR)
RESULT_DIR = os.path.join(BASE_DIR, "results")
if not os.path.exists(RESULT_DIR):
    os.mkdir(RESULT_DIR)

SLEEP_EDF = "SleepEDF"
CHAPMAN = "Chapman"
CPSC = "CPSC"
PTBXL = "PTBXL"
GEORGIA = "Georgia"
AVAILABLE_DATASET_NAMES = {SLEEP_EDF, CHAPMAN, CPSC, PTBXL, GEORGIA}
AVAILABLE_LEARNING_MODES = ("Supervised", "SelfSupervised", "TrainLinear", "FineTune")
AVAILABLE_METHODS = ("Default", "AttnSleep", "TS-TCC")
AVAILABLE_MODELS = ("DefaultTF", "AttnSleep", "TS-TCC")


def get_base_dataset_dir(dataset_name):
    assert dataset_name in AVAILABLE_DATASET_NAMES
    target_dataset_dir = os.path.join(DATASET_DIR, dataset_name)
    if not os.path.exists(target_dataset_dir):
        os.mkdir(target_dataset_dir)
    return target_dataset_dir


def get_raw_dataset_dir(dataset_name):
    assert dataset_name in AVAILABLE_DATASET_NAMES
    target_dataset_dir = os.path.join(DATASET_DIR, dataset_name)
    raw_data_dir = os.path.join(target_dataset_dir, "Raw_dataset")
    if not os.path.exists(target_dataset_dir):
        os.mkdir(target_dataset_dir)
    return raw_data_dir


def get_preprocessed_dataset_dir(dataset_name):
    assert dataset_name in AVAILABLE_DATASET_NAMES
    target_dataset_dir = os.path.join(DATASET_DIR, dataset_name)
    preproc_data_dir = os.path.join(target_dataset_dir, "Preprocessed_dataset")
    if not os.path.exists(target_dataset_dir):
        os.mkdir(target_dataset_dir)
    if not os.path.exists(preproc_data_dir):
        os.mkdir(preproc_data_dir)
    return preproc_data_dir


def get_result_dir(dataset_name):
    target_result_dir = os.path.join(RESULT_DIR, dataset_name)
    if not os.path.exists(target_result_dir):
        os.mkdir(target_result_dir, mode=0o777)
    return target_result_dir
