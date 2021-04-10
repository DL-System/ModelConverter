default_cy = {
    "elements": {"nodes": [], "edges": []},
    "style": [
        {
            "selector": "node",
            "style": {
                "text-valign": "center",
                "color": "white",
                "width": "200px",
                "height": "40px",
                "shape": "roundrectangle",
            },
        },
        {
            "selector": 'node[root = "Input Layers"]',
            "style": {"background-color": "#8a93ac"},
        },
        {
            "selector": 'node[root = "Input Layers"]:selected',
            "style": {"background-color": "#019ebd"},
        },
        {
            "selector": 'node[root = "Convolutional Layers"]',
            "style": {"background-color": "#939eac"},
        },
        {
            "selector": 'node[root = "Convolutional Layers"]:selected',
            "style": {"background-color": "#019ebd"},
        },
        {
            "selector": 'node[root = "Merge Layers"]',
            "style": {"background-color": "#93a8b6"},
        },
        {
            "selector": 'node[root = "Merge Layers"]:selected',
            "style": {"background-color": "#019ebd"},
        },
        {
            "selector": 'node[root = "Normalization Layers"]',
            "style": {"background-color": "#93a8c0"},
        },
        {
            "selector": 'node[root = "Normalization Layers"]:selected',
            "style": {"background-color": "#019ebd"},
        },
        {
            "selector": 'node[root = "Pooling Layers"]',
            "style": {"background-color": "#93a8ca"},
        },
        {
            "selector": 'node[root = "Pooling Layers"]:selected',
            "style": {"background-color": "#019ebd"},
        },
        {
            "selector": 'node[root = "Recurrent Layers"]',
            "style": {"background-color": "#93a8a2"},
        },
        {
            "selector": 'node[root = "Recurrent Layers"]:selected',
            "style": {"background-color": "#019ebd"},
        },
        {
            "selector": 'node[root = "Advanced Activations Layers"]',
            "style": {"background-color": "#93a898"},
        },
        {
            "selector": 'node[root = "Advanced Activations Layers"]:selected',
            "style": {"background-color": "#019ebd"},
        },
        {
            "selector": 'node[root = "Core Layers"]',
            "style": {"background-color": "#93a88e"},
        },
        {
            "selector": 'node[root = "Core Layers"]:selected',
            "style": {"background-color": "#019ebd"},
        },
        {
            "selector": 'node[root = "Loss Functions"]',
            "style": {"background-color": "#93a8b6"},
        },
        {
            "selector": 'node[root = "Loss Functions"]:selected',
            "style": {"background-color": "#019ebd"},
        },
        {
            "selector": 'node[root = "Canned Models"]',
            "style": {"background-color": "#e29a47", "height": "90px"},
        },
        {
            "selector": 'node[root = "Canned Models"]:selected',
            "style": {"background-color": "#019ebd"},
        },
        {
            "selector": "edge",
            "style": {"curve-style": "bezier", "target-arrow-shape": "triangle"},
        },
        {
            "selector": ".eh-handle",
            "style": {
                "background-color": "#666666",
                "width": "12px",
                "height": "12px",
                "shape": "ellipse",
                "overlay-opacity": "0",
                "border-width": "12px",
                "border-opacity": "0",
            },
        },
        {"selector": ".eh-hover", "style": {"background-color": "#666666"}},
        {
            "selector": ".eh-source",
            "style": {"border-width": "2px", "border-color": "#666666"},
        },
        {
            "selector": ".eh-target",
            "style": {"border-width": "2px", "border-color": "#666666"},
        },
        {
            "selector": ".eh-preview, .eh-ghost-edge",
            "style": {
                "background-color": "#666666",
                "line-color": "#666666",
                "target-arrow-color": "#666666",
                "source-arrow-color": "#666666",
            },
        },
        {
            "selector": ".eh-ghost-edge .eh-preview-active",
            "style": {"opacity": "0"},
        },
        {
            "selector": ":parent",
            "style": {
                "background-opacity": "0.333",
                "background-color": "#e29a47",
                "border-width": "2px",
                "border-color": "#666666",
            },
        },
        {
            "selector": "node.cy-expand-collapse-collapsed-node",
            "style": {"background-color": "#e29a47", "height": "90px"},
        },
        {
            "selector": ".edgebendediting-hasbendpoints",
            "style": {
                "curve-style": "segments",
                "segment-distances": "fn",
                "segment-weights": "fn",
                "edge-distances": "node-position",
            },
        },
    ],
    "zoomingEnabled": True,
    "userZoomingEnabled": False,
    "zoom": 1.2,
    "minZoom": 1e-50,
    "maxZoom": 1.2,
    "panningEnabled": True,
    "userPanningEnabled": True,
    "pan": {"x": 311.3, "y": 308.70000000000005},
    "boxSelectionEnabled": True,
    "renderer": {"name": "canvas"},
}

default_node = {
    "data": {},
    "position": {"x": 101, "y": None},
    "group": "nodes",
    "removed": False,
    "selected": False,
    "selectable": True,
    "locked": False,
    "grabbable": True,
    "classes": "",
}

default_edge = {
    "data": {},
    "position": {},
    "group": "edges",
    "removed": False,
    "selected": False,
    "selectable": True,
    "locked": False,
    "grabbable": True,
    "classes": "",
}
