import os
import argparse
import datetime
from src.models import CombineSource
from src.tools import Tools


def combine(bootloader_path, calibration_path, configuration_path, app_path):
    tools = Tools()
    tools.add_combine_source(CombineSource(bootloader_path, 1024 * 32))
    tools.add_combine_source(CombineSource(calibration_path, 1024 * 16))
    tools.add_combine_source(CombineSource(configuration_path, 1024 * 16))
    tools.add_combine_source(CombineSource(app_path))
    tools.export(os.path.join(os.getcwd(), 'export',
                              'combined_fw_{0}.bin'.format(
                                  datetime.datetime.now().strftime('%Y%m%d%H%M%S'))
                              ))


def receive_args():
    """parse input arguments
    """
    parser = argparse.ArgumentParser(
        description='Aceinna python driver input args command:')

    default_bootloader_path = os.path.join(os.getcwd(), 'resource',
                                           'OpenIMU300_Bootloader_4_0_4.bin')
    default_calibration_path = os.path.join(os.getcwd(), 'resource',
                                            'OpenIMU300_Calibration.bin')
    default_configuration_path = os.path.join(
        os.getcwd(), 'resource', 'OpenIMU300_Configuration.bin')
    default_app_path = os.path.join(
        os.getcwd(), 'resource', 'OpenIMU300ZI_IMU_1_1_2.bin')

    parser.add_argument("--bootloader", type=str,
                        help="Bootloader bin path", default=default_bootloader_path)
    parser.add_argument("--calibration", type=str,
                        help="Calibration bin path", default=default_calibration_path)
    parser.add_argument("--configuration", type=str,
                        help="Configuration bin path", default=default_configuration_path)
    parser.add_argument("--app", type=str,
                        help="App bin path", default=default_app_path)
    return parser.parse_args()


if __name__ == '__main__':
    # build a whole fw bin for SN:1808400528
    ARGS = receive_args()
    combine(ARGS.bootloader, ARGS.calibration, ARGS.configuration, ARGS.app)
