# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Grid(Component):
    """A Grid component.


Keyword arguments:

- children (optional):
    The children of the grid.

- id (optional):
    The ID used to identify this component in Dash callbacks.

- allowOverlap (default False):
    allow overlapping in the grid.

- autoSize (default False):
    If True, container size swells to fit contents.

- cols (default 12):
    The number of columns in the grid.

- compactType (optional):
    Compaction type.

- containerPadding (default [10, 10]):
    Padding inside the container [x, y] in px.

- isBounded (default False):
    Is bounded.

- isDraggable (default True):
    Whether the grid items are draggable.

- isResizable (default True):
    Whether the grid items are resizable.

- layout (optional):
    The layout of the grid, Readonly.

- margin (default [10, 10]):
    Margin between items [x, y] in px.

- preventCollision (default False):
    If True, grid items wont change position when being dragged over.

- resizeHandles (default ['se']):
    Which resize handles to display  s, e, w, n, se, ne, sw, nw.

- rowHeight (default 150):
    The row height of the grid. Default is 150.

- setProps (optional):
    Dash-assigned callback that should be called whenever any of the
    properties change.

- transformScale (default 1):
    If parent DOM node of ResponsiveReactGridLayout or ReactGridLayout
    has \"transform: scale(n)\" css property,  we should set scale
    coefficient to avoid render artefacts while dragging.

- useCSSTransforms (default True):
    Uses CSS3 `translate()` instead of position top/left.  This makes
    about 6x faster paint performance.

- width (optional):
    Initial width of the grid."""
    _children_props = []
    _base_nodes = ['children']
    _namespace = 'dash_grid_layout'
    _type = 'Grid'
    @_explicitize_args
    def __init__(self, children=None, id=Component.UNDEFINED, width=Component.UNDEFINED, autoSize=Component.UNDEFINED, cols=Component.UNDEFINED, compactType=Component.UNDEFINED, layout=Component.UNDEFINED, margin=Component.UNDEFINED, containerPadding=Component.UNDEFINED, rowHeight=Component.UNDEFINED, isDraggable=Component.UNDEFINED, isResizable=Component.UNDEFINED, isBounded=Component.UNDEFINED, useCSSTransforms=Component.UNDEFINED, transformScale=Component.UNDEFINED, allowOverlap=Component.UNDEFINED, preventCollision=Component.UNDEFINED, resizeHandles=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'id', 'allowOverlap', 'autoSize', 'cols', 'compactType', 'containerPadding', 'isBounded', 'isDraggable', 'isResizable', 'layout', 'margin', 'preventCollision', 'resizeHandles', 'rowHeight', 'setProps', 'transformScale', 'useCSSTransforms', 'width']
        self._valid_wildcard_attributes =            []
        self.available_properties = ['children', 'id', 'allowOverlap', 'autoSize', 'cols', 'compactType', 'containerPadding', 'isBounded', 'isDraggable', 'isResizable', 'layout', 'margin', 'preventCollision', 'resizeHandles', 'rowHeight', 'setProps', 'transformScale', 'useCSSTransforms', 'width']
        self.available_wildcard_properties =            []
        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs and excess named props
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        super(Grid, self).__init__(children=children, **args)
