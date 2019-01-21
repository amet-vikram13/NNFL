import _plotly_utils.basevalidators


class DthetaValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(self, plotly_name='dtheta', parent_name='barpolar', **kwargs):
        super(DthetaValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type=kwargs.pop('edit_type', 'calc'),
            role=kwargs.pop('role', 'info'),
            **kwargs
        )
