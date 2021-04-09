import json
import os
import sys
import uuid

from config.default import default_cy, default_node
from config.layers import layers_dict


def convertToTFjs(model):
    model_TFjs = {}
    model_TFjs["modelTopology"] = model
    return model_TFjs


def convertToCy(model):
    model_cy = default_cy.copy()

    for md in model["config"]["layers"]:
        node = default_node.copy()

        data = {}
        data["name"] = md["name"]
        data["class_name"] = md["class_name"]
        data["weight"] = 75
        data["id"] = uuid.uuid1()

        for root, classes in layers_dict:
            if data["class_name"] in classes:
                data["root"] = root

        if not data.get("root"):
            sys.exit(
                "{} does not exist in the configuration!".format(data["class_name"])
            )

        data["content"] = layers_dict[data["root"]][data["class_name"]]

        ## TODO: 1. generate date content, 2. update edges


with open(os.path.join("test", "test.json")) as f:
    model = json.load(f)

model["keras_version"] = "2.2.4"
model["backend"] = "tensor_flow.js"
