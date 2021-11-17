import argparse
CLI=argparse.ArgumentParser()
CLI.add_argument(
  "--lista",  # name on the CLI - drop the `--` for positional/required parameters
  nargs="*",  # 0 or more values expected => creates a list
  type=int,
  default=[],  # default if nothing is provided
)
args = CLI.parse_args()
print("lista: %r" % args.lista)

