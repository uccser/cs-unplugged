"""Program for launching the multiple subprocesses for each test configuration."""
import json
import sys
import subprocess


def get_browsers(json_name):
    """Retrieve the browser capabilities from the given file."""
    with open(json_name, "r") as f:
        cap_list = json.loads(f.read())
    return cap_list


def main():
    """Generate a subprocess for each browser configuration and run nosetests on this thread."""
    try:
        json_name = sys.argv[1]
    except IndexError:
        print("Please provide browser config json file as first from command line.")
        sys.exit(1)

    cap_list = get_browsers(json_name)

    processes = []
    results = []
    num_of_tests = len(cap_list)

    print("Automated browser tests have started\nThere are {} user configurations to test.\nPlease wait..."
          .format(num_of_tests))

    for counter in range(num_of_tests):
        cmd = "JSONFILE={} INDEX={} nosetests --process-timeout=60".format(json_name, counter)
        processes.append(subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE))

    for counter in range(num_of_tests):
        results.append(processes[counter].wait())

    if all(result_code == 0 for result_code in results):
        for process in processes:
            print(process.stderr.read().decode("utf-8"))
        print("TESTS PASS")
        sys.exit(0)
    else:
        for process in processes:
            print(process.stderr.read().decode("utf-8"))
        print("TESTS FAILED")
        sys.exit(1)


if __name__ == "__main__":
    main()
