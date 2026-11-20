import argparse
from run_experiment import run_experiment


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description="Run and experiment")
    parser.add_argument(
        "-e",
        "--experiment",
        type=int,
        help="Enter the experiment number or -1 to run all",
    )

    args = parser.parse_args(argv)
    assert args.experiment in [-1, 1, 2, 3]
    experiments = [1, 2, 3] if args.experiment == -1 else [args.experiment]
    for experiment in experiments:
        run_experiment(experiment)


if __name__ == "__main__":
    main()
