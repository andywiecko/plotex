from pathlib import Path
from pkg_resources import resource_listdir, resource_stream
import yaml

from plotex import Exiter


def replace_slash_in_list(list_of_args):
    return [arg.replace("\\", "\\\\") for arg in list_of_args]


def get_available_profiles():
    return [
        Path(path_str).name
        for path_str in resource_listdir("plotex", "profiles")
        if path_str.endswith(".yml")
    ]


def load_profile(profile_name, args):
    try:
        profile = yaml.safe_load(resource_stream("plotex.profiles", f"{profile_name}.yml"))
        if args.terminal:
            profile["terminalSettings"]["terminal"] = args.terminal

        if args.append:
            profile["terminalSettings"]["header"] += replace_slash_in_list(args.append)

        if args.replace:
            profile["terminalSettings"]['header'] = replace_slash_in_list(args.replace)

        return profile
    except FileNotFoundError:
        Exiter.Exit(
            f"Profile `{profile_name}` not found! Check for the typos! "
            f"Profiles available:\n * {get_available_profiles()}"
        )
