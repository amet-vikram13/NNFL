import _plotly_utils.basevalidators


class SplomValidator(_plotly_utils.basevalidators.CompoundValidator):

    def __init__(self, plotly_name='splom', parent_name='', **kwargs):
        super(SplomValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            data_class_str=kwargs.pop('data_class_str', 'Splom'),
            data_docs=kwargs.pop(
                'data_docs', """
            customdata
                Assigns extra data each datum. This may be
                useful when listening to hover, click and
                selection events. Note that, "scatter" traces
                also appends customdata items in the markers
                DOM elements
            customdatasrc
                Sets the source reference on plot.ly for
                customdata .
            diagonal
                plotly.graph_objs.splom.Diagonal instance or
                dict with compatible properties
            dimensions
                plotly.graph_objs.splom.Dimension instance or
                dict with compatible properties
            dimensiondefaults
                When used in a template (as
                layout.template.data.splom.dimensiondefaults),
                sets the default property values to use for
                elements of splom.dimensions
            hoverinfo
                Determines which trace information appear on
                hover. If `none` or `skip` are set, no
                information is displayed upon hovering. But, if
                `none` is set, click and hover events are still
                fired.
            hoverinfosrc
                Sets the source reference on plot.ly for
                hoverinfo .
            hoverlabel
                plotly.graph_objs.splom.Hoverlabel instance or
                dict with compatible properties
            ids
                Assigns id labels to each datum. These ids for
                object constancy of data points during
                animation. Should be an array of strings, not
                numbers or any other type.
            idssrc
                Sets the source reference on plot.ly for  ids .
            legendgroup
                Sets the legend group for this trace. Traces
                part of the same legend group hide/show at the
                same time when toggling legend items.
            marker
                plotly.graph_objs.splom.Marker instance or dict
                with compatible properties
            name
                Sets the trace name. The trace name appear as
                the legend item and on hover.
            opacity
                Sets the opacity of the trace.
            selected
                plotly.graph_objs.splom.Selected instance or
                dict with compatible properties
            selectedpoints
                Array containing integer indices of selected
                points. Has an effect only for traces that
                support selections. Note that an empty array
                means an empty selection where the `unselected`
                are turned on for all points, whereas, any
                other non-array values means no selection all
                where the `selected` and `unselected` styles
                have no effect.
            showlegend
                Determines whether or not an item corresponding
                to this trace is shown in the legend.
            showlowerhalf
                Determines whether or not subplots on the lower
                half from the diagonal are displayed.
            showupperhalf
                Determines whether or not subplots on the upper
                half from the diagonal are displayed.
            stream
                plotly.graph_objs.splom.Stream instance or dict
                with compatible properties
            text
                Sets text elements associated with each (x,y)
                pair to appear on hover. If a single string,
                the same string appears over all the data
                points. If an array of string, the items are
                mapped in order to the this trace's (x,y)
                coordinates.
            textsrc
                Sets the source reference on plot.ly for  text
                .
            uid

            uirevision
                Controls persistence of some user-driven
                changes to the trace: `constraintrange` in
                `parcoords` traces, as well as some `editable:
                true` modifications such as `name` and
                `colorbar.title`. Defaults to
                `layout.uirevision`. Note that other user-
                driven trace attribute changes are controlled
                by `layout` attributes: `trace.visible` is
                controlled by `layout.legend.uirevision`,
                `selectedpoints` is controlled by
                `layout.selectionrevision`, and
                `colorbar.(x|y)` (accessible with `config:
                {editable: true}`) is controlled by
                `layout.editrevision`. Trace changes are
                tracked by `uid`, which only falls back on
                trace index if no `uid` is provided. So if your
                app can add/remove traces before the end of the
                `data` array, such that the same trace has a
                different index, you can still preserve user-
                driven changes if you give each trace a `uid`
                that stays with it as it moves.
            unselected
                plotly.graph_objs.splom.Unselected instance or
                dict with compatible properties
            visible
                Determines whether or not this trace is
                visible. If "legendonly", the trace is not
                drawn, but can appear as a legend item
                (provided that the legend itself is visible).
            xaxes
                Sets the list of x axes corresponding to
                dimensions of this splom trace. By default, a
                splom will match the first N xaxes where N is
                the number of input dimensions. Note that, in
                case where `diagonal.visible` is false and
                `showupperhalf` or `showlowerhalf` is false,
                this splom trace will generate one less x-axis
                and one less y-axis.
            yaxes
                Sets the list of y axes corresponding to
                dimensions of this splom trace. By default, a
                splom will match the first N yaxes where N is
                the number of input dimensions. Note that, in
                case where `diagonal.visible` is false and
                `showupperhalf` or `showlowerhalf` is false,
                this splom trace will generate one less x-axis
                and one less y-axis.
"""
            ),
            **kwargs
        )
