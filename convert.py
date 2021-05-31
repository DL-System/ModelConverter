import json
import copy
import os
import sys
import shutil
import uuid
import argparse

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

from tensorflow import keras
from config.default import default_cy, default_node, default_edge
from config.layers import layers_dict

KERAS_VERSION = "2.2.4"
BACKEND = "tensor_flow.js"
depth, position_y = 0, 21


def convertToTFjs(model):
    model_TFjs = {}
    model_json = json.loads(model.to_json())
    model_json["keras_version"] = KERAS_VERSION
    model_json["backend"] = BACKEND
    model_TFjs["modelTopology"] = model_json
    return model_TFjs


def convertToCy(model):
    model_cy = copy.deepcopy(default_cy)

    layers = model.layers
    model_json = json.loads(model.to_json())
    configs = model_json["config"]["layers"]
    ids = []

    for i in range(len(layers)):
        config = configs[i]
        layer_config = layers[i].get_config()
        node = createNode(layer_config, config)
        ids.append(node["data"]["id"])

        model_cy["elements"]["nodes"].append(node)

    edges = createEdges(ids)
    model_cy["elements"]["edges"] = edges

    return model_cy

    ## TODO: 2. update edges


def createNode(layer_config, config):
    global depth, position_y
    node = copy.deepcopy(default_node)
    node["position"]["y"] = position_y
    position_y += 90

    data = {}
    data["name"] = config["name"]
    data["class_name"] = config["class_name"]
    data["weight"] = 75
    data["id"] = str(uuid.uuid1())
    data["depth"] = depth
    depth += 1

    for root, classes in layers_dict.items():
        if data["class_name"] in classes:
            data["root"] = root

    if not data.get("root"):
        sys.exit("{} does not exist in the configuration!".format(data["class_name"]))

    data["content"] = layers_dict[data["root"]][data["class_name"]]

    for con in data["content"]:
        if con == "input_shape":
            data["content"][con]["value"] = [
                l for l in layer_config["batch_input_shape"] if l
            ]
        elif not isinstance(data["content"][con], dict):
            continue
        elif data["content"][con]["type"] == "select":
            for val in data["content"][con]["options"]:
                if isinstance(val, str) and layer_config[con]:
                    if isinstance(layer_config[con], dict):
                        if val.lower() == layer_config[con]["class_name"].lower():
                            data["content"][con]["value"] = val
                    elif isinstance(layer_config[con], str):
                        if val.lower() == layer_config[con].lower():
                            data["content"][con]["value"] = val
                else:
                    if val == layer_config[con]:
                        data["content"][con]["value"] = val
        else:
            data["content"][con]["value"] = layer_config[con]

    data["content"]["name"] = {"type": "text", "value": config["name"]}
    node["data"] = copy.deepcopy(data)

    return node


def createEdges(ids):
    edges = []
    for i in range(len(ids) - 1):
        edge = copy.deepcopy(default_edge)
        edge["data"]["source"] = ids[i]
        edge["data"]["target"] = ids[i + 1]
        edge["data"]["id"] = str(uuid.uuid1())

        edges.append(edge)

    return edges


if __name__ == "__main__":
    root_path = os.getenv("DATA_ROOT_PATH") or "."

    parser = argparse.ArgumentParser(description="Model Converter for System.")

    parser.add_argument(
        "-n", "--name", dest="model_name", default="model", help="Model Name"
    )

    parser.add_argument(
        "-p", "--model", dest="model_path", default=None, help="Model Path"
    )

    parser.add_argument("-g", "--generate", action="store_true")

    args = parser.parse_args()

    if not args.model_path:
        model_path = os.path.join("test", "model.h5")
    else:
        model_path = args.model_path

    files_path = os.path.join(
        os.path.abspath(root_path), "test", "models", args.model_name
    )

    if os.path.isdir(files_path):
        sys.exit("Please input a different model name!")
    else:
        os.makedirs(files_path)

    model = keras.models.load_model(model_path)

    model_TFjs = convertToTFjs(model)

    model_cy = convertToCy(model)

    if args.generate:
        pkl_path = os.path.join(files_path, args.model_name + ".pkl")
        open(pkl_path, "a").close()
        paths = ["checkpoints", "custom", "log", "tmp"]
        for p in paths:
            os.makedirs(os.path.join(files_path, p), exist_ok=True)

        with open(
            os.path.join(files_path, "custom", args.model_name + "_tfjs.json"), "w"
        ) as c:
            json.dump(model_TFjs, c, indent=4, separators=(",", ":"))

        with open(
            os.path.join(files_path, "custom", args.model_name + "_cy.json"), "w"
        ) as c:
            json.dump(model_cy, c, indent=4, separators=(",", ":"))

        with open(os.path.join(files_path, "config.ini"), "w") as c:
            c.write("[PATHS]\n")
            c.write(
                "checkpoint_dir = {}\n".format(os.path.join(files_path, "checkpoints"))
            )
            c.write("custom_model = {}\n".format(os.path.join(files_path, "custom")))
            c.write(
                "export_dir = {}\n".format(
                    os.path.join(files_path, "checkpoints", "export", "best_exporter")
                )
            )
            c.write("log_dir = {}\n".format(os.path.join(files_path, "log")))
            c.write("tmp_dir = {}\n".format(os.path.join(files_path, "tmp")))
            c.write("data_path = {}\n".format(pkl_path))

        model_dest = os.path.join(root_path, "backup", args.model_name + ".h5")
        print(f"Move the model source to {model_dest}!")
        os.makedirs(os.path.join(root_path, "backup"), exist_ok=True)
        shutil.move(model_path, model_dest)

    else:
        print(json.dumps(model_TFjs))
        print(json.dumps(model_cy))
