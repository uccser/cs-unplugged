import json
import sys
import subprocess


def get_browsers(json_name):
    with open(json_name, "r") as f:
        cap_list = json.loads(f.read())
    return cap_list


def main():
    try:
        json_name = sys.argv[1]
    except IndexError:
        print("Please provide browser config json file as first from command line.")
        sys.exit(1)

    cap_list = get_browsers(json_name)

    process = []
    num_of_tests = len(cap_list)

    for counter in range(num_of_tests):
        cmd = "JSONFILE={} INDEX={} nosetests --process-timeout=60".format(json_name, counter)
        process.append(subprocess.Popen(cmd, shell=True))

    for counter in range(num_of_tests):
        process[counter].wait()


if __name__ == "__main__":
    main()
