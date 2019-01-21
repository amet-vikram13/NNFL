import _plotly_utils.basevalidators


class NbinsxValidator(_plotly_utils.basevalidators.IntegerValidator):

    def __init__(
        self, plotly_name='nbinsx', parent_name='histogram', **kwargs
    ):
        super(NbinsxValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            min=kwargs.pop('min', 0),
            role=kwargs.pop('role', 'style'),
            **kwargs
        )
