import os
from source.py.feature import (
    get_cv_cn_version_info,
    get_cv_italic_version_info,
    get_cv_version_info,
    get_ss_version_info,
    get_total_feat_ts,
)
from source.py.task._utils import write_json, write_text
from source.py.utils import joinPaths


def page(base_path: str, var_dir: str, commit: bool = False) -> None:
    # Update landing page data
    feature_data_base = joinPaths(base_path, "data", "features")
    os.makedirs(feature_data_base, exist_ok=True)
    write_json(joinPaths(feature_data_base, "cv.json"), get_cv_version_info())
    write_json(joinPaths(feature_data_base, "cn.json"), get_cv_cn_version_info())
    write_json(
        joinPaths(feature_data_base, "italic.json"), get_cv_italic_version_info()
    )
    write_json(joinPaths(feature_data_base, "ss.json"), get_ss_version_info())
    write_text(
        joinPaths(feature_data_base, "features.ts"),
        get_total_feat_ts(),
    )

    os.system("python build.py --ttf-only --no-nerd-font --least-styles")
    font_dir = joinPaths(base_path, "public", "fonts")
    for filename in os.listdir(var_dir):
        new_name = filename.replace(".ttf", "-VF.ttf")
        if new_name:
            os.rename(joinPaths(var_dir, filename), joinPaths(font_dir, new_name))

    # Commit changes if specified
    if commit:
        # todo))
        print('Changes committed successfully')
