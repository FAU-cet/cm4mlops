from cmind import utils
import os

def preprocess(i):
    os_info = i['os_info']
    if os_info['platform'] == 'windows':
        return {'return':1, 'error': 'Windows is not supported in this script yet'}

    env = i['env']
    version = env['CM_LIB_ARMNN_VERSION']
    if env.get('CM_HOST_PLATFORM_FLAVOR','') == 'x86_64':
        url = f"https://github.com/ARM-software/armnn/releases/download/{version}/ArmNN-linux-x86_64.tar.gz"
    elif env.get('CM_HOST_PLATFORM_FLAVOR','') == 'arm64':
        url = f"https://github.com/ARM-software/armnn/releases/download/{version}/ArmNN-linux-aarch64.tar.gz"

    env['CM_LIB_ARMNN_PREBUILT_BINARY_URL'] = url
    env['CM_LIB_ARMNN_EXTRACT_FILENAME'] = os.path.basename(url)

    return {'return':0}

def postprocess(i):

    env = i['env']

    paths = [
            "+C_INCLUDE_PATH",
            "+CPLUS_INCLUDE_PATH",
            "+LD_LIBRARY_PATH",
            "+DYLD_FALLBACK_LIBRARY_PATH"
            ]

    for key in paths:
        env[key] = []

    env['+C_INCLUDE_PATH'].append(os.path.join(os.getcwd(), 'include'))
    env['+CPLUS_INCLUDE_PATH'].append(os.path.join(os.getcwd(), 'include'))

    lib_path = os.path.join(os.getcwd())
    env['+LD_LIBRARY_PATH'].append(lib_path)
    env['+DYLD_FALLBACK_LIBRARY_PATH'].append(lib_path)

    return {'return':0}