from dash_snap_grid import ResponsiveGrid, DraggableDiv
from dash import Dash, html, Input, Output, dcc, State, ctx, ALL
import dash_mantine_components as dmc
import random
from dash_iconify import DashIconify

app = Dash(__name__)


def card(id, title, text, bg=1):
    return dmc.Card(
        id=id,
        children=[
            dmc.CardSection(
                dmc.Image(
                    src=f"https://raw.githubusercontent.com/mantinedev/mantine/master/.demo/images/bg-{bg}.png",
                    alt="Norway",
                    style={"maxHeight": 100, "objectFit": "cover"},
                )
            ),
            dmc.Space(h=10),
            dmc.Text(title, fw=500),
            dmc.Text(
                text,
                size="sm",
                c="dimmed",
            ),
            dmc.ActionIcon(
                DashIconify(icon="material-symbols:close"),
                radius="xl",
                id={"type": "close", "index": id},
                className="dont-drag",
                style={"position": "absolute", "top": 0, "right": 0},
                variant="transparent",
                color="gray",
            ),
        ],
        withBorder=True,
        shadow="sm",
        radius="md",
        h="100%",
    )


initial_layout = [
    {"i": "a", "x": 0, "y": 0, "w": 2, "h": 2},
    {"i": "b", "x": 2, "y": 0, "w": 2, "h": 2, "isResizable": False},
    {"i": "c", "x": 4, "y": 0, "w": 2, "h": 2, "static": True},
    {"i": "d", "x": 6, "y": 0, "w": 3, "h": 2, "minW": 3},
]

app.layout = dmc.MantineProvider(
    [
        dcc.Store(id="layout-store", storage_type="local"),
        html.Div(
            [
                dmc.Group(
                    [
                        dmc.Button("Save Layout", id="save-layout"),
                        dmc.Button("Reset Layout", id="reset-layout"),
                        dmc.Button("Add New", id="add-new"),
                        DraggableDiv(
                            id="draggable-div", children=[dmc.Button("Drag me")]
                        ),
                    ]
                ),
                ResponsiveGrid(
                    id="input",
                    layouts={"lg": initial_layout},
                    cols={"lg": 12, "md": 6, "sm": 2, "xs": 1},
                    rowHeight=100,
                    preventCollision=True,
                    compactType="vertical",
                    draggableCancel=".dont-drag",
                    resizeHandles=["sw", "se", "nw", "ne"],
                    isDroppable=True,
                    children=[
                        card("a", "Regular Card", "This is a regular grid item"),
                        card(
                            "b",
                            "Non-Resizable Card",
                            "This card cannot be resized, but can still be moved",
                            bg=2,
                        ),
                        card(
                            "c",
                            "Fixed card",
                            "This card cannot be resized or moved",
                            bg=7,
                        ),
                        card(
                            "d",
                            "Card with min-width",
                            "This card has a minimum width of 3 grid columns",
                            bg=8,
                        ),
                    ],
                ),
                dmc.Text(id="output"),
            ],
            style={"padding": "20px"},
        ),
    ]
)


@app.callback(
    Output("layout-store", "data"),
    Input("save-layout", "n_clicks"),
    Input("reset-layout", "n_clicks"),
    State("input", "layouts"),
    prevent_initial_call=True,
)
def update_layout(save_click, reset_click, layouts):
    if ctx.triggered_id == "save-layout":
        return layouts
    return {}


@app.callback(
    Output("input", "layouts", allow_duplicate=True),
    Input("layout-store", "data"),
    prevent_initial_call=True,
)
def retrieve_layouts(layouts):
    if not layouts:
        return {"lg": initial_layout}
    return layouts


@app.callback(
    Output("input", "children"),
    Output("input", "layouts"),
    Input("add-new", "n_clicks"),
    Input({"type": "close", "index": ALL}, "n_clicks"),
    Input("input", "droppedItem"),
    State("input", "children"),
    State("input", "layouts"),
    State("layout-store", "data"),
    prevent_initial_call=True,
)
def add_new(n_clicks, close_clicks, dropped_item, children, layouts, stored_layouts):
    if ctx.triggered_id == "add-new":
        bg = random.randint(1, 9)
        children.append(
            card(
                f"new-{len(children)}",
                "New Card",
                "This card was added dynamically",
                bg=bg,
            )
        )
        if stored_layouts:
            layouts = stored_layouts
    elif isinstance(ctx.triggered_id, dict) and ctx.triggered_id["type"] == "close":
        children = [
            child
            for child in children
            if child["props"]["id"] != ctx.triggered_id["index"]
        ]
    elif ctx.triggered_id == "input" and dropped_item:
        bg = random.randint(1, 9)
        dropped_item["i"] = f"new-{len(children)}"
        children.append(
            card(
                dropped_item["i"],
                "New Card",
                "This card was added by dropping an item",
                bg=bg,
            )
        )
        for key in layouts.keys():
            layouts[key].append(dropped_item)

    return children, layouts


if __name__ == "__main__":
    app.run_server(debug=True)
