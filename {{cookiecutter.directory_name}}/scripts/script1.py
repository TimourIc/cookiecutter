import yaml
import argparse

#config_params:
with open("config/config.yaml", "r") as file:
    config_data = yaml.safe_load(file)
data_path = config_data["paths"]["data_path"]
results_path= config_data["paths"]["results_path"]


if __name__=="__main__":

    parser = argparse.ArgumentParser(description="description of script")
    parser.add_argument(
    "--ARGUMENT", default="Hello World", type=str, help=f"ARGUMENT"
    )
    args=parser.parse_args()
    print(args.ARGUMENT)
