import os
import pprint
import shutil


def rm_all_target():
    path = os.path.dirname(__file__)
    print(path)
    it = os.walk(path)
    targets = []
    for dirpath, dirnames, filenames in it:
        if "target" in dirnames and "Cargo.toml" in filenames:
            targets.append(f"{dirpath}/target")
    pprint.pprint(dict(enumerate(targets)))
    ensure = input("y for ensure; i for interact: ").lower()
    if not ensure:
        return
    if ensure == 'y':
        for target in targets:
            shutil.rmtree(target)
            print(f"remove: {target}")
    elif ensure == 'i':
        for target in targets:
           if input(f"remove \"{target}\"? [y for yes]").lower() == 'y':
                shutil.rmtree(target)
                print(f"remove: {target}")


if __name__ == "__main__":
    rm_all_target()
