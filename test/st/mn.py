import argparse

# Parsing of args
def parse_args():

    # init
    parser = argparse.ArgumentParser(
        description="Promodoro CLI"
    )

    # Acceptable arguments
    parser.add_argument("--silent",action="store_true", help="Disable sound effects")

    # It returns a BUILD ARGS PARSER
    return parser.parse_args()

args = parse_args()  # Creation and assigning

if args.silent:  #testing
    print("It's Silent")